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
    
    path('facturaSujetoExcluido/formaPago', FormaPagoView.as_view(), name='index_formaPago'),
    path('facturaSujetoExcluido/formaPagoCreate', FormaPagoCreateView.as_view(), name='formaPagoCreate'),
    path('facturaSujetoExcluido/formaPagoUpdate/<int:pk>', FormaPagoUpdateView.as_view(), name='formaPagoUpdate'),
    
    path('facturaSujetoExcluido/pago', PagoView.as_view(), name='index_pago'),
    path('facturaSujetoExcluido/pagoCreate', PagoCreateView.as_view(), name='PagoCreate'),
    path('facturaSujetoExcluido/pagoUpdate/<int:pk>', PagoUpdateView.as_view(), name='PagoUpdate'),
    
    path('factura/apendice', ApendiceView.as_view(), name='index_apendice'),
    path('factura/apendiceCreate', ApendiceCreateView.as_view(), name='apendiceCreate'),
    path('factura/apendiceUpdate/<int:pk>', ApendiceUpdateView.as_view(), name='apendiceUpdate'),
    
    path('factura/tipoDocumento', TipoDocumentoView.as_view(), name='index_tipoDocumento'),
    path('factura/tipoDocumentoCreate', TipoDocumentoCreateView.as_view(), name='tipoDocumentoCreate'),
    path('factura/tipoDocumentoUpdate/<int:pk>', TipoDocumentoUpdateView.as_view(), name='tipoDocumentoUpdate'),
    
    path('factura/identificador', IdentificadorView.as_view(), name='index_identificador'),
    path('factura/identificadorCreate', IdentificadorCreateView.as_view(), name='identificadorCreate'),
    path('factura/identificadorUpdate/<int:pk>', IdentificadorUpdateView.as_view(), name='identificadorUpdate'),
    
    path('factura/emisor', EmisorView.as_view(), name='index_emisor'),
    path('factura/emisorCreate', EmisorCreateView.as_view(), name='emisorCreate'),
    path('factura/emisorUpdate/<int:pk>', EmisorUpdateView.as_view(), name='emisorUpdate'),
    
    path('factura/receptor', ReceptorView.as_view(), name='index_receptor'),
    path('factura/receptorCreate', ReceptorCreateView.as_view(), name='receptorCreate'),
    path('factura/receptorUpdate/<int:pk>', ReceptorUpdateView.as_view(), name='receptorUpdate'),
    
    path('facturaSujetoExcluido/sujetoExcluidoMonth/<int:year>/<int:month>', SujetoExcluidoMonthView.as_view(), name='sujetoExcluidoMonth'),
    path('facturaSujetoExcluido/sujetoExcluidoVer/<int:pk>', SujetoExcluidoDetailView.as_view(), name='sujetoExcluidoDetailView'),
    
    path('comprobanteDonacion/otroDocumentoAsociado', OtroDocumentoAsociadoView.as_view(), name='index_otroDocumentoAsociado'),
    path('comprobanteDonacion/otroDocumentoAsociadoCreate', OtroDocumentoAsociadoCreateView.as_view(), name='otroDocumentoAsociadoCreate'),
    path('comprobanteDonacion/otroDocumentoAsociadoUpdate/<int:pk>', OtroDocumentoAsociadoUpdateView.as_view(), name='otroDocumentoAsociadoUpdate'),
    
    path('comprobanteDonacion/cuerpoDocumento', CuerpoDocumentoView.as_view(), name='index_cuerpoDocumento'),
    path('comprobanteDonacion/cuerpoDocumentoCreate', CuerpoDocumentoCreateView.as_view(), name='cuerpoDocumentoCreate'),
    path('comprobanteDonacion/cuerpoDocumentoUpdate/<int:pk>', CuerpoDocumentoUpdateView.as_view(), name='cuerpoDocumentoUpdate'),
    
    path('comprobanteDonacion/pagoDonacion', PagoDonacionView.as_view(), name='index_pagoDonacion'),
    path('comprobanteDonacion/pagoDonacionCreate', PagoDonacionCreateView.as_view(), name='pagoDonacionCreate'),
    path('comprobanteDonacion/pagoDonacionUpdate/<int:pk>', PagoDonacionUpdateView.as_view(), name='pagoDonacionUpdate'),  
    
]
