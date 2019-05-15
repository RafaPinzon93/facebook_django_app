from django.contrib.auth import logout
from django.http import Http404
from django.shortcuts import redirect
from django.views import View

from allauth.socialaccount.models import SocialAccount

from .utils import parse_facebook_signed_request


def logout_view(request):
    logout(request)
    return redirect('index')


class DeauthorizeView(View):
    def post(self, request):
        signed_request = parse_facebook_signed_request(request.body)
        try:
            social_account = SocialAccount.objects.get(
                uid=signed_request['user_id'])
        except SocialAccount.DoesNotExist:
            raise Http404("User does not exists")
        user = social_account.user
        user.is_active = False
        user.save()
