from django.dispatch import receiver, Signal
from django.db.models import F

post_is_viewed = Signal()


@receiver(post_is_viewed)
def post_is_viewed_reciever(sender,**kwargs):
    # print("Signals ",kwargs)
    post = kwargs.get('post')
    session = "viewed_{}".format(post.id)
    
    if not kwargs.get('request').session.get(session,False):
        post.viewers = F('viewers') + 1
        post.save(update_fields=['viewers'])
        post.refresh_from_db()
        kwargs["request"].session[session] = True   
