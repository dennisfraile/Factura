from django.urls import path
from usuarios.views import *

urlpatterns = [
    path('usuarios/parametosHacienda/<int:pk>', ParametrosHaciendaDetailView.as_view(), name='verParametrosHacienda'),
    path('usuarios/parametosHaciendaCreate', ParametrosAuthHaciendaCreateView.as_view(), name='createParametrosHacienda'),
    path('usuarios/parametosHaciendaUpdate/<int:pk>', ParametrosAuthHaciendaUpdateView.as_view(), name='updateParametrosHacienda'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('usuarios', UserListView.as_view(), name='index_user'),
    path('add-user/', redirect_to_add_user, name='add_user_redirect'),
    path('usuarios/update/<int:pk>', ParametrosHaciendaDetailView.as_view(), name='userUpdate'),
    path('usuarios/actividadEconomicaCreate', ActividadEconomicaCreateView.as_view(), name='actividadEconomicaCreate'),
    path('usuarios/actividadEconomicaUpdate/<int:pk>', ActividadEconomicaUpdateView.as_view(), name='actividadEconomicaUpdate'),
    path('usuarios/entidadCreate', EntidadCreateView.as_view(), name='entidadCreate'),
    path('usuarios/entidadUpdate', EntidadUpdateView.as_view(), name='entidadUpdate'),

]


  