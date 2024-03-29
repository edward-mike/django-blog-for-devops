from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

class CustomLoginView(LoginView):
    redirect_authenticated_user = True  # Redirect authenticated users

    def dispatch(self, request, *args, **kwargs):
        if self.redirect_authenticated_user and self.request.user.is_authenticated:
            # If user is authenticated, redirect them to a different URL
            return HttpResponseRedirect(reverse_lazy('post:post-index'))  # Change 'home' to your desired URL
        return super().dispatch(request, *args, **kwargs)
