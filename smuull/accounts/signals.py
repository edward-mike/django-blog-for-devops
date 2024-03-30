from django.dispatch import receiver
from django.db.models.signals import pre_save

from .models import Profile
from .utils import user_random_avatar

"""
signal to assigns a randomly generated avatar to a new user.
"""
@receiver(pre_save,sender=Profile)
def user_default_avatar_set_reciever(sender,instance,*args,**kwargs):
    if not instance.image:
        instance.image = user_random_avatar()