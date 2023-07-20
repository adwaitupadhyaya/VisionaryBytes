from django.contrib import admin
from django.urls import path
from hackapp.views import LandingPageView, LoginPageView, HomePageView, LogoutView, ClientView, ServiceProviderView, ServicesView, DashboardView, ServiceProviderListView

urlpatterns = [
    path('', LandingPageView.as_view(), name="landing"),
    path('login/', LoginPageView.as_view(), name="login"),
        path('logout/', LogoutView.as_view(), name="logout"),
    path('home/', HomePageView.as_view(), name = 'home'),
    path('client/', ClientView.as_view(), name = 'client'),
    path('service-provider/', ServiceProviderView.as_view(), name = 'service-provider'),
    path('services/', ServicesView.as_view(), name = 'services'),
    path('dashboard/', DashboardView.as_view(), name = 'dashboard'),
    path('details/<int:pk>/', ServiceProviderListView.as_view(), name = 'details'),
]
