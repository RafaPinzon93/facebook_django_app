from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View


def logout_view(request):
    logout(request)
    return redirect('index')


def DeauthorizeView(View):
    def post(self, request):
        pass
