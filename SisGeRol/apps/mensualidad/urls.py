from django.urls import path
from .views import MensualidadDeleteView, MensualidadListView, MensualidadCreateView, MensualidadUpdateView, mensualidadDetailView
urlpatterns = [

path("", MensualidadListView.as_view(), name="mensualidad-list"),
path("detail/<int:pk>/", mensualidadDetailView.as_view(), name="mensualidad-detail"),
path("create/", MensualidadCreateView.as_view(), name="mensualidad-create"),
path("delete/<int:pk>/", MensualidadDeleteView.as_view(), name="mensualidad-delete"),
path("update/<int:pk>/", MensualidadUpdateView.as_view(), name="mensualidad-update"),

]
