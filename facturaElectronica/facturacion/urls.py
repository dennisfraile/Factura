from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('panelFacturas/', views.IndexView.as_view(), name='panel_facturas'),
    
    path('responses/sujeto_excluido/<int:pk>', views.ResponseHaciendaBySujetoExcluidoListView.as_view(), name='response_hacienda_by_sujeto_excluido_list'),
    path('responses/comprobante_donacion/<int:pk>', views.ResponseHaciendaByComprobanteDonacionListView.as_view(), name='response_hacienda_by_comprobante_donacion_list'),
    path('responses/factura_electronica/<int:pk>', views.ResponseHaciendaByFacturaElectronicaListView.as_view(), name='response_hacienda_by_factura_electronica_list'),
  
    path('get_operacioneSujetoExcluido', views.get_opercionSujetoExcluido, name='getoperacionesSujetoExcluido'),
    
    path('factura/pais', views.PaisView.as_view(), name='index_pais'),
    path('factura/paisCreate', views.PaisCreateView.as_view(), name='paisCreate'),
    path('factura/paisUpdate/<int:pk>', views.PaisUpdateView.as_view(), name='paisUpdate'),
    
    path('factura/departamento', views.DepartamentoView.as_view(), name='index_departamento'),
    path('factura/departamentoCreate', views.DepartamentoCreateView.as_view(), name='departamentoCreate'),
    path('factura/departamentoUpdate/<int:pk>', views.DepartamentoUpdateView.as_view(), name='departamentoUpdate'),
    
    path('factura/municipio', views.MunicipioView.as_view(), name='index_municipio'),
    path('factura/municipioCreate', views.MunicipioCreateView.as_view(), name='municipioCreate'),
    path('factura/municipioUpdate/<int:pk>', views.MunicipioUpdateView.as_view(), name='municipioUpdate'),
    
    path('factura/direccion', views.DireccionView.as_view(), name='index_direccion'),
    path('factura/direccionCreate', views.DireccionCreateView.as_view(), name='direccionCreate'),
    path('factura/direccionUpdate/<int:pk>', views.DireccionUpdateView.as_view(), name='direccionUpdate'),
    
    path('factura/unidadMedida', views.UnidadMedidaView.as_view(), name='index_unidadMedida'),
    path('factura/unidadMedidaCreate', views.UnidadMedidaCreateView.as_view(), name='unidadMedidaCreate'),
    path('factura/unidadMedidaUpdate/<int:pk>', views.UnidadMedidaUpdateView.as_view(), name='unidadMedidaUpdate'),
    
    path('factura/operacionSujetoExcluido', views.OperacionSujetoExcluidoView.as_view(), name='index_operacionSujetoExcluido'),
    path('factura/operacionSujetoExcluidoCreate/<int:id>', views.OperacionSujetoExcluidoCreateView.as_view(), name='operacionSujetoExcluidoCreate'),
    path('factura/operacionSujetoExcluidoUpdate/<int:pk>', views.OperacionSujetoExcluidoUpdateView.as_view(), name='operacionSujetoExcluidoUpdate'),
    path('factura/operacionSujetoExcluidoVer/<int:pk>', views.OperacionSujetoExcluidoDetailView.as_view(), name='operacionSujetoExcluidoVer'),
    
    path('factura/formaPago', views.FormaPagoView.as_view(), name='index_formaPago'),
    path('factura/formaPagoCreate', views.FormaPagoCreateView.as_view(), name='formaPagoCreate'),
    path('factura/formaPagoUpdate/<int:pk>', views.FormaPagoUpdateView.as_view(), name='formaPagoUpdate'),
    
    path('factura/pago', views.PagoView.as_view(), name='index_pago'),
    path('factura/pagoCreate', views.PagoCreateView.as_view(), name='pagoCreate'),
    path('factura/pagoUpdate/<int:pk>', views.PagoUpdateView.as_view(), name='pagoUpdate'),
    
    path('factura/apendice', views.ApendiceView.as_view(), name='index_apendice'),
    path('factura/apendiceCreate/<int:pk>', views.ApendiceCreateView.as_view(), name='apendiceCreate'),
    path('factura/apendiceUpdate/<int:pk>', views.ApendiceUpdateView.as_view(), name='apendiceUpdate'),
    
    path('factura/tipoDocumento', views.TipoDocumentoView.as_view(), name='index_tipoDocumento'),
    path('factura/tipoDocumentoCreate', views.TipoDocumentoCreateView.as_view(), name='tipoDocumentoCreate'),
    path('factura/tipoDocumentoUpdate/<int:pk>', views.TipoDocumentoUpdateView.as_view(), name='tipoDocumentoUpdate'),
    
    path('factura/identificador', views.IdentificadorView.as_view(), name='index_identificador'),
    path('factura/identificadorCreate/<int:pk>', views.IdentificadorCreateView.as_view(), name='identificadorCreate'),
    path('factura/identificadorUpdate/<int:pk>', views.IdentificadorUpdateView.as_view(), name='identificadorUpdate'),
    
    path('factura/receptor', views.ReceptorView.as_view(), name='index_receptor'),
    path('factura/receptorCreate', views.ReceptorCreateView.as_view(), name='receptorCreate'),
    path('factura/receptorUpdate/<int:pk>', views.ReceptorUpdateView.as_view(), name='receptorUpdate'),
    
    path('factura/sujetoExcluidoMonth/<int:year>/<int:month>', views.SujetoExcluidoMonthView.as_view(month_format='%m'), name='sujetoExcluidoMonth'),
    path('factura/sujetoExcluidoCreate', views.SujetoExcluidoCreateView.as_view(), name='sujetoExcluidoCreateView'),
    path('factura/sujetoExcluidoVer/<int:pk>', views.SujetoExcluidoDetailView.as_view(), name='sujetoExcluidoDetailView'),
    path('factura/sujetoExcluidoUpdate/<int:pk>', views.SujetoExcluidoUpdateView.as_view(), name='sujetoExcluidoUpdateView'),
    path('factura/transmitirSujetoExcluido/<int:pk>', views.Transmitir.as_view(), name='transmitirSujetoExcluido'),
    
    path('factura/comprobanteDonacion/otroDocumentoAsociado', views.OtroDocumentoAsociadoView.as_view(), name='index_otroDocumentoAsociado'),
    path('factura/comprobanteDonacion/otroDocumentoAsociadoCreate/<int:id>', views.OtroDocumentoAsociadoCreateView.as_view(), name='otroDocumentoAsociadoCreate'),
    path('factura/comprobanteDonacion/otroDocumentoAsociadoUpdate/<int:pk>', views.OtroDocumentoAsociadoUpdateView.as_view(), name='otroDocumentoAsociadoUpdate'),
    
    path('factura/comprobanteDonacion/cuerpoDocumento', views.CuerpoDocumentoView.as_view(), name='index_cuerpoDocumento'),
    path('factura/comprobanteDonacion/cuerpoDocumentoCreate/<int:id>', views.CuerpoDocumentoCreateView.as_view(), name='cuerpoDocumentoCreate'),
    path('factura/comprobanteDonacion/cuerpoDocumentoUpdate/<int:pk>', views.CuerpoDocumentoUpdateView.as_view(), name='cuerpoDocumentoUpdate'),
    
    path('factura/comprobanteDonacion/pagoDonacion', views.PagoDonacionView.as_view(), name='index_pagoDonacion'),
    path('factura/comprobanteDonacion/pagoDonacionCreate', views.PagoDonacionCreateView.as_view(), name='pagoDonacionCreate'),
    path('factura/comprobanteDonacion/pagoDonacionUpdate/<int:pk>', views.PagoDonacionUpdateView.as_view(), name='pagoDonacionUpdate'),  
    
    path('factura/comprobanteDonacionMonth/<int:year>/<int:month>', views.ComprobanteDonacionMonthView.as_view(month_format='%m'), name='comprobanteDonacionMonth'),
    path('factura/comprobanteDonacionCreate', views.ComprobanteDonacionCreateView.as_view(), name='comprobanteDonacionCreateView'),
    path('factura/comprobanteDonacionVer/<int:pk>', views.ComprobanteDonacionDetailView.as_view(), name='comprobanteDonacionDetailView'),
    path('factura/comprobanteDonacionUpdate/<int:pk>', views.ComprobanteDonacionUpdateView.as_view(), name='comprobanteDonacionUpdateView'),
    path('factura/transmitirComprobanteDonacion/<int:pk>', views.Transmitir.as_view(), name='transmitirComprobanteDonacion'),
    
    path('factura/facturaElectronicaMonth/<int:year>/<int:month>', views.FacturaElectronicaMonthView.as_view(month_format='%m'), name='facturaElectronicaMonth'),
    path('factura/facturaElectronicaCreate', views.FacturaElectronicaCreateView.as_view(), name='facturaElectronicaCreateView'),
    path('factura/facturaElectronicaVer/<int:pk>', views.FacturaElectronicaDetailView.as_view(), name='facturaElectronicaDetailView'),
    path('factura/facturaElectronicaUpdate/<int:pk>', views.FacturaElectronicaUpdateView.as_view(), name='facturaElectronicaUpdateView'),
    path('factura/transmitirFacturaElectronica/<int:pk>', views.Transmitir.as_view(), name='transmitirFacturaElectronica'),
    
    path('factura/documentoCreate', views.DocumentoCreateView.as_view(), name='documentoCreateView'),
    path('factura/documentoVer/<int:pk>', views.DocumentoDetailView.as_view(), name='documentoDetailView'),
    path('factura/documentoUpdate/<int:pk>', views.DocumentoUpdateView.as_view(), name='documentoUpdateView'),
    
    path('factura/ventaTerceroCreate', views.VentaTerceroCreateView.as_view(), name='ventaTerceroCreateView'),
    path('factura/ventaTerceroVer/<int:pk>', views.VentaTerceroDetailView.as_view(), name='ventaTerceroDetailView'),
    path('factura/ventaTerceroUpdate/<int:pk>', views.VentaTerceroUpdateView.as_view(), name='ventaTerceroUpdateView'),
    
    path('factura/otroDocumentoCreate', views.OtroDocumentoCreateView.as_view(), name='otroDocumentoCreateView'),
    path('factura/otroDocumentoVer/<int:pk>', views.OtroDocumentoDetailView.as_view(), name='otroDocumentoDetailView'),
    path('factura/otroDocumentoUpdate/<int:pk>', views.OtroDocumentoUpdateView.as_view(), name='otroDocumentoUpdateView'),
    
    path('factura/medicoCreate', views.MedicoCreateView.as_view(), name='medicoCreateView'),
    path('factura/medicoVer/<int:pk>', views.MedicoDetailView.as_view(), name='medicoDetailView'),
    path('factura/medicoUpdate/<int:pk>', views.MedicoUpdateView.as_view(), name='medicoUpdateView'),
    
    path('factura/documentoRelacionadoCreate', views.DocumentoRelacionadoCreateView.as_view(), name='documentoRelacionadoCreateView'),
    path('factura/documentoRelacionadoVer/<int:pk>', views.DocumentoRelacionadoDetailView.as_view(), name='documentoRelacionadoDetailView'),
    path('factura/documentoRelacionadoUpdate/<int:pk>', views.DocumentoRelacionadoUpdateView.as_view(), name='documentoRelacionadoUpdateView'),
    
    path('factura/extencionCreate', views.ExtencionCreateView.as_view(), name='extencionCreateView'),
    path('factura/extencionVer/<int:pk>', views.ExtencionDetailView.as_view(), name='extencionDetailView'),
    path('factura/extencionUpdate/<int:pk>', views.ExtencionUpdateView.as_view(), name='extencionUpdateView'),
    
    path('factura/pagoFacturaCreate', views.PagoFacturaCreateView.as_view(), name='pagoFacturaCreateView'),
    path('factura/pagoFacturaVer/<int:pk>', views.PagoFacturaDetailView.as_view(), name='pagoFacturaDetailView'),
    path('factura/pagoFacturaUpdate/<int:pk>', views.PagoFacturaUpdateView.as_view(), name='pagoFacturaUpdateView'),
    
    path('factura/tributoResumenCreate', views.TributoResumenCreateView.as_view(), name='tributoResumenCreateView'),
    path('factura/tributoResumenUpdate/<int:pk>', views.TributoResumenUpdateView.as_view(), name='tributoResumenUpdateView'),
    
    path('factura/tributoCreate', views.TributoCreateView.as_view(), name='tributoCreateView'),
    path('factura/tributoUpdate/<int:pk>', views.TributoUpdateView.as_view(), name='tributoUpdateView'),
    
    path('generar-pdf/<int:id>/', views.generar_pdf_view, name='generar_pdf'),
    
]
