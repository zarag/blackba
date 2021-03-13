from coupons.models import Coupon
from django.utils.timezone import now
from django.views import generic


class HomeView(generic.ListView):
    template = "coupons/coupon_list.html"
    # queryset = Coupon.objects.a()
    # paginate_by = 10

    def get_queryset(self):
        return Coupon.objects.filter(end_time__gte=now()).order_by("-start_time")

    context_object_name = "coupons"
