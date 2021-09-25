from django.conf.urls import url
from django.urls import path

from .views import CouponDetail, coupon_list_json

urlpatterns = [
    path("<int:pk>", CouponDetail.as_view()),
    url("search", coupon_list_json),
]
