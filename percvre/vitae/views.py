from typing import Self

from django.contrib import messages
from django.db.models import QuerySet
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views.generic import TemplateView

from percvre.vitae.forms import TokenForm
from percvre.vitae.models import (
    Experience,
    Education,
    PersonalData,
    Recipient,
    Trivia,
    Reference,
)


class CvView(TemplateView):
    template_name = "vitae/cv.html"

    def get_context_data(self: Self, **kwargs) -> QuerySet:
        context = super().get_context_data(**kwargs)
        context["work_exps"] = Experience.objects.filter(experience_type="WORK")
        context["volunteer_exps"] = Experience.objects.filter(
            experience_type="VOLUNTEER"
        )
        context["education"] = Education.objects.all()
        context["trivia"] = Trivia.objects.all()
        context["references"] = Reference.objects.all()
        personal_data = PersonalData.objects.first()
        context["public_personal_data"] = {
            "name": personal_data.name,
            "at_a_glance": personal_data.at_a_glance,
            "position": personal_data.position,
        }
        return context


def request_personal_data(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = TokenForm(request.POST)
        if form.is_valid():
            tokens = [recipient.token.lower() for recipient in Recipient.objects.all()]
            if form.cleaned_data["token"].lower() not in tokens:
                messages.add_message(
                    request,
                    messages.INFO,
                    "The company you entered was not recognized.",
                )
                # Use 200 return code instead of 401 to avoid additional configuration needed for htmx
                return render(
                    request=request,
                    template_name="vitae/partials/_cv_personal_data_form.html",
                )
            context = {"personal_data": PersonalData.objects.first()}
            return render(
                request=request,
                template_name="vitae/partials/_cv_personal_data.html",
                context=context,
            )
    messages.add_message(request, messages.INFO, "You did not enter a company name.")
    # Use 200 return code instead of 401 to avoid additional configuration needed for htmx
    return render(
        request=request,
        template_name="vitae/partials/_cv_personal_data_form.html",
    )
