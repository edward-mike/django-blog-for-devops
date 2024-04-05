from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Post
from .signals import post_is_viewed


# Create your views here.
def index(request:HttpResponse, template_name:str = "post/index.html"):
    
    post_qs = Post.objects.all()
    
    template_data: dict = {"title":"index title","posts":post_qs}
    return TemplateResponse(request, template_name, template_data)


def post_detail(request:HttpResponse, template_name:str = "post/detail.html", *args,**kwargs):
    
    post = get_object_or_404(Post, pk = int(kwargs.pop("post_id")))
    
    post_is_viewed.send(sender = None, post = post, request = request)
    
    template_data = {
        "post": post
    }
    return TemplateResponse(request, template_name, template_data)