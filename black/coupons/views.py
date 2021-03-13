from django.views.generic import DetailView

from .models import Coupon


class CouponDetail(DetailView):
    model = Coupon
