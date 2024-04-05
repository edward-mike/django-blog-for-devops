from  django.conf import settings
from .models import Post

def site_informations(request):
	""" Context processor for site - name and domain. """
 
	qs = Post.objects.all().order_by('-viewers')[:3]
 
	context_data:dict = {
	"PROJECT_NAME":settings.PROJECT_NAME,
	"trending_posts": qs
	}
	return context_data