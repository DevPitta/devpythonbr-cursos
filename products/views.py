from django.views.generic import ListView, DetailView
from products.models import Plan, Course, Formation


class PlansListView(ListView):
    model = Plan
    template_name = 'products/plans_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plans'] = Plan.objects.all()
        return context


class CoursesListView(ListView):
    model = Course
    template_name = 'products/courses_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        return context


class CourseDetailView(DetailView):
    model = Course
    template_name = 'products/course_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course'] = Course.objects.all()
        return context


class FormationsListView(ListView):
    model = Formation
    template_name = 'products/formations_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formations'] = Formation.objects.all()
        return context


class FormationDetailView(DetailView):
    model = Formation
    template_name = 'products/formation_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formation'] = Formation.objects.all()
        return context
