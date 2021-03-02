from django.db import models
from django.utils import timezone
from partners.models import Partner
from tinymce.models import HTMLField
from versatileimagefield.fields import VersatileImageField


class Coupon(models.Model):
    title = models.CharField(max_length=256, blank=True)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, null=True)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    description = HTMLField()
    photo = VersatileImageField(upload_to="coupon-avatars", blank=True, null=True)
