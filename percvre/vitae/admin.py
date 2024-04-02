from django.contrib import admin

from percvre.vitae.models import Experience, Education, Trivia


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    pass


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    pass


@admin.register(Trivia)
class TriviaAdmin(admin.ModelAdmin):
    pass
