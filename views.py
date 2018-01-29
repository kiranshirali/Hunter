from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.response import TemplateResponse
from django.views.generic.base import TemplateView

def index(request): 
    return render(request, 'hunter.html', {})
    