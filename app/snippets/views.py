from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

import snippets
from .models import Snippet
from .serializers import SnippetSerializer


class JsonResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super().__init__(content, **kwargs)


@csrf_exempt
def snippet_list(request):
    data = JSONParser().parse(request)
    serializer = SnippetSerializer(data=data)
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return JsonResponse(serializer.data)
    elif request.method == 'POST':
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
