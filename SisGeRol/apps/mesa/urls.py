from django.urls import path
from apps.mesa.views import MesaCreateView, MesaDeleteView, MesaListView, MesaDetailView, MesaUpdateView
urlpatterns = [
    path('', MesaListView.as_view(), name='mesa_list'),
    path('<int:pk>/', MesaDetailView.as_view(), name='mesa_detail'),
    path('create/', MesaCreateView.as_view(), name='mesa_create'),
    path('delete/<int:pk>/', MesaDeleteView.as_view(), name='mesa-delete'),
    path('update/<int:pk>/', MesaUpdateView.as_view(), name='mesa-update'),
    
]
