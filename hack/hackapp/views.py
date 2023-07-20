from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LogoutView
from django.contrib import messages

from .forms import ServiceProviderForm
from .models import ClientRequestsModel, ServiceProviderModel, UserType

from hackapp.forms import SignupForm, LoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from .cv_matcher import comparer

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
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)    
                return redirect('client')
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
            'form':ServiceProviderForm(),
        
            }
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        return render(request, self.template_name, self.args)
    
    def post(self,request):
        form = ServiceProviderForm(request.POST, request.FILES)
        if form.is_valid():
            m = form.save()
            print(m.type_of_service)

            if m.type_of_service == 'electrician':
                vacancy_path = '..'
            if m.type_of_service == 'Plumbing':
                vacancy_path = '../static/vacancies/for plumber.pdf'
            if m.type_of_service == 'Gardening':
                vacancy_path = '../static/vacancies/Gardener.pdf'
            if m.type_of_service == 'Painting':
                vacancy_path = '../static/vacancies/wall painter.pdf'
            if m.type_of_service == 'IT':
                vacancy_path = '../static/vacancies/IT technician.pdf'
            if m.type_of_service == 'Carpentry':
                vacancy_path = '../static/vacancies/elec.pdf'

            cv_path = m.cv.path
            threshold = comparer(cv_path, vacancy_path)
            print(threshold)
            if threshold<0.5:
                self.args['errors'] = "Sorry We couldn't Validate your resume in our system!"
                ServiceProviderModel.objects.filter(id=m.id).delete()
                messages.error(request, "Sorry We couldn't Validate your resume in our system!" )
                return render(request, self.template_name, self.args)
            else:
                self.args['success'] = "Congratulations, You have been registered in our system"
                messages.success(request, "Congratulations, You have been registered in our system")
                return redirect('dashboard')
        else:
            self.args['errors'] = form.errors
            return render(request, self.template_name, self.args)

    

class ServicesView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = 'services.html'
        self.args = {

        }
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
     
        return render(request, self.template_name, self.args)
    
class DashboardView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = "dashboard.html"
        print(request.user)
        self.args ={
            "datas": ClientRequestsModel.objects.filter(technician = request.user)

        }
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        return render(request, self.template_name, self.args)
    

class ServiceProviderListView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = "details.html"

        self.args = {

        }
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        
        id = kwargs.get('pk')
        print(id)

        if (id == 1):
            data = ServiceProviderModel.objects.filter(type_of_service = "Electrician").order_by('-threshold')
        if (id == 2):
            data  = ServiceProviderModel.objects.filter(type_of_service = "IT").order_by('-threshold')
        if (id == 3):
            data = ServiceProviderModel.objects.filter(type_of_service = "Plumbing").order_by('-threshold')
        if (id == 4):
            data  = ServiceProviderModel.objects.filter(type_of_service = "Gardening").order_by('-threshold')
        if (id == 5):
            data = ServiceProviderModel.objects.filter(type_of_service = "Painting").order_by('-threshold')
        if (id == 6):
            data  = ServiceProviderModel.objects.filter(type_of_service = "Carpentry").order_by('-threshold')

        self.args['data'] = data

        return render(request, self.template_name, self.args )
    
    def post(self, request, *args, **kwargs):
        user = request.user
        technician = request.POST.dict()
        print(technician)
        client_request = ClientRequestsModel(user = user, technician = technician['technician'])
        client_request.save()
        messages.success(request, "Your request has been placed")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    