from typing import Self

from django.db import models
from django.utils.translation import gettext_lazy as _


class Experience(models.Model):
    """Represent working or volunteering experience."""

    class ExperienceTypes(models.TextChoices):
        """Define the type of experience."""

        PLANNING = "WORK", _("Work")
        EXECUTION = "VOLUNTEER", _("Volunteer")

    experience_type = models.CharField(
        choices=ExperienceTypes.choices,
        max_length=10,
    )
    organisation = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    start_description = models.CharField(max_length=32)
    end_description = models.CharField(max_length=32)
    description = models.TextField()
    highlight = models.BooleanField(default=False)

    class Meta:
        ordering = ("-start_date", "pk")
        verbose_name = _("Experience")
        verbose_name_plural = _("Experience")

    def __str__(self: Self) -> str:
        return f"{self.title} - {self.company}"


class Education(models.Model):
    """Represent a part of the educational path."""

    institute = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    start_description = models.CharField(max_length=32)
    end_description = models.CharField(max_length=32)
    description = models.TextField()

    class Meta:
        ordering = ("-start_date", "pk")
        verbose_name = _("Education")
        verbose_name_plural = _("Education")

    def __str__(self: Self) -> str:
        return f"{self.title} - {self.institute}"


class Trivia(models.Model):
    """Represent a piece of trivia."""

    order = models.PositiveSmallIntegerField()
    description = models.TextField()
    highlight = models.BooleanField(default=False)

    class Meta:
        ordering = ("order", "pk")
        verbose_name = _("Trivia")
        verbose_name_plural = _("Trivia")

    def __str__(self: Self) -> str:
        return self.description
