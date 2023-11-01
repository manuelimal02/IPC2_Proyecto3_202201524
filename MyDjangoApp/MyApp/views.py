from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import requests

def myform_view(request):
    return render(request, 'myform.html')

def consulta_hashtag(request):
    try:
        response = requests.get('http://127.0.0.1:5000/consulta/consultarHashtag')
        response.raise_for_status()
        response_data = response.json()
        return JsonResponse(response_data)
    except requests.exceptions.RequestException as e:
        return HttpResponse(str(e), status=500)

def consulta_menciones(request):
    try:
        response = requests.get('http://127.0.0.1:5000/consulta/consultarMenciones')
        response.raise_for_status()
        response_data = response.json()
        return JsonResponse(response_data)
    except requests.exceptions.RequestException as e:
        return HttpResponse(str(e), status=500)

def consulta_sentimiento(request):
    try:
        response = requests.get('http://127.0.0.1:5000/consulta/consultarSentimiento')
        response.raise_for_status()
        response_data = response.json()
        return JsonResponse(response_data)
    except requests.exceptions.RequestException as e:
        return HttpResponse(str(e), status=500)
    
def grafica_hashtag(request):
    try:
        response = requests.get('http://127.0.0.1:5000/grafica/grafica-consulta-hashtag')
        response.raise_for_status()
        response_data = response.json()
        return JsonResponse(response_data)
    except requests.exceptions.RequestException as e:
        return HttpResponse(str(e), status=500)

def grafica_menciones(request):
    try:
        response = requests.get('http://127.0.0.1:5000/grafica/grafica-consulta-menciones')
        response.raise_for_status()
        response_data = response.json()
        return JsonResponse(response_data)
    except requests.exceptions.RequestException as e:
        return HttpResponse(str(e), status=500)

def grafica_sentimiento(request):
    try:
        response = requests.get('http://127.0.0.1:5000/grafica/grafica-consulta-sentimiento')
        response.raise_for_status()
        response_data = response.json()
        return JsonResponse(response_data)
    except requests.exceptions.RequestException as e:
        return HttpResponse(str(e), status=500)