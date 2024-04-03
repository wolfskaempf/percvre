FROM docker.io/python:3.12

# Setup pipx to be accessible by all users
ENV PIPX_HOME=/app/.local/pipx \
    PIPX_BIN_DIR=/app/.local/bin \
    PATH=/app/.local/bin:$PATH

# Install pipx and poetry
RUN python3 -m pip install pipx
RUN pipx install poetry

# Set WORKDIR
WORKDIR /app/src

# Setup poetry to use /app/src/.venv as path
RUN poetry config virtualenvs.in-project true

# Copy poetry environment information
COPY pyproject.toml poetry.lock /app/src/

# Install system dependencies
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y tini && \
    rm -rf /var/lib/apt/lists/*

RUN poetry install

# Setup ENV
ENV VENV_PATH="/app/src/.venv"
ENV PATH="$VENV_PATH/bin:${PATH}"

# Copy application
COPY . /app/src

# Ensure static files exist
RUN DJANGO_SECRET_KEY=oneshot-invalid python manage.py collectstatic --noinput

# Setup ENV for gunicorn startup
ENV WEB_CONCURRENCY=4 \
    WORKER_TIMEOUT=600 \
    WORKER_MAX_REQUESTS=1000 \
    WORKER_LOGLEVEL=warning

ENTRYPOINT ["/usr/bin/tini", "--"]
CMD ["gunicorn", "percvre.wsgi", "--bind=0.0.0.0:80"]
EXPOSE 80
