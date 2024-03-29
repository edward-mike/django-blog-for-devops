from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm


# Create your views here.
def register(request:HttpResponse, template_name:str = "accounts/register.html"):
    # MEssages require fixing : error and success
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts-login')
        else:
            # print(form.errors.items())
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request,f"Error in {field}: {error}")
            return redirect("accounts:accounts-register")
    else:
        form = RegisterForm()
    
    template_data: dict = {
        "form":form
    }
    return TemplateResponse(request, template_name, template_data)


@login_required
def logout(request:HttpResponse, template_name:str = "accounts/logout.html"):
	auth.logout(request)
	return redirect("accounts:accounts-logout-redirect")

@login_required
def logout_redirect(request:HttpResponse, template_name:str = "accounts/logout.html"):
	return TemplateResponse(request, template_name,{})