from django.urls import path
from django.conf.urls.static import static
from facturacion.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='panel_facturas'),
    
    path('pais', PaisView.as_view(), name='index_pais'),
    path('paisCreate', PaisCreateView.as_view(), name='paisCreate'),
    path('paisUpdate/<int:pk>', PaisUpdateView.as_view(), name='paisUpdate'),
    
    path('departamento', DepartamentoView.as_view(), name='index_departamento'),
    path('departamentoCreate', DepartamentoCreateView.as_view(), name='departamentoCreate'),
    path('departamentoUpdate/<int:pk>', DepartamentoUpdateView.as_view(), name='departamentoUpdate'),
    
    path('municipio', MunicipioView.as_view(), name='index_municipio'),
    path('municipioCreate', MunicipioCreateView.as_view(), name='municipioCreate'),
    path('municipioUpdate/<int:pk>', MunicipioUpdateView.as_view(), name='municipioUpdate'),
    
    path('direccion', DireccionView.as_view(), name='index_direccion'),
    path('direccionCreate', DireccionCreateView.as_view(), name='direccionCreate'),
    path('direccionUpdate/<int:pk>', DireccionUpdateView.as_view(), name='direccionUpdate'),
    
    path('factura/unidadMedida', UnidadMedidaView.as_view(), name='index_unidadMedida'),
    path('factura/unidadMedidaCreate', UnidadMedidaCreateView.as_view(), name='unidadMedidaCreate'),
    path('factura/unidadMedidaUpdate/<int:pk>', UnidadMedidaUpdateView.as_view(), name='unidadMedidaUpdate'),
    
    path('facturaSujetoExcluido/operacionSujetoExcluido', OperacionSujetoExcluidoView.as_view(), name='index_operacionSujetoExcluido'),
    path('facturaSujetoExcluido/operacionSujetoExcluidoCreate', OperacionSujetoExcluidoCreateView.as_view(), name='operacionSujetoExcluidoCreate'),
    path('facturaSujetoExcluido/operacionSujetoExcluidoUpdate/<int:pk>', OperacionSujetoExcluidoUpdateView.as_view(), name='operacionSujetoExcluidoUpdate'),
    
    path('facturaSujetoExcluido/sujetoExcluidoMonth/<int:year>/<int:month>', SujetoExcluidoMonthView.as_view(), name='sujetoExcluidoMonth'),
    path('facturaSujetoExcluido/sujetoExcluidoVer/<int:pk>', SujetoExcluidoDetailView.as_view(), name='sujetoExcluidoDetailView'),
      
    
]
