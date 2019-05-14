from django.urls import path
from django.views.generic import TemplateView

from .views import logout_view, deauthorize_view


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('logout/', logout_view, name='logout'),
    path('facebook/deauthorize/', DeauthorizeView.as_view()),
]
