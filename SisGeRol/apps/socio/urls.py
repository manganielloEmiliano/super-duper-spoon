from django.urls import path
from apps.socio.views import SocioView

urlpatterns = [
    path("detalle/<int:pk>/", SocioView.as_view(), name="detalle_socio"),
]