from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View,CreateView
from django.views.generic.edit import FormView

#
from .forms import LoginForm, UserRegisterForm # UpdatePasswordForm,)
from .models import User

def home(request):
    return render(request, 'home.html', {})

def profile(request):
    return render(request, 'profile.html', {})


class UserRegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        #
        User.objects.create_user(
            form.cleaned_data['email'],
            form.cleaned_data['first_name'],
            form.cleaned_data['last_name'],
            form.cleaned_data['password1'],
        )
        return super(UserRegisterView, self).form_valid(form)


def login_view(request):

    form = LoginForm(request.POST or None)

    if form.is_valid():
        email=form.cleaned_data.get('email')
        password=form.cleaned_data.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)

            if user.is_active and user.is_superuser:
                return HttpResponseRedirect(reverse_lazy('admin:index'))
            elif user.is_active:      
                return HttpResponseRedirect(reverse_lazy('users:home'))
    
    return render(request, 'users/login.html', {'form': form})


class LogoutView(View, LoginRequiredMixin):
    def get(self, request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect( 
            reverse(
                'users:home'
            )
        )
