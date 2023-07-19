from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import authenticate, login

from hackapp.forms import SignupForm, LoginForm
from hackapp.models import CustomUser

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

        if form.is_valid():
            form.save()
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
            user = CustomUser.objects.filter(username=username)
            passwordToCheck = CustomUser.objects.filter(
                username=username).values('password')
            if password == passwordToCheck[0]['password']:

                return HttpResponse("logged in")
            else:
                self.args['errors'] = "Invalid Credentials"
                return render(request, self.template_name, self.args)
