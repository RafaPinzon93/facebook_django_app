from django.contrib.auth import logout
from django.http import Http404, HttpResponse
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from allauth.socialaccount.models import SocialAccount

from .utils import parse_facebook_signed_request


def logout_view(request):
    logout(request)
    return redirect('index')


@method_decorator(csrf_exempt, name="dispatch")
class DeauthorizeView(View):

    def post(self, request):
        signed_request = parse_facebook_signed_request(
            request.POST.get('signed_request'))
        try:
            social_account = SocialAccount.objects.get(
                uid=signed_request['user_id'])
        except SocialAccount.DoesNotExist:
            raise Http404("User does not exists")
        user = social_account.user
        user.is_active = False
        user.save()
        return HttpResponse(status=204)
