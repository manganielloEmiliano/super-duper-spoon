from django.urls import path
from .views import SocioListView, SocioView

urlpatterns = [
    path('', SocioListView.as_view(), name='socio-list'),
    path('socio/<int:pk>/', SocioView.as_view(), name='socio-detail'),
]