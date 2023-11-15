from django.urls import path
from .views import SocioCreateView, SocioDeleteView, SocioListView, SocioUpdateView, SocioView

urlpatterns = [
    path('', SocioListView.as_view(), name='socio-list'),
    path('<int:pk>/', SocioView.as_view(), name='socio-detail'),
    path('create/', SocioCreateView.as_view(), name='socio-create'),
    path('delete/<int:pk>/', SocioDeleteView.as_view(), name='socio-delete'),
    path('update/<int:pk>/', SocioUpdateView.as_view(), name='socio-update'),
]