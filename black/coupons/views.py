from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
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


def coupon_list_json(request):
    ctx = {}
    user_input = request.GET.get("inputValue")
    user_input = user_input if user_input else ""
    page = request.GET.get("page", 1)
    query_result = Coupon.objects.filter(
        Q(title__icontains=user_input), end_time__gte=now()
    ).order_by("-start_time")
    paginator = Paginator(query_result, 3)
    query_result = paginator.page(page)
    ctx["coupons"] = query_result
    ctx["top_offers"] = Coupon.objects.filter(Q(top_offer=True))
    ctx["number_of_pages"] = paginator.num_pages
    ctx["page_number"] = query_result.number
    ctx["has_next"] = query_result.has_next()
    ctx["has_previous"] = query_result.has_previous()
    if request.is_ajax():
        html = render_to_string(
            template_name="coupons/coupons_search_results.html", context=ctx
        )
        data_dict = {"html_from_view": html}
        return JsonResponse(data=data_dict, safe=False)

    # data_serialized = serializers.serialize('python', query_result)
    # data = json.dumps([d['fields'] for d in data_serialized], cls=DjangoJSONEncoder)
    return render(request, "pages/home.html", context=ctx)
