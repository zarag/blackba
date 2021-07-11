from coupons.models import Coupon
from django import forms
from django.core.mail import BadHeaderError, send_mail
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.timezone import now
from django.views import generic


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.CharField(max_length=150)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)


class HomeView(generic.ListView):
    template_name = "pages/home.html"

    def get_queryset(self, **kwargs):
        context = {}
        context["top_offers"] = Coupon.objects.filter(Q(top_offer=True))
        query = self.request.GET.get("q")
        search_term = query if query else ""
        context["search_results"] = Coupon.objects.filter(
            Q(title__icontains=search_term), end_time__gte=now()
        ).order_by("-start_time")
        return context

    context_object_name = "coupons"


def contact(self):
    if self.method == "POST":
        form = ContactForm(self.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                "name": form.cleaned_data["name"],
                "email": form.cleaned_data["email"],
                "message": form.cleaned_data["message"],
            }
            message = "\n".join(body.values())

            try:
                send_mail(
                    subject,
                    message,
                    form.cleaned_data["email"],
                    ["rezervacija@black.ba"],
                )
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return render(self, "pages/contact.html", {"form": form})

    form = ContactForm()
    return render(self, "pages/contact.html", {"form": form})
