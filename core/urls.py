from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.formularioPublicacion, name='add_url'),
    path('edit/<int:fP_id>', views.updateView, name= 'update_url'),
    path('delete/<int:fP_id>', views.deleteView, name= 'delete_url'),
]