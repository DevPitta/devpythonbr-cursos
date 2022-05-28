from django.urls import path
from products.views import FormationsListView, CoursesListView

app_name = 'products'

urlpatterns = [
    path('formations/', FormationsListView.as_view(), name='formations'),
    path('courses/', CoursesListView.as_view(), name='courses'),
]
