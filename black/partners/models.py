from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from utils.validators import validate_possible_number
from versatileimagefield.fields import VersatileImageField
from django.utils.translation import gettext_lazy as _


class PossiblePhoneNumberField(PhoneNumberField):
    """Less strict field for phone numbers written to database."""

    default_validators = [validate_possible_number]


class Partner(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=256, blank=True, verbose_name=_("Partner's first name"))
    last_name = models.CharField(max_length=256, blank=True)
    city = models.CharField(max_length=256, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    addresses = models.TextField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    date_joined = models.DateTimeField(default=timezone.now, editable=False)
    avatar = VersatileImageField(upload_to="partner-avatars", blank=True, null=True)
    phone = PossiblePhoneNumberField(blank=True, default="", region="BA")
    # objects = UserManager()
