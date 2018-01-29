from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.response import TemplateResponse
from django.views.generic.base import TemplateView
from rest_framework import generics
from .models import HttpEndpoint
from .serializers import HttpEndpointSerializer
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from .scoring_controller import test_and_score_endpoint
import json

def index(request): 
    return render(request, 'hunter.html', {})


    
@api_view(["GET","POST"])
def httpEndPoint_details(request):
    
    if request.method == 'GET':
        httpendpoint = HttpEndpoint(endpoint_url='github.com')
        #httpendpoint.set_tls_one_one_enbled(False)
        #httpendpoint.set_tls_one_zer0_supported_cipher_list({"ham" : "yes", "egg" : "yes", "spam" : "no"})
        
        httpendpoint = test_and_score_endpoint(httpendpoint)
        serializer = HttpEndpointSerializer(httpendpoint)
        return Response(serializer.data)
    elif request.method == 'POST':
        print('Reached POST')
        if request.is_ajax():
            print("Yes, AJAX!")
        else:
            print("Not Ajax")
            
        body_unicode = request.body.decode('utf-8')
        
        print(body_unicode)
        httpendpoint = HttpEndpoint(endpoint_url=body_unicode)
        #httpendpoint.set_tls_one_one_enbled(False)
        #httpendpoint.set_tls_one_zer0_supported_cipher_list({"ham" : "yes", "egg" : "yes", "spam" : "no"})
        httpendpoint = test_and_score_endpoint(httpendpoint)
        serializer = HttpEndpointSerializer(httpendpoint)
        return Response(serializer.data)
    else:
        raise ValueError('Incorrect Response')