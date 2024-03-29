from django.template.response import TemplateResponse
from django.http import HttpResponse


# Create your views here.
def register(request:HttpResponse, template_name:str = "accounts/register.html"):
    
    template_data: dict = {"title":"register"}
    return TemplateResponse(request, template_name, template_data)