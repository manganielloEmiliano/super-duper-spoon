from django.urls import path
from apps.mesa.views import MesaListView, MesaDetailView
urlpatterns = [
    path('', MesaListView.as_view(), name='mesa_list'),
    path('<int:pk>/', MesaDetailView.as_view(), name='mesa_detail'),    
]
