from django.urls import path
from .views import MensualidadListView, MensualidadDetailView, MensualidadCreateView, MensualidadUpdateView, MensualidadDeleteView
urlpatterns = [

path("", MensualidadListView.as_view(), name="mensualidad-list"),
path("mensualidad/<int:pk>/", MensualidadDetailView.as_view(), name="mensualidad-detail"),
path("mensualidad/create/", MensualidadCreateView.as_view(), name="mensualidad-create"),
path("mensualidad/<int:pk>/update/", MensualidadUpdateView.as_view(), name="mensualidad-update"),
path("mensualidad/<int:pk>/delete/", MensualidadDeleteView.as_view(), name="mensualidad-delete"),
]
