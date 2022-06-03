from django.urls import path
from user.views import SignUpCreateView, ProfileTemplateView

app_name = 'user'

urlpatterns = [
    path('signup/', SignUpCreateView.as_view(), name='signup'),
    path('profile/', ProfileTemplateView.as_view(), name='profile'),
]
