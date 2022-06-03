from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from user.forms import SignUpForm


class SignUpCreateView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class ProfileTemplateView(TemplateView):
    template_name = 'registration/profile.html'
