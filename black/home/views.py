from coupons.models import Coupon
from django.db.models import Q
from django.views import generic


class HomeView(generic.ListView):
    template_name = "base.html"

    def get_queryset(self):
        return Coupon.objects.filter(Q(top_offer=True))

    context_object_name = "top_offers"
