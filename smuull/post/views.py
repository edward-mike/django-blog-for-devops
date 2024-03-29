from django.template.response import TemplateResponse
from django.http import HttpResponse


# Create your views here.
def index(request:HttpResponse, template:str = "index.html"):
    template_data: dict = {}
    return TemplateResponse(request, template, template_data)
