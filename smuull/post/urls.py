from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('',views.index,name='post-index'),
    path('detail/<int:post_id>/',views.post_detail,name='post-detail'),
]