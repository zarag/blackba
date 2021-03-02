from django.views import generic

from black.coupons.models import Coupon


class HomeView(generic.ListView):
    model = Coupon
