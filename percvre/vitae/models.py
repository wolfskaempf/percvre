from typing import Self

from django.db import models
from django.utils.translation import gettext_lazy as _


class Recipient(models.Model):
    """Represent a CV recipient, granting access to the personal data section."""

    name = models.CharField(max_length=128)
    token = models.CharField(max_length=64)

    class Meta:
        verbose_name = _("Recipient")
        verbose_name_plural = _("Recipients")

    def __str__(self: Self) -> str:
        return self.name


class PersonalData(models.Model):
    """Represent the CV owners personal data."""

    # This model uses text fields without a length limit since it is impossible to validate
    # what a valid name, place of birth etc. is when taking account all customs around naming worldwide
    at_a_glance = models.TextField()
    name = models.TextField()
    position = models.TextField()
    place_of_birth = models.TextField()
    date_of_birth = models.DateField()
    telephone = models.TextField()
    email = models.TextField()
    nationality = models.TextField()
    # The address format assumes the operator lives in a country with a Germany-ish address format
    address_zip = models.TextField()
    address_city = models.TextField()
    address_street = models.TextField()

    class Meta:
        verbose_name = _("Personal data")
        verbose_name_plural = _("Personal data")

    def __str__(self: Self) -> str:
        return self.name


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
        return f"{self.title} - {self.organisation}"


class Education(models.Model):
    """Represent a part of the educational path."""

    institute = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    start_description = models.CharField(max_length=32)
    end_description = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ("-start_date", "pk")
        verbose_name = _("Education")
        verbose_name_plural = _("Education")

    def __str__(self: Self) -> str:
        return f"{self.title} - {self.institute}"


class Reference(models.Model):
    """Reference to other resources."""

    name = models.CharField(max_length=128)
    link = models.URLField()


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
