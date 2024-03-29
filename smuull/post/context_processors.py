from  django.conf import settings

def site_informations(request):
	""" Context processor for site - name and domain. """
	context_data:dict = {
	"PROJECT_NAME":settings.PROJECT_NAME,
	}
	return context_data