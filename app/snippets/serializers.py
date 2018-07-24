from django.contrib.auth import get_user_model
from django.forms import widgets
from rest_framework import serializers

from .models import LANGUAGE_CHOICES, STYLE_CHOICES, Snippet

User = get_user_model()

__all__ = (
    'UserSerializer',
    'SnippetSerializer',
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'username',
            'snippets',
        )


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = (
            'id',
            'title',
            'code',
            'linenos',
            'language',
            'style',
        )
