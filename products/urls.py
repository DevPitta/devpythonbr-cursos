from django.urls import path
from products.views import FormationsListView, CoursesListView, FormationDetailView, CourseDetailView

app_name = 'products'

urlpatterns = [
    path('formations/', FormationsListView.as_view(), name='formations-list'),
    path('courses/', CoursesListView.as_view(), name='courses-list'),
    path('formations/<slug:slug>/', FormationDetailView.as_view(), name='formation-detail'),
    path('courses/<slug:slug>/', CourseDetailView.as_view(), name='course-detail'),
]
