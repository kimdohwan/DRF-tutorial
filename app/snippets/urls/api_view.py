from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from ..views import api_view

urlpatterns = [
    path('snippets/', api_view.SnippetList.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/', api_view.SnippetDetail.as_view(), name='snippet-detail'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
