from django.urls import path

from percvre.vitae import views
from percvre.vitae.views import CvView

app_name = "vitae"

urlpatterns = [
    path("cv/", CvView.as_view(), name="cv"),
    path("personal_data/", views.request_personal_data, name="request_personal_data"),
]
