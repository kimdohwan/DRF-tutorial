from django.urls import path

from ..views import django_view

urlpatterns = [
    path('snippets/', django_view.snippet_list, name='snippet-list'),
    path('snippets/<int:pk>/', django_view.snippet_detail, name='snippet-detail'),
]