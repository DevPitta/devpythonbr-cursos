from django.views.generic import ListView
from products.models import Course, Formation


class CoursesListView(ListView):
    model = Course
    template_name = 'products/courses_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        return context


class FormationsListView(ListView):
    model = Formation
    template_name = 'products/formations_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formations'] = Formation.objects.all()
        return context
