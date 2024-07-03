from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='panel_facturas'),
    
    path('responses/sujeto_excluido/<int:pk>', views.ResponseHaciendaBySujetoExcluidoListView.as_view(), name='response_hacienda_by_sujeto_excluido_list'),
    path('responses/comprobante_donacion/<int:pk>', views.ResponseHaciendaByComprobanteDonacionListView.as_view(), name='response_hacienda_by_comprobante_donacion_list'),
  
    path('get_operacioneSujetoExcluido', views.get_opercionSujetoExcluido, name='getoperacionesSujetoExcluido'),
    
    path('pais', views.PaisView.as_view(), name='index_pais'),
    path('paisCreate', views.PaisCreateView.as_view(), name='paisCreate'),
    path('paisUpdate/<int:pk>', views.PaisUpdateView.as_view(), name='paisUpdate'),
    
    path('departamento', views.DepartamentoView.as_view(), name='index_departamento'),
    path('departamentoCreate', views.DepartamentoCreateView.as_view(), name='departamentoCreate'),
    path('departamentoUpdate/<int:pk>', views.DepartamentoUpdateView.as_view(), name='departamentoUpdate'),
    
    path('municipio', views.MunicipioView.as_view(), name='index_municipio'),
    path('municipioCreate', views.MunicipioCreateView.as_view(), name='municipioCreate'),
    path('municipioUpdate/<int:pk>', views.MunicipioUpdateView.as_view(), name='municipioUpdate'),
    
    path('direccion', views.DireccionView.as_view(), name='index_direccion'),
    path('direccionCreate', views.DireccionCreateView.as_view(), name='direccionCreate'),
    path('direccionUpdate/<int:pk>', views.DireccionUpdateView.as_view(), name='direccionUpdate'),
    
    path('factura/unidadMedida', views.UnidadMedidaView.as_view(), name='index_unidadMedida'),
    path('factura/unidadMedidaCreate', views.UnidadMedidaCreateView.as_view(), name='unidadMedidaCreate'),
    path('factura/unidadMedidaUpdate/<int:pk>', views.UnidadMedidaUpdateView.as_view(), name='unidadMedidaUpdate'),
    
    path('facturaSujetoExcluido/operacionSujetoExcluido', views.OperacionSujetoExcluidoView.as_view(), name='index_operacionSujetoExcluido'),
    path('facturaSujetoExcluido/operacionSujetoExcluidoCreate/<int:id>', views.OperacionSujetoExcluidoCreateView.as_view(), name='operacionSujetoExcluidoCreate'),
    path('facturaSujetoExcluido/operacionSujetoExcluidoUpdate/<int:pk>', views.OperacionSujetoExcluidoUpdateView.as_view(), name='operacionSujetoExcluidoUpdate'),
    path('facturaSujetoExcluido/operacionSujetoExcluidoVer/<int:pk>', views.OperacionSujetoExcluidoDetailView.as_view(), name='operacionSujetoExcluidoVer'),
    
    path('facturaSujetoExcluido/formaPago', views.FormaPagoView.as_view(), name='index_formaPago'),
    path('facturaSujetoExcluido/formaPagoCreate', views.FormaPagoCreateView.as_view(), name='formaPagoCreate'),
    path('facturaSujetoExcluido/formaPagoUpdate/<int:pk>', views.FormaPagoUpdateView.as_view(), name='formaPagoUpdate'),
    
    path('facturaSujetoExcluido/pago', views.PagoView.as_view(), name='index_pago'),
    path('facturaSujetoExcluido/pagoCreate', views.PagoCreateView.as_view(), name='pagoCreate'),
    path('facturaSujetoExcluido/pagoUpdate/<int:pk>', views.PagoUpdateView.as_view(), name='pagoUpdate'),
    
    path('factura/apendice', views.ApendiceView.as_view(), name='index_apendice'),
    path('factura/apendiceCreate/<int:pk>', views.ApendiceCreateView.as_view(), name='apendiceCreate'),
    path('factura/apendiceUpdate/<int:pk>', views.ApendiceUpdateView.as_view(), name='apendiceUpdate'),
    
    path('factura/tipoDocumento', views.TipoDocumentoView.as_view(), name='index_tipoDocumento'),
    path('factura/tipoDocumentoCreate', views.TipoDocumentoCreateView.as_view(), name='tipoDocumentoCreate'),
    path('factura/tipoDocumentoUpdate/<int:pk>', views.TipoDocumentoUpdateView.as_view(), name='tipoDocumentoUpdate'),
    
    path('factura/identificador', views.IdentificadorView.as_view(), name='index_identificador'),
    path('factura/identificadorCreate', views.IdentificadorCreateView.as_view(), name='identificadorCreate'),
    path('factura/identificadorUpdate/<int:pk>', views.IdentificadorUpdateView.as_view(), name='identificadorUpdate'),
    
    path('factura/receptor', views.ReceptorView.as_view(), name='index_receptor'),
    path('factura/receptorCreate', views.ReceptorCreateView.as_view(), name='receptorCreate'),
    path('factura/receptorUpdate/<int:pk>', views.ReceptorUpdateView.as_view(), name='receptorUpdate'),
    
    path('facturaSujetoExcluido/sujetoExcluidoMonth/<int:year>/<int:month>', views.SujetoExcluidoMonthView.as_view(month_format='%m'), name='sujetoExcluidoMonth'),
    path('facturaSujetoExcluido/sujetoExcluidoCreate', views.SujetoExcluidoCreateView.as_view(), name='sujetoExcluidoCreateView'),
    path('facturaSujetoExcluido/sujetoExcluidoVer/<int:pk>', views.SujetoExcluidoDetailView.as_view(), name='sujetoExcluidoDetailView'),
    path('facturaSujetoExcluido/sujetoExcluidoUpdate/<int:pk>', views.SujetoExcluidoUpdateView.as_view(), name='sujetoExcluidoUpdateView'),
    path('facturaSujetoExcluido/transmitirSujetoExcluido/<int:pk>', views.Transmitir.as_view(), name='transmitirSujetoExcluido'),
    
    path('comprobanteDonacion/otroDocumentoAsociado', views.OtroDocumentoAsociadoView.as_view(), name='index_otroDocumentoAsociado'),
    path('comprobanteDonacion/otroDocumentoAsociadoCreate', views.OtroDocumentoAsociadoCreateView.as_view(), name='otroDocumentoAsociadoCreate'),
    path('comprobanteDonacion/otroDocumentoAsociadoUpdate/<int:pk>', views.OtroDocumentoAsociadoUpdateView.as_view(), name='otroDocumentoAsociadoUpdate'),
    
    path('comprobanteDonacion/cuerpoDocumento', views.CuerpoDocumentoView.as_view(), name='index_cuerpoDocumento'),
    path('comprobanteDonacion/cuerpoDocumentoCreate', views.CuerpoDocumentoCreateView.as_view(), name='cuerpoDocumentoCreate'),
    path('comprobanteDonacion/cuerpoDocumentoUpdate/<int:pk>', views.CuerpoDocumentoUpdateView.as_view(), name='cuerpoDocumentoUpdate'),
    
    path('comprobanteDonacion/pagoDonacion', views.PagoDonacionView.as_view(), name='index_pagoDonacion'),
    path('comprobanteDonacion/pagoDonacionCreate', views.PagoDonacionCreateView.as_view(), name='pagoDonacionCreate'),
    path('comprobanteDonacion/pagoDonacionUpdate/<int:pk>', views.PagoDonacionUpdateView.as_view(), name='pagoDonacionUpdate'),  
    
    path('facturaComprobanteDonacion/comprobanteDonacionMonth/<int:year>/<int:month>', views.ComprobanteDonacionMonthView.as_view(month_format='%m'), name='comprobanteDonacionMonth'),
    path('facturaComprobanteDonacion/comprobanteDonacionCreate', views.ComprobanteDonacionCreateView.as_view(), name='comprobanteDonacionCreateView'),
    path('facturaComprobanteDonacion/comprobanteDonacionVer/<int:pk>', views.ComprobanteDonacionDetailView.as_view(), name='comprobanteDonacionDetailView'),
    path('facturaComprobanteDonacion/comprobanteDonacionUpdate/<int:pk>', views.ComprobanteDonacionUpdateView.as_view(), name='comprobanteDonacionUpdateView'),
    path('facturaComprobanteDonacion/transmitirComprobanteDonacion/<int:pk>', views.Transmitir.as_view(), name='transmitirComprobanteDonacion'),
    
]
