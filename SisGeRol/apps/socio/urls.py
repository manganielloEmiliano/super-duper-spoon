from django.urls import path
from apps.socio.views import SocioView
urlpatterns = [
    path("",SocioView.as_view(), name="index" ),

]
