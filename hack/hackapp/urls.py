from django.contrib import admin
from django.urls import path
from hackapp.views import LandingPageView, LoginPageView


urlpatterns = [
    path('', LandingPageView.as_view(), name="landing"),
    path('login/', LoginPageView.as_view(), name="login"),
]
