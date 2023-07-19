from django.contrib import admin
from django.urls import path
from hackapp.views import LandingPageView


urlpatterns = [
    path('', LandingPageView.as_view(), name="landing"),
]
