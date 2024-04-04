from django.urls import path
from django.conf.urls.static import static
from facturacion import views

urlpatterns = [
    path('', views.index),
    path('facturas/sujetoescluido', views.sujetoExcluido),
    path('facturas/facturaelectronica', views.facturaElectronica),
    path('facturas/comprobantedonacion', views.comprobanteDonacion),
    path('facturas/comprobantecreditofiscal', views.comprobanteCreditoFiscal),
]
