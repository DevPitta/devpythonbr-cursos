from django.urls import path
from products.views import FormationsTemplateView, CoursesTemplateView


urlpatterns = [
    path('formations/', FormationsTemplateView.as_view(), name='formations'),
    path('courses/', CoursesTemplateView.as_view(), name='courses'),
]
