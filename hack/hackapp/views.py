from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LogoutView
from .models import UserType

from hackapp.forms import SignupForm, LoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class LandingPageView(View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = "landing.html"
        self.args = {
            'form': SignupForm()

        }
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, self.args)

    def post(self, request):
        form = SignupForm(request.POST)
        m = form.save(commit = False)
        if form.is_valid():
            m.set_password(form.cleaned_data['password'])
            m.save()
            return redirect('login')
        else:
            print(form.errors)
            return HttpResponse("errors")


class LoginPageView(View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = "login.html"
        self.args = {
            'form': LoginForm()
        }
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, self.args)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(form.cleaned_data)
            user = authenticate(request, username=username, password=password)
            print(user) 
            if user is not None:
                login(request, user)    
                return redirect('home')
            else:
                self.args['errors'] = "Invalid Credentials"
                return render(request, self.template_name, self.args)
        else:
            self.args['error'] = 'Sorry, Unable to process your request'
            return render(request, self.template_name, self.args)
        
class LogoutView(LoginRequiredMixin, View):
    def get(self,request):
        logout(request)
        return redirect('login')

class HomePageView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = 'home.html'
        self.args = {
            "id": request.user.id
        }
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        return render(request, self.template_name, self.args)
    
    def post(Self,request):
        data = request.POST.dict()
        user_type = data['test']
        user = request.user
        user_type_model = UserType(user = user, user_type = user_type)
        user_type_model.save()
        print(user_type_model)

        if user_type_model.user_type == "client":
            return redirect('client')
        else:
            return redirect('service-provider')

class ClientView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = "client.html"
        self.args = {
            
        }
        
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request):
        return render(request, self.template_name, self.args)

    
class ServiceProviderView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = "service-details.html"
        self.args = {

        }
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        return render(request, self.template_name, self.args)
    
