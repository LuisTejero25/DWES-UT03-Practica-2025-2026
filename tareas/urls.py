from django.urls import path
from .views import DetalleTareaView

urlpatterns = [
    path('tarea/<uuid:pk>/', DetalleTareaView.as_view(), name='detalle_tarea'),
]
