from django.contrib.auth import get_user_model
from rest_framework import generics, permissions


from utils.pagenations import SnippetListPagination
from ..models import Snippet
from ..serializers import SnippetListSerializer, UserListSerializer

User = get_user_model()
__all__ = (
    'SnippetList',
    'SnippetDetail',
    'UserList',
    'UserDetail',
)


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetListSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
    pagination_class = SnippetListPagination

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetListSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        # IsOwnerOrReadOnly,
    )


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
