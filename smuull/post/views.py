from django.template.response import TemplateResponse
from django.http import HttpResponse


fake_data = [
    {
        "title": "Post 1",
        "author": "Edward Mike",
        "content": "Hey there!",
    },
    {
        "title": "Post 2",
        "author": "Areilla Mike",
        "content": "Hi there!",
    },
]

# Create your views here.
def index(request:HttpResponse, template_name:str = "post/index.html"):
    template_data: dict = {"title":"index title","fake_data":fake_data}
    return TemplateResponse(request, template_name, template_data)


def about(request:HttpResponse, template_name:str = "post/about.html"):
    template_data: dict = {"title":"about title"}
    return TemplateResponse(request, template_name, template_data)