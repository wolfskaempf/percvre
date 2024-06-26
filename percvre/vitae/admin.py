from django.contrib import admin

from percvre.vitae.models import (
    Experience,
    Education,
    Trivia,
    Recipient,
    PersonalData,
    Reference,
)


@admin.register(Recipient)
class RecipientAdmin(admin.ModelAdmin):
    pass


@admin.register(PersonalData)
class PersonalDataAdmin(admin.ModelAdmin):
    pass


@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    pass


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    pass


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    pass


@admin.register(Trivia)
class TriviaAdmin(admin.ModelAdmin):
    pass
