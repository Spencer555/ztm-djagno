from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth import logout
from django.shortcuts import render

class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class MyLogoutView(TemplateView):
    template_name = 'registration/logout.html'
    
    def get(self, request):
        logout(request)
        return render(request, self.template_name)
    
    
    
class MyLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = '/'
