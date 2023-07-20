from django.contrib import admin

from .models import UserType, ServiceProviderModel

admin.site.register(UserType)
admin.site.register(ServiceProviderModel)

