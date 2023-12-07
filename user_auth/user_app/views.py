from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import SignupForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required


class SignupView(CreateView):
    form_class = SignupForm
    template_name = 'signup.html'


    def get_success_url(self):
        login(self.request, self.object)
        return '/' 
    
    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
    
   
    
class CustomLoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        user = self.request.user
        if user.user_type == 'patient':
            return '/patient-dashboard/'  # Redirect patient to the patient dashboard
        elif user.user_type == 'doctor':
            return '/doctor-dashboard/'  # Redirect doctor to the doctor dashboard
        else:
            return '/'  # Redirect to a default dashboard or homepage
        
@login_required(login_url='login')
def patient_dashboard(request):
    return render(request, 'patient-dashboard.html')

@login_required(login_url='login')
def doctor_dashboard(request):
    return render(request, 'doctor-dashboard.html')
