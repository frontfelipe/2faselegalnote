import json
from django.shortcuts import render, render_to_response
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from teste.models import Processos
from teste.serializers import ProcessoSerializer


def inicio(request):    
    return render_to_response('home.html',RequestContext(request))


##### API #####
@api_view(['GET', 'POST'])
def processo_list(request, format=None):
    """
    Retorna os processos
    """
    if request.method == 'GET':
        pro = Processos.objects.all()
        serializer = ProcessoSerializer(pro, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProcessoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE']) 
def processo_detalhe(request, id, format=None): 

    try: 
        pro = Processos.objects.get(pk=id) 
    except Processos.DoesNotExist: 
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProcessoSerializer(pro)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProcessoSerializer(pro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        pro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)