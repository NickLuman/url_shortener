from .models import URL
from .serializers import URLSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.core import validators, exceptions


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_url(request, hash_url):
    """View for processing cutted url"""
    url_object = get_object_or_404(URL, hash_url=hash_url)

    if request.method == 'GET':
        url_object.clicked()
        return HttpResponseRedirect(url_object.base_url)
    elif request.method == 'DELETE':
        url_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = URLSerializer(url_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_post_urls(request):
    """Creation and getting all urls"""
    if request.method == 'GET':
        urls = URL.objects.all()
        serializer = URLSerializer(urls, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {
            'base_url': request.data.get('base_url'),
        }
        validator = validators.URLValidator()

        try:
            validator(data['base_url'])
        except exceptions.ValidationError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = URLSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            url_object = get_object_or_404(URL, base_url=data['base_url'])
            return Response('{0}{1}'.format(request.build_absolute_uri(), url_object.hash_url),
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
