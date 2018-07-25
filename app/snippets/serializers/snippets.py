from rest_framework import serializers

from snippets.models import Snippet
from snippets.serializers.users import UserListSerializer

__all__ = (
    'SnippetListSerializer',
    'SnippetDetailSerializer',
)


class SnippetBaseSerializer(serializers.ModelSerializer):
    owner = UserListSerializer(required=False)

    class Meta:
        model = Snippet
        fields = (
            'pk',
            'title',
            'code',
            'linenos',
            'language',
            'style',
            'owner',
        )
        read_only_fields = (
            'owner',
        )


class SnippetListSerializer(SnippetBaseSerializer):
    pass


class SnippetDetailSerializer(SnippetBaseSerializer):
    class Meta(SnippetBaseSerializer.Meta):
        fields = SnippetBaseSerializer.Meta.fields + ('code',)
