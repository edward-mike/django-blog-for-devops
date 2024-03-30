import os
from django.db import models
from django.contrib.auth.models import User


def avatar_upload_dir(user,filename):
	filename,ext = os.path.splitext(filename)
	return os.path.join(
		'avatar_images',
		'avatar_{id}_{filename}{ext}'.format(
			id=user.id,filename=filename,ext=ext))
 
 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    image = models.ImageField(upload_to=avatar_upload_dir,verbose_name="profile pic.", blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_at = models.DateTimeField(auto_now=True)
    bio = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username} profile"
    
    def save(self,*args,**kwargs):
        super(self.__class__,self).save(*args,**kwargs)
        
            