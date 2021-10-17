from django.contrib import admin

from .models import Coupon, Image


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    def partner_first_name(self, obj):
        return obj.partner.first_name

    def get_form(self, request, obj=None, **kwargs):
        form = super(CouponAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields["partner"].label_from_instance = lambda obj: "{} {}".format(
            obj.first_name, obj.last_name
        )
        return form

    list_display = ("partner_first_name", "title")
    search_fields = ("partner__first_name", "title")
    list_filter = ('partner__first_name',)

@admin.register(Image)
class CouponImage(admin.ModelAdmin):
    list_display = ["image"]
