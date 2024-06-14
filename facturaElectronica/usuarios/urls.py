from django.urls import path
from usuarios.views import *

urlpatterns = [
    path('usuarios/parametosHacienda/<int:pk>', ParametrosHaciendaDetailView.as_view(), name='verParametrosHacienda'),
    path('usuarios/parametosHaciendaCreate', ParametrosAuthHaciendaCreateView.as_view(), name='createParametrosHacienda'),
    path('usuarios/parametosHaciendaUpdate/<int:pk>', ParametrosAuthHaciendaUpdateView.as_view(), name='updateParametrosHacienda'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/system-admin/', SystemAdminRegistrationView.as_view(), name='register_system_admin'),
    path('register/entity-admin/', EntityAdminRegistrationView.as_view(), name='register_entity_admin'),
    path('usuarios', UserListView.as_view(), name='index_user'),
    path('usuarios/create', UserCreateView.as_view(), name='create_user'),
    path('usuarios/update/<int:pk>', UserUpdateView.as_view(), name='edit_user'),
    path('usuarios/delete/<int:pk>', UserDeleteView.as_view(), name='delete_user'), 
    path('usuarios/ver)<int:pk>', UserDetailView, name='verUsuario'),
    path('usuarios/update/<int:pk>', ParametrosHaciendaDetailView.as_view(), name='userUpdate'),
    path('usuarios/actividadEconomicaCreate', ActividadEconomicaCreateView.as_view(), name='actividadEconomicaCreate'),
    path('usuarios/actividadEconomicaUpdate/<int:pk>', ActividadEconomicaUpdateView.as_view(), name='actividadEconomicaUpdate'),
    path('usuarios/entidadCreate', EntidadCreateView.as_view(), name='entidadCreate'),
    path('usuarios/entidadUpdate', EntidadUpdateView.as_view(), name='entidadUpdate'),

]


  