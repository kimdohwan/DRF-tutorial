from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from ..views import generic_cbv

urlpatterns = [
    path('users/', generic_cbv.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', generic_cbv.UserDetail.as_view(), name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
