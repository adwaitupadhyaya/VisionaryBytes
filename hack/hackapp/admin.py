from django.contrib import admin

from .models import UserType, ServiceProviderModel, ClientRequestsModel

admin.site.register(UserType)
admin.site.register(ServiceProviderModel)
admin.site.register(ClientRequestsModel)

