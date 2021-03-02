from django import forms
from django.contrib import admin

from .models import Partner


class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        exclude = ["name"]


class PartnerAdmin(admin.ModelAdmin):
    form = PartnerForm
