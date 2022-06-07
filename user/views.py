from poplib import CR
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from user.forms import SignUpForm


class SignUpCreateView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('account_login')
    template_name = 'account/signup.html'


class ProfileTemplateView(TemplateView):
    template_name = 'account/profile.html'