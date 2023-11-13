from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.urls import reverse_lazy




class CustomLoginView(LoginView):
    template_name = "custom_login.html"
    
    
    def form_invalid(self, form):
        messages.error(
            self.request, "Credenciales incorrectas. Por favor, inténtalo de nuevo."
        )  
        return super().form_invalid(form)


class CustomLogoutView(LogoutView):
    success_url = reverse_lazy("custom_login.html")

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, '¡Te has desconectado exitosamente!')
        return super().dispatch(request, *args, **kwargs)