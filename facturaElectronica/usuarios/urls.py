from django.urls import path
from . import views

urlpatterns = [
    path('administracion', views.IndexView.as_view(), name='panel_administrativo'),
    path('usuarios/parametosHacienda', views.ParametrosHaciendaDetailView.as_view(), name='verParametrosHacienda'),
    path('usuarios/parametosHaciendaCreate', views.ParametrosAuthHaciendaCreateView.as_view(), name='createParametrosHacienda'),
    path('usuarios/parametosHaciendaUpdate/<int:pk>', views.ParametrosAuthHaciendaUpdateView.as_view(), name='updateParametrosHacienda'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('register/system-admin/', views.SystemAdminRegistrationView.as_view(), name='register_system_admin'),
    path('register/entity-admin/', views.EntityAdminRegistrationView.as_view(), name='register_entity_admin'),
    path('usuarios', views.UserListView.as_view(), name='index_user'),
    path('usuarios/create', views.UserCreateView.as_view(), name='create_user'),
    path('usuarios/update/<int:pk>', views.UserUpdateView.as_view(), name='edit_user'),
    path('usuarios/delete/<int:pk>', views.UserDeleteView.as_view(), name='delete_user'), 
    path('usuarios/ver)<int:pk>', views.UserDetailView.as_view(), name='verUsuario'),
    path('usuarios/actividadEconomicaCreate', views.ActividadEconomicaCreateView.as_view(), name='actividadEconomicaCreate'),
    path('usuarios/actividadEconomicaUpdate/<int:pk>', views.ActividadEconomicaUpdateView.as_view(), name='actividadEconomicaUpdate'),
    path('usuarios/entidad/ver', views.EntidadDetailView.as_view(), name='verEntidad'),
    path('usuarios/entidadCreate', views.EntidadCreateView.as_view(), name='entidadCreate'),
    path('usuarios/entidadUpdate/<int:pk>', views.EntidadUpdateView.as_view(), name='entidadUpdate'),

]


  