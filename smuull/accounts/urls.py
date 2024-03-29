from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/',views.register,name="accounts-register"),
    path('logout-redirect/',views.logout_redirect,name="accounts-logout-redirect"),
    path('logout/',views.logout,name="accounts-logout"),
    
    
]