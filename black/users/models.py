from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from utils.validators import validate_possible_number


class PossiblePhoneNumberField(PhoneNumberField):
    """Less strict field for phone numbers written to database."""

    default_validators = [validate_possible_number]


class User(AbstractUser):
    """Default user for blackba."""

    GENDER_CHOICES = (
        (u"M", _(u"Male")),
        (u"F", _(u"Female")),
    )

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    birthday = models.DateField(_("birthday"), null=True)
    last_name = None  # type: ignore
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, null=True)
    phone = PossiblePhoneNumberField(blank=True, default="")

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
