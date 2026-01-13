from django.shortcuts import redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login

class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    

class UserLogoutView(LogoutView):
    next_page = 'accounts:login'

class UserCreationView(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('core:index')

    def form_valid(self, form):
        """ Automatic login """
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)