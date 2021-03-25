from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView

User = get_user_model()


class DateInput(forms.DateInput):
    is_localized = True
    input_type = "date"


class UserDetailView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = User
    fields = [
        "name",
        "gender",
        "phone",
    ]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        return reverse("users:update")

    def get_object(self):
        return self.request.user

    # def get_form(self):
    #     form = super().get_form()
    #     # form.widgets = {
    #     #     'birthday': forms.SelectDateWidget()
    #     # }
    #     form.fields["birthday"].localize = True
    #     form.base_fields["birthday"].localize = True
    #     form.fields["birthday"].widget = forms.DateInput(attrs={'placeholder': 'Initial date...', 'type': 'text',
    #                'onfocus': "(this.type='date')", "format": "'%d %B, %Y',"}, format='%d-%m-%Y')
    #     form.fields["birthday"].widget.is_localized = True
    #     return form


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("users:update", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()
