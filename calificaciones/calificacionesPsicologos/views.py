from .logic import calificacionespsicologos_logic as cl
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def psicologo_view(request,id):
    if request.method == 'GET':
        psicologo_dto = cl.get_psicologo(id)
        psicologo = serializers.serialize('json',[psicologo_dto,])
        return HttpResponse(psicologo, 'application/json')

    
@csrf_exempt
def psicologo_view_noid(request):
    if request.method == 'POST':
        psicologo_dto = cl.create_psicologo(json.loads(request.body))
        psicologo = serializers.serialize('json', [psicologo_dto,])
        return HttpResponse(psicologo, 'application/json')

@csrf_exempt
def calificacion_view(request,id_psicologo):
    if request.method == 'POST':
        calificacion_dto = cl.create_calificacion(json.loads(request.body),id_psicologo)
        calificacion = serializers.serialize('json', [calificacion_dto,])
        return HttpResponse(calificacion, 'application/json')

@csrf_exempt
def calificacion_viewnn(request,id_psicologo):
    if request.method == 'POST':
        calificacion_dto = cl.create_calificacion(json.loads(request.body),id_psicologo)
        calificacion = serializers.serialize('json', [calificacion_dto,])
        return HttpResponse(calificacion, 'application/json')

@csrf_exempt
def calificacion_viewass(request,id_psicologo):
    if request.method == 'POST':
        calificacion_dto = cl.create_calificacion(json.loads(request.body),id_psicologo)
        calificacion = serializers.serialize('json', [calificacion_dto,])
        return HttpResponse(calificacion, 'application/json')

@csrf_exempt
def calificacion_viewsonar(request,id_psicologo):
    if request.method == 'POST':
        calificacion_dto = cl.create_calificacion(json.loads(request.body),id_psicologo)
        calificacion = serializers.serialize('json', [calificacion_dto,])
        return HttpResponse(calificacion, 'application/json')


@csrf_exempt
def calificacion_viewpeo(request,id_psicologo):
    if request.method == 'POST':
        calificacion_dto = cl.create_calificacion(json.loads(request.body),id_psicologo)
        calificacion = serializers.serialize('json', [calificacion_dto,])
        return HttpResponse(calificacion, 'application/json')
    

@csrf_exempt
def calificacion_viewss(request,id_psicologo):
    if request.method == 'POST':
        calificacion_dto = cl.create_calificacion(json.loads(request.body),id_psicologo)
        calificacion = serializers.serialize('json', [calificacion_dto,])
        return HttpResponse(calificacion, 'application/json')


@csrf_exempt
def calificacion_vie(request,id_psicologo):
    if request.method == 'POST':
        calificacion_dto = cl.create_calificacion(json.loads(request.body),id_psicologo)
        calificacion = serializers.serialize('json', [calificacion_dto,])
        return HttpResponse(calificacion, 'application/json')


@csrf_exempt
def calificacion_viewport(request,id_psicologo):
    if request.method == 'POST':
        calificacion_dto = cl.create_calificacion(json.loads(request.body),id_psicologo)
        calificacion = serializers.serialize('json', [calificacion_dto,])
        return HttpResponse(calificacion, 'application/json')


@csrf_exempt
def calificacion_viewred(request,id_psicologo):
    if request.method == 'POST':
        calificacion_dto = cl.create_calificacion(json.loads(request.body),id_psicologo)
        calificacion = serializers.serialize('json', [calificacion_dto,])
        return HttpResponse(calificacion, 'application/json')
    
@csrf_exempt
def cal(request,id_psicologo):
    if request.method == 'POST':
        calificacion_dto = cl.create_calificacion(json.loads(request.body),id_psicologo)
        calificacion = serializers.serialize('json', [calificacion_dto,])
        return HttpResponse(calificacion, 'application/json')


@csrf_exempt
def ql(request,id_psicologo):
    if request.method == 'POST':
        calificacion_dto = cl.create_calificacion(json.loads(request.body),id_psicologo)
        calificacion = serializers.serialize('json', [calificacion_dto,])
        return HttpResponse(calificacion, 'application/json')

@csrf_exempt
def cafo(request,id_psicologo):
    if request.method == 'POST':
        calificacion_dto = cl.create_calificacion(json.loads(request.body),id_psicologo)
        calificacion = serializers.serialize('json', [calificacion_dto,])
        return HttpResponse(calificacion, 'application/json')
    
@csrf_exempt
def lol(request,id_psicologo):
    if request.method == 'POST':
        calificacion_dto = cl.create_calificacion(json.loads(request.body),id_psicologo)
        calificacion = serializers.serialize('json', [calificacion_dto,])
        return HttpResponse(calificacion, 'application/json')

@csrf_exempt
def nota(request,id_psicologo):
    if request.method == 'POST':
        calificacion_dto = cl.create_calificacion(json.loads(request.body),id_psicologo)
        calificacion = serializers.serialize('json', [calificacion_dto,])
        return HttpResponse(calificacion, 'application/json')

@csrf_exempt
def otra(request,id_psicologo):
    if request.method == 'POST':
        calificacion_dto = cl.create_calificacion(json.loads(request.body),id_psicologo)
        calificacion = serializers.serialize('json', [calificacion_dto,])
        return HttpResponse(calificacion, 'application/json')

@csrf_exempt
def bb(request,id_psicologo):
    if request.method == 'POST':
        calificacion_dto = cl.create_calificacion(json.loads(request.body),id_psicologo)
        calificacion = serializers.serialize('json', [calificacion_dto,])
        return HttpResponse(calificacion, 'application/json')

@csrf_exempt
def cali(request,id_psicologo):
    if request.method == 'POST':
        calificacion_dto = cl.create_calificacion(json.loads(request.body),id_psicologo)
        calificacion = serializers.serialize('json', [calificacion_dto,])
        return HttpResponse(calificacion, 'application/json')

@csrf_exempt
def calidad(request,id_psicologo):
    if request.method == 'POST':
        calificacion_dto = cl.create_calificacion(json.loads(request.body),id_psicologo)
        calificacion = serializers.serialize('json', [calificacion_dto,])
        return HttpResponse(calificacion, 'application/json')