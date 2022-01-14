from django.urls import reverse_lazy
from django.views.generic import CreateView

from authapp.forms import UserRegisterForm


class RegisterView(CreateView):
    """ Страница регистрации """
    form_class = UserRegisterForm
    template_name = 'authapp/register.html'
    extra_context = {'category_page': 'Register'}
    success_url = reverse_lazy('main:index')
