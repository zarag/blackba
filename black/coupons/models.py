from django.db import models
from django.utils import timezone
from partners.models import Partner
from tinymce.models import HTMLField


class Image(models.Model):
    image = models.ImageField()


class Coupon(models.Model):
    title = models.CharField(max_length=256, blank=True)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, null=True)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    description = HTMLField()
    photos = models.ManyToManyField(Image)
    price_before = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    price_now = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    @property
    def days_left(self):
        return abs((timezone.now - self.end_time).days)
