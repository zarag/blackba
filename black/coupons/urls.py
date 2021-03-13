from django.urls import path

from .views import CouponDetail

urlpatterns = [
    path("<int:pk>", CouponDetail.as_view()),
]
