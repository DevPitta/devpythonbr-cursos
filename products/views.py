from django.views.generic import TemplateView


class FormationsTemplateView(TemplateView):
    template_name = 'products/formations.html'


class CoursesTemplateView(TemplateView):
    template_name = 'products/courses.html'
