# percvre

[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/wolfskaempf/percvre/build-container-image.yml?branch=main)](https://github.com/wolfskaempf/percvre/actions/workflows/build-container-image.yml)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/wolfskaempf/percvre?color=success)](https://github.com/wolfskaempf/percvre/releases)
[![pre-commit enabled](https://img.shields.io/badge/pre--commit-enabled-success?logo=pre-commit)](./.pre-commit-config.yaml)
[![OCI Container image available](https://img.shields.io/badge/Container%20Image-amd64%20%7C%20arm64-success?logo=Open%20Containers%20Initiative)](https://github.com/wolfskaempf/percvre/pkgs/container/percvre)
[![Mastodon Follow](https://img.shields.io/mastodon/follow/109321997385535274?domain=https%3A%2F%2Fclimatejustice.social&style=social)](https://climatejustice.social/@wolfskaempf)

A personal CV app written in Python with Django.

## Before you reuse this
- Until this notice is removed you need to replace static files,
  including favicons, webmanifest and profile picture yourself. The license does not cover usage
  of these files and all rights are reserved.

## Instantly run a local demo
Instantly run a local instance of `percvre` using `podman`, `docker` or any other container engine.

First, start the container.
```bash
docker run --rm -e PERCVRE_USE_SQLITE=True -e PERCVRE_ALLOWED_HOSTS=localhost -e PERCVRE_CSRF_TRUSTED_ORIGINS=http://localhost:8082 -v percvre-db:/app/src/persistent_db --name percvre-localhost -p 8082:80 ghcr.io/wolfskaempf/percvre:latest
```

Then, in a separate shell window you'll need to run database migrations to initialise the SQLite database and create an administrative account by running the following command.

```bash
docker exec -i -t percvre-localhost /bin/sh -c "python manage.py migrate && python manage.py createsuperuser"
```

Now you can access your local instance at http://localhost:8082/ and the administrative area at http://localhost:8082/admin/

If you have any feedback, do not hesitate to contact me or open an issue.

# Deploy using Caprover
[Caprover](https://caprover.com/) is a tool that turns your personal VPS into a Platform as a Service comparable to [dokku](https://dokku.com/) or Heroku.

1. [Get started with Caprover on your VPS and your CLI](https://caprover.com/docs/get-started.html)
2. Create a One-Click-Postgres app and remember the data you chose (app name, default database, user and password).
3. Create a new app named anything you like in the Caprover interface. This tutorial will go with `percvre` for the app name.
4. Inside the `HTTP Settings` section of the new app enable HTTPS and select `Force HTTPS by redirecting all HTTP traffic to HTTPS`
5. Inside the `App Configs` section of the new app configure the app specific environment variables described in [example.env](./example.env)
- Ensure you have added all environment variables that start with `PERCVRE` (do not copy the `POSTGRES` variables into the `App Configs` section of the `percvre` app)
- Ensure the database connection information matches the database you created earlier
    - The `PERCVRE_POSTGRES_HOST` can be found in the app overview of the database you created earlier
    - It should look something like this `srv-captain--percvre-db` where `percvre-db` is the name you selected for your database
    - Ensure you include only the hostname and no protocol (such as https://) in `PERCVRE_POSTGRES_HOST`
6. On your local machine run `git clone https://github.com/wolfskaempf/percvre.git && cd percvre` to clone this repository and change directory into it.
7. Run `npx caprover deploy` and select your server and the app you just created
    * If this command doesn't exist, make sure that you followed [Step 3 of Getting Started with Caprover](https://caprover.com/docs/get-started.html#step-3-install-caprover-cli)
