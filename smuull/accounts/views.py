from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, UpdateUserForm, UpdateProfileForm


def register(request:HttpResponse, template_name:str = "accounts/register.html"):
    # ToDo : This view needs attention.
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


@login_required
def profile_index(request:HttpResponse, template_name:str = "accounts/profile_index.html"):

    if request.method == "POST":
        user_form = UpdateUserForm(instance = request.user, data = request.POST)
        profile_form = UpdateProfileForm(instance = request.user.profile, data = request.POST, files = request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,"Profile updated!")
            return redirect("accounts:accounts-profile")
        else:
            messages.error(request,"Error updating your profile")
            return redirect("accounts:accounts-profile")
        
    user_form = UpdateUserForm(instance = request.user)
    profile_form = UpdateProfileForm(instance = request.user.profile)
    
    template_data:dict = {
        "user_form":user_form,
        "profile_form":profile_form
    }
    
    return TemplateResponse(request, template_name,template_data)