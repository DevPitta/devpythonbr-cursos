from django.views.generic import TemplateView


class AboutTemplateView(TemplateView):
    template_name = 'about/about.html'
