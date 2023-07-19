from django.shortcuts import render
from django.views import View

# Create your views here.


class LandingPageView(View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = "landing.html"
        self.args = {

        }
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, self.args)
