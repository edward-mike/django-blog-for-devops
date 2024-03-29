from django.template.response import TemplateResponse
from django.http import HttpResponse
from .models import Post


# Create your views here.
def index(request:HttpResponse, template_name:str = "post/index.html"):
    
    post_qs = Post.objects.all()
    
    template_data: dict = {"title":"index title","posts":post_qs}
    return TemplateResponse(request, template_name, template_data)


def about(request:HttpResponse, template_name:str = "post/about.html"):
    template_data: dict = {"title":"about title"}
    return TemplateResponse(request, template_name, template_data)