from django.urls import path

from authapp.views import RegisterView

app_name = 'authapp'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
]
