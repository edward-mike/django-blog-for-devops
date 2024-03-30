from django import forms
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.models import User
from .models import Profile


USERNAME_RE = r'^[\.\w]+$'

class RegisterForm(forms.Form):
    username = forms.RegexField(regex=USERNAME_RE,max_length=15,required=True,
        error_messages={"invalid":"Username must contain only letters,numbers,dots and underscores."},
        widget=forms.TextInput(attrs={'autofocus':True,'autocomplete':"off",
        }))

    email = forms.EmailField(label='Email',required=True,disabled=False,
        widget = forms.EmailInput(attrs={'autocomplete':"off",}))

    password1 = forms.CharField(
        label=('Password'), required=True,
        widget=forms.PasswordInput(attrs={'autocomplete': 'off'}),
        help_text=("Enter a strong password"))

    password2 = forms.CharField(
        label=("Password confirmation"), required=True,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=("Enter the same password as above, for verification."))


    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("the two password fields didn\'t match.")
        return self.cleaned_data


    def clean_username(self):
        username = self.cleaned_data.get("username").strip().lower()

        users_qs = User.objects.filter(username__iexact=username)

        if users_qs.exists():
            raise forms.ValidationError(f"user with {username} already exists.")
        return self.cleaned_data.get("username")


    def clean_email(self):
        email = self.cleaned_data.get("email")
        
        try:
            validate_email(email)
        except ValidationError:
            raise forms.ValidationError("invalid email")

        users_qs = User._default_manager.filter(email__iexact=email)

        if users_qs.exists():
            raise forms.ValidationError(f"a user with {email} already exists.")
        return self.cleaned_data.get("email")


    def save(self,force_insert=False,force_update=False,commit=True,**kwargs):
            username = self.cleaned_data['username'].lower()
            email = self.cleaned_data["email"].lower()
            password2 = self.cleaned_data["password2"]
            
            user = None
             
            if commit:
                try:
                    user = User.objects.create_user(username=username,
                                 email=email,
                                 password=password2)
                except IntegrityError:
                    raise ValidationError("User is already registered")
            return user
        

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ["username", "email"]
    
    def __init__(self,*args,**kwargs):
        super(self.__class__, self).__init__(*args,**kwargs)

        
         

class UpdateProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ["bio","image",]

    def __init__(self,*args,**kwargs):
        super(self.__class__, self).__init__(*args,**kwargs)
        

        