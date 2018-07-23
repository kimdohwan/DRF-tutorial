from django.urls import include, path

from . import django_view, api_view

app_name = 'snippets'
urlpatterns = [
    path('django_view/', include(django_view)),
    path('api_view/', include(api_view)),
]
