from django.db.models import Q
from django.utils.timezone import now
from django.views import generic
from django.views.generic import DetailView

from .models import Coupon


class CouponDetail(DetailView):
    model = Coupon


class CouponListView(generic.ListView):
    template = "coupons/coupon_list.html"
    # queryset = Coupon.objects.a()
    # paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get("q")
        search_term = query if query else ""
        return Coupon.objects.filter(
            Q(title__icontains=search_term), end_time__gte=now()
        ).order_by("-start_time")

    # def get_queryset(self):
    #     query = self.request.GET.get('q')
    #     object_list = City.objects.filter(
    #         Q(name__icontains=query) | Q(state__icontains=query)
    #     )
    #     return object_list

    context_object_name = "coupons"
