from django.shortcuts import render
from calendar import month
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http.response import HttpResponse
from .models import *
from .forms import *
from usuarios.models import *
from datetime import datetime, timedelta, date
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.views.generic.dates import MonthArchiveView, YearArchiveView
from django.views.generic.list import ListView
from django.views.generic import DetailView, View, TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import jwt
import json
from django.http import JsonResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io
from django.core.mail import EmailMessage
# Create your views here.

@login_required(redirect_field_name='/ingresar')
def get_opercionSujetoExcluido(request):
    operacionesSujetoExccluido = OperacionesSujetoExcluido.objects.all()
    return JsonResponse(list(operacionesSujetoExccluido), safe = False)

@login_required(redirect_field_name='/ingresar')
class IndexView(TemplateView):
    template_name = 'views/index.html'

@login_required(redirect_field_name='/ingresar')    
class PaisView(View):
    
    login_url = '/ingresar/'
    template_name = 'pais_view.html'
    model = Pais
    
    def get_context_data(self, **kwargs) :
        context = super(Pais, self).get_context(**kwargs)
        pais = Pais.objects.all()
        context['registro'] = pais
        return context

@login_required(redirect_field_name='/ingresar')    
class PaisCreateView(UserPassesTestMixin,CreateView):
    
    login_url = '/ingresar'
    template_name = 'pais_form.html'
    form_class = PaisForm
    model = Pais
    
    def get_success_url(self):
        return reverse_lazy('paisList')
    
    def post(self, request, *args, **kwargs):
        pk=self.kwargs.get("pk")
        codigo = request.POST.get("codigo")
        valor = request.POST.get("valor")
        pais= Pais.objects.create(codigo=codigo, valor=valor)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a creado el pais: "+ codigo + " " + valor + "con exito")
        return redirect('paisList')

@login_required(redirect_field_name='/ingresar')
class PaisUpdateView(UserPassesTestMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'pais_form.html'
    form_class = PaisForm
    
    def get_success_url(self):
        return reverse_lazy('paisList')

    def post(self, request, *args, **kwargs):
        pk=self.kwargs.get("pk")
        codigo = request.POST.get("codigo")
        valor = request.POST.get("valor")
        Pais.objects.update(codigo=codigo, valor=valor)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a actualizado el pais: "+ codigo + " " + valor + "con exito")
        return redirect('paisList')

@login_required(redirect_field_name='/ingresar')
class DepartamentoView(View):
    
    login_url = '/ingresar/'
    template_name = 'departamento_view.html'
    model = Departamento
    
    def get_context_data(self, **kwargs) :
        context = super(Departamento, self).get_context(**kwargs)
        departamento = Departamento.objects.all()
        context['registro'] = departamento
        return context

@login_required(redirect_field_name='/ingresar')   
class DepartamentoCreateView(UserPassesTestMixin,CreateView):
    
    login_url = '/ingresar'
    template_name = 'departamento_form.html'
    form_class = DepartamentoForm
    model = Departamento
    
    def get_success_url(self):
        return reverse_lazy('departamentoList')
    
    def post(self, request, *args, **kwargs):
        pk=self.kwargs.get("pk")
        codigo = request.POST.get("codigo")
        valor = request.POST.get("valor")
        departamento= Departamento.objects.create(codigo=codigo, valor=valor)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a creado el departamento: "+ codigo + " " + valor + "con exito")
        return redirect('departamentoList')

@login_required(redirect_field_name='/ingresar')
class DepartamentoUpdateView(UserPassesTestMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'departamento_form.html'
    form_class = DepartamentoForm
    
    def get_success_url(self):
        return reverse_lazy('departamentoList')

    def post(self, request, *args, **kwargs):
        pk=self.kwargs.get("pk")
        codigo = request.POST.get("codigo")
        valor = request.POST.get("valor")
        Departamento.objects.update(codigo=codigo, valor=valor)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a actualizado el departamento: "+ codigo + " " + valor + "con exito")
        return redirect('departamentoList')

@login_required(redirect_field_name='/ingresar')
class MunicipioView(View):
    
    login_url = '/ingresar/'
    template_name = 'municipio_view.html'
    model = Municipio
    
    def get_context_data(self, **kwargs) :
        context = super(Municipio, self).get_context(**kwargs)
        municipio = Municipio.objects.all()
        context['registro'] = municipio
        return context

@login_required(redirect_field_name='/ingresar')    
class MunicipioCreateView(UserPassesTestMixin,CreateView):
    
    login_url = '/ingresar'
    template_name = 'municipio_form.html'
    form_class = MunicipioForm
    model = Municipio
    
    def get_success_url(self):
        return reverse_lazy('municipioList')
    
    def post(self, request, *args, **kwargs):
        pk=self.kwargs.get("pk")
        codigo = request.POST.get("codigo")
        valor = request.POST.get("valor")
        departamentoId = request.POST.get("departamento")
        departamento = Departamento.objects.get(id=departamentoId)
        municipio= Municipio.objects.create(codigo=codigo, valor=valor, departamento=departamento)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a creado el municipio: "+ codigo + " " + valor + "con exito")
        return redirect('paisList')

@login_required(redirect_field_name='/ingresar')
class MunicipioUpdateView(UserPassesTestMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'municipio_form.html'
    form_class = MunicipioForm
    
    def get_success_url(self):
        return reverse_lazy('municipioList')

    def post(self, request, *args, **kwargs):
        pk=self.kwargs.get("pk")
        codigo = request.POST.get("codigo")
        valor = request.POST.get("valor")
        departamentoId = request.POST.get("departamento")
        departamento = Departamento.objects.get(id=departamentoId)
        Municipio.objects.update(codigo=codigo, valor=valor, departamento=departamento)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a actualizado el municipio: "+ codigo + " " + valor + "con exito")
        return redirect('paisList')

@login_required(redirect_field_name='/ingresar')
class DireccionView(View):
    
    login_url = '/ingresar/'
    template_name = 'direccion_view.html'
    model = Direccion
    
    def get_context_data(self, **kwargs) :
        context = super(Direccion, self).get_context(**kwargs)
        direccion = Direccion.objects.all()
        context['registro'] = direccion
        return context

@login_required(redirect_field_name='/ingresar')    
class DireccionCreateView(UserPassesTestMixin,CreateView):
    
    login_url = '/ingresar'
    template_name = 'direccion_form.html'
    form_class = DireccionForm
    model = Direccion
    
    def get_success_url(self):
        origin = self.request.POST.get('origin')
        if origin == 'entidad':
            receptor_id = self.request.POST.get('receptor_id')
            if receptor_id:
                return redirect('receptorUpdate', pk=receptor_id)
            else:
                return redirect('receptorCreate')
        elif origin == 'receptor':
            entidad_id = self.request.POST.get('entidad_id')
            if entidad_id:
                return redirect('entidadUpdate', pk=entidad_id)
            else:
                return redirect('entidadCreate')
        else:
            return redirect('panel_facturas')
    
    def post(self, request, *args, **kwargs):
        pk=self.kwargs.get("pk")
        complementoDireccion = request.POST.get("complementoDireccion")
        municipioId = request.POST.get("municipio")
        municipio = Municipio.objects.get(id=municipioId)
        direccion= Direccion.objects.create(complementoDireccion=complementoDireccion, municipio=municipio)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a creado la direccion: "+ complementoDireccion + " "  + "con exito")
        return redirect('direccionList')

@login_required(redirect_field_name='/ingresar')
class DireccionUpdateView(UserPassesTestMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'direccion_form.html'
    form_class = DireccionForm
    
    def get_success_url(self):
        origin = self.request.POST.get('origin')
        if origin == 'entidad':
            receptor_id = self.request.POST.get('receptor_id')
            if receptor_id:
                return redirect('receptorUpdate', pk=receptor_id)
            else:
                return redirect('receptorCreate')
        elif origin == 'receptor':
            entidad_id = self.request.POST.get('entidad_id')
            if entidad_id:
                return redirect('entidadUpdate', pk=entidad_id)
            else:
                return redirect('entidadCreate')
        else:
            return redirect('panel_facturas')

    def post(self, request, *args, **kwargs):
        pk=self.kwargs.get("pk")
        complementoDireccion = request.POST.get("complementoDireccion")
        municipioId = request.POST.get("municipio")
        municipio = Municipio.objects.get(id=municipioId)
        Direccion.objects.update(complementoDireccion=complementoDireccion, municipio=municipio)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a actualizado la direccion: "+ complementoDireccion + " " + "con exito")
        return redirect('direccionList')

@login_required(redirect_field_name='/ingresar')
class UnidadMedidaView(View):
    
    login_url = '/ingresar/'
    template_name = 'unidad_medida_view.html'
    model = UnidadMedida
    
    def get_context_data(self, **kwargs) :
        context = super(UnidadMedida, self).get_context(**kwargs)
        unidadMedida = UnidadMedida.objects.all()
        context['registro'] = unidadMedida
        return context

@login_required(redirect_field_name='/ingresar')    
class UnidadMedidaCreateView(UserPassesTestMixin,CreateView):
    
    login_url = '/ingresar'
    template_name = 'unidad_medida_form.html'
    form_class = UnidadMedidaForm
    model = UnidadMedida
    
    def get_success_url(self):
        return reverse_lazy('unidadMedidaList')
    
    def post(self, request, *args, **kwargs):
        pk=self.kwargs.get("pk")
        codigo = request.POST.get("codigo")
        valor = request.POST.get("valor")
        unidadMedida= UnidadMedida.objects.create(codigo=codigo, valor=valor)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a creado la unidad de medida: "+ codigo + " " + valor + "con exito")
        return redirect('unidadMedidaList')

@login_required(redirect_field_name='/ingresar')
class UnidadMedidaUpdateView(UserPassesTestMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'unidad_medida_form.html'
    form_class = UnidadMedidaForm
    
    def get_success_url(self):
        return reverse_lazy('unidadMedidaList')

    def post(self, request, *args, **kwargs):
        pk=self.kwargs.get("pk")
        codigo = request.POST.get("codigo")
        valor = request.POST.get("valor")
        UnidadMedida.objects.update(codigo=codigo, valor=valor)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a actualizado la unidad de medida: "+ codigo + " " + valor + "con exito")
        return redirect('unidadMedidaList')

@login_required(redirect_field_name='/ingresar')
class OperacionSujetoExcluidoView(View):
    
    login_url = '/ingresar'
    template_name = 'operacion_sujeto_exluido_view.html'
    model = OperacionesSujetoExcluido
    
    def get_context_data(self, **kwargs) :
        context = super(OperacionesSujetoExcluido, self).get_context(**kwargs)
        operacionesSujetoExcluido = OperacionesSujetoExcluido.objects.all()
        context['registro'] = operacionesSujetoExcluido
        return context

@login_required(redirect_field_name='/ingresar')
class OperacionSujetoExcluidoCreateView(UserPassesTestMixin, CreateView):
    
    login_url = '/ingresar'
    template_name = 'operacion_sujeto_excluido_form.html'
    form_class = OperacionesSujetoExcluidoForm
    model = OperacionesSujetoExcluido
    
    def get_success_url(self):
        return reverse_lazy('sujetoExcluidoDetailView', kwargs={'pk':id})
    
    def post(self, request, *args, **kwargs):
        id=self.kwargs.get("id")
        sujetoExcluido = get_object_or_404(SujetoExcluido, pk=id)
        user = request.user
        entidad = user.Usuarios.all()
        numItem = request.POST.get('numItem')
        codigo = request.POST.get('codigo')
        idUnidadMedida = request.POST.get('unidadMedida')
        unidadMedida = get_object_or_404(UnidadMedida, pk=idUnidadMedida)
        cantidad = request.POST.get('canitdad')
        montoDescu = request.POST.get('montoDescu')
        compra = request.POST.get('compra')
        retencion = request.POST.get('retencion')
        description = request.POST.get('description')
        precioUni = request.POST.get('precioUni')
        operacion = OperacionesSujetoExcluido.objects.create(numItem=numItem, codigo=codigo, uniMedida=unidadMedida, cantidad=cantidad, 
                                                             montoDescu=montoDescu, compra=compra, retencion=retencion, descripccion=description,
                                                             precioUni=precioUni, sujetoExcluido=sujetoExcluido, entidad=entidad)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a creado la operacion del sujeto excluido con exito")
        return redirect(reverse_lazy('sujetoExcluidoDetailView', kwargs={'pk':id}))

@login_required(redirect_field_name='/ingresar')
class OperacionSujetoExcluidoUpdateView(UserPassesTestMixin, UpdateView):
    
    login_url = '/ingresar'
    template_name = 'operacion_sujeto_excluido_form.html'
    form_class = OperacionesSujetoExcluidoForm
    model = OperacionesSujetoExcluido
    
    def get_success_url(self):
        id=self.kwargs.get("pk")
        return reverse_lazy('sujetoExcluidoDetailView', kwargs={'pk':id})
    
    def post(self, request, *args, **kwargs):
        sujetoExcluido = get_object_or_404(SujetoExcluido, pk=id)
        numItem = request.POST.get('numItem')
        codigo = request.POST.get('codigo')
        idUnidadMedida = request.POST.get('unidadMedida')
        unidadMedida = get_object_or_404(UnidadMedida, pk=idUnidadMedida)
        cantidad = request.POST.get('canitdad')
        montoDescu = request.POST.get('montoDescu')
        compra = request.POST.get('compra')
        retencion = request.POST.get('retencion')
        description = request.POST.get('description')
        precioUni = request.POST.get('precioUni')
        operacion = OperacionesSujetoExcluido.objects.update(numItem=numItem, codigo=codigo, uniMedida=unidadMedida, cantidad=cantidad, 
                                                             montoDescu=montoDescu, compra=compra, retencion=retencion, descripccion=description,
                                                             precioUni=precioUni, sujetoExcluido=sujetoExcluido)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a actualizado la operacion del sujeto excluido con exito")
        return redirect(reverse_lazy('sujetoExcluidoDetailView', kwargs={'pk':id}))

@login_required(redirect_field_name='/ingresar')
class OperacionSujetoExcluidoDetailView(UserPassesTestMixin, DetailView):
    login_url = '/ingresar/'
    template_name = 'operacion_sujeto_excluido_by_id.html'
    model = OperacionesSujetoExcluido
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        operacionSujetoExcluido = get_object_or_404(OperacionesSujetoExcluido, pk=context['object'].id)
        context['operacion'] = operacionSujetoExcluido
        context['show'] = True
        return context

@login_required(redirect_field_name='/ingresar')
class SujetoExcluidoMonthView(MonthArchiveView):
    """Muestra la lista de sujetos excluidos por mes"""

    login_url='/ingresar/'
    """queryset = SujetoExcluido.objects.all()"""
    data_field = "fechaTransmicion"
    template_name='sujeto_excluido_month.html'
    allow_empty = True
    allow_future = True

    def get_context_data(self, **kwargs) :
        context = super(SujetoExcluido, self).get_context(**kwargs)
        sujeto = SujetoExcluido.objects.all()
        context['registro'] = sujeto
        return context

@login_required(redirect_field_name='/ingresar')
class SujetoExcluidoDetailView(DetailView):
    """Muestra los datos de un sujeto excluido en especifico"""

    login_url = '/ingresar/'
    template_name = 'sujeto_excluido_by_id_view.html'
    model = SujetoExcluido

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sujetoExcluido = SujetoExcluido.objects.filter(id=context['object'].id)
        operacionesSujetoExcluido = OperacionesSujetoExcluido.objects.filter(id=sujetoExcluido.id) 
        apendice = Apendice.objects.filter(sujetoExcluido=sujetoExcluido)
        context['sujetoExcluido'] = sujetoExcluido
        context['operacionesSujetoExcluido'] = operacionesSujetoExcluido
        context['apendice'] = apendice
        context['show'] = True
        return context   

@login_required(redirect_field_name='/ingresar')
class SujetoExcluidoCreateView(UserPassesTestMixin, CreateView):
    
    login_url = '/ingresar/'
    template_name = 'sujeto excluido/sujeto_excluido_create_view.html'
    model = SujetoExcluido
    
    def get_success_url(self):
        current_date = datetime.datetime.now()
        mes = current_date.month
        año = current_date.year
        return reverse_lazy('sujetoExcluidoMonthView', kwargs={'year':año, 'month':mes})
    
    def post(self, request, *args, **kwargs):
        identificadorId = request.POST.get('identificador')
        identificador = get_object_or_404(Identificador, id=identificadorId)
        entidadId = request.POST.get('emisor')
        emisor = get_object_or_404(Entidad, id=entidadId)
        receptorId = request.POST.get('receptor')
        receptor = get_object_or_404(Receptor, id=receptor)
        totalCompra = request.POST.get('totalCompra')
        descu = request.POST.get('descu')
        totalDescu = request.POST.get('totalDescu')
        subtotal = request.POST.get('subtotal')
        retencionIVAMH = request.POST.get('retencionIVAMH')
        ivarete1 = request.POST.get('ivarete1')
        reterenta = request.POST.get('reterenta')
        totalPagar = request.POST.get('totalPagar')
        totalLetras = request.POST.get('totalLetras')
        condicionOperacion = request.POST.get('condicionOperacion')
        pagoId = request.POST.get('pago')
        pago = get_object_or_404(Pago, id=pagoId)
        observaciones = request.POST.get('observaciones')
        user = request.user
        entidad = user.Usuarios.all()
        sujetoExcluido = SujetoExcluido.objects.create(identificador=identificador,emisor=emisor,receptor=receptor,totalCompra=totalCompra,descu=descu,
                                                       totalDescu=totalDescu,subtotal=subtotal,retencionIVAMH=retencionIVAMH,ivarete1=ivarete1,reterenta=reterenta,
                                                       totalPagar=totalPagar,totalLetras=totalLetras,condicionOperacion=condicionOperacion,pago=pago,observaciones=observaciones,
                                                       entidad=entidad)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a creado el sujeto excluido con exito")
        return redirect(self.get_success_url())
        

@login_required(redirect_field_name='/ingresar')
class SujetoExcluidoUpdateView(UserPassesTestMixin, UpdateView):
    
    login_url = '/ingresar/'
    model = SujetoExcluido
    template_name = 'sujeto excluido/sujeto_excluido_create_view.html'    
    
    def get_success_url(self):
        current_date = datetime.datetime.now()
        mes = current_date.month
        año = current_date.year
        return reverse_lazy('sujetoExcluidoMonthView', kwargs={'year':año, 'month':mes})
    
    def post(self, request):
        identificadorId = request.POST.get('identificador')
        identificador = get_object_or_404(Identificador, id=identificadorId)
        entidadId = request.POST.get('emisor')
        emisor = get_object_or_404(Entidad, id=entidadId)
        receptorId = request.POST.get('receptor')
        receptor = get_object_or_404(Receptor, id=receptor)
        totalCompra = request.POST.get('totalCompra')
        descu = request.POST.get('descu')
        totalDescu = request.POST.get('totalDescu')
        subtotal = request.POST.get('subtotal')
        retencionIVAMH = request.POST.get('retencionIVAMH')
        ivarete1 = request.POST.get('ivarete1')
        reterenta = request.POST.get('reterenta')
        totalPagar = request.POST.get('totalPagar')
        totalLetras = request.POST.get('totalLetras')
        condicionOperacion = request.POST.get('condicionOperacion')
        pagoId = request.POST.get('pago')
        pago = get_object_or_404(Pago, id=pagoId)
        observaciones = request.POST.get('observaciones')
        user = request.user
        entidad = user.Usuarios.all()
        sujetoExcluido = SujetoExcluido.objects.create(identificador=identificador,emisor=emisor,receptor=receptor,totalCompra=totalCompra,descu=descu,
                                                       totalDescu=totalDescu,subtotal=subtotal,retencionIVAMH=retencionIVAMH,ivarete1=ivarete1,reterenta=reterenta,
                                                       totalPagar=totalPagar,totalLetras=totalLetras,condicionOperacion=condicionOperacion,pago=pago,observaciones=observaciones)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a actualizado el sujeto excluido con exito")
        return redirect(self.get_success_url())

def sujetoExcluidoList(self,id):
    sujetoExcluido = SujetoExcluido.objects.get(id=id)
    emisor = User.objects.get(id = sujetoExcluido.emisor.emisor.id)
    documentoEmisor = emisor.documentos.all()
    entidad = emisor.Usuarios.all()
    receptor = User.objects.get(id=sujetoExcluido.receptor.receptor.id)
    documentoReceptor = receptor.documentos.all()
    operacionesSujetoExcluido = sujetoExcluido.operacionesSujetoExcluido.all()
    apendiceSujetoExcluido = sujetoExcluido.apendices.all()
    fechaEmi = sujetoExcluido.fechaTransmicion.date()
    horaEmi = sujetoExcluido.get_formatted_time()
    sujetoData = []
    
    sujetoData = {
        'identificacion': {
            'version': sujetoExcluido.identificador.version,
            'ambiente': sujetoExcluido.identificador.ambiente,
            'tipoDte': sujetoExcluido.identificador.tipoDte,
            'numeroControl': sujetoExcluido.identificador.numeroControl,
            'codigoGeneracion': sujetoExcluido.identificador.codigoGeneracion,
            'tipoModelo': sujetoExcluido.identificador.tipoModelo,
            'tipoOperacion': sujetoExcluido.identificador.tipoOperacion,
            'tipoContingencia': sujetoExcluido.identificador.tipoContingencia,
            'motivoContin': sujetoExcluido.identificador.motivoContin,
            'fechaEmi': fechaEmi,
            'horaEmi': horaEmi,
            'tipoMoneda': sujetoExcluido.identificador.tipoMoneda
        },
        'Emisor': {
            "nit": sujetoExcluido.emisor.nit,
            "nrc": sujetoExcluido.emisor.nrc,
            "nombre": sujetoExcluido.emisor.razonSocial,
            "codActividad": sujetoExcluido.emisor.actividadEconomica.codigo,
            "descActividad": sujetoExcluido.emisor.actividadEconomica.valor,
            "direccion": {
                "departamento": sujetoExcluido.emisor.direccionEmisor.municipio.departamento.codigo,
                "municipio": sujetoExcluido.emisor.direccionEmisor.municipio.codigo,
                "complemento": sujetoExcluido.emisor.direccionEmisor.complementoDireccion,
            },
            "telefono": sujetoExcluido.emisor.cellphone,
            "codEstableMH": sujetoExcluido.emisor.codEstableMH,
            "codEstable": sujetoExcluido.emisor.codEstable,
            "codPuntoVentaMH": sujetoExcluido.emisor.codPuntoVentaMH,
            "codPuntoVenta": sujetoExcluido.emisor.codPuntoVenta,
            "correo": sujetoExcluido.emisor.email
        },
        "sujetoExcluido": {
            "tipoDocumento": sujetoExcluido.receptor.tipo,
            "numDocumento": sujetoExcluido.receptor.numero,
            "nombre": sujetoExcluido.receptor.receptor.nombre,
            "codActividad": sujetoExcluido.receptor.actividadEconomica.codigo,
            "descActividad": sujetoExcluido.receptor.actividadEconomica.valor,
            "direccion": {
                "departamento": sujetoExcluido.receptor.direccionReceptor.municipio.departamento.codigo,
                "municipio": sujetoExcluido.receptor.direccionReceptor.municipio.codigo,
                "complemento": sujetoExcluido.receptor.direccionReceptor.complementoDireccion
            },
            "telefono": sujetoExcluido.receptor.cellphone,
            "correo": sujetoExcluido.receptor.email
        },
        "cuerpoDocumento":[],
        "resumen": {
            "totalCompra" : sujetoExcluido.totalCompra,
            "descu" : sujetoExcluido.descu,
            "totalDescu" : sujetoExcluido.totalDescu,
            "subTotal" : sujetoExcluido.subTotal,
            "retencionIVAMH": sujetoExcluido.retencionIVAMH,
            "ivaRete1" : sujetoExcluido.ivaRete1,
            "reteRenta" : sujetoExcluido.reteRenta,
            "totalPagar" : sujetoExcluido.totalPagar,
            "totalLetras" : sujetoExcluido.totalLetras,
            "condicionOperacion" : sujetoExcluido.condicionOperacion,
            "pagos" : [
                {
                    "codigo" : sujetoExcluido.pago.codigo,
                    "formaPago":sujetoExcluido.pago.formaPago,
                    "montoPago" : sujetoExcluido.pago.montoPago,
                    "referencia" : sujetoExcluido.pago.referencia,
                    "plazo" : sujetoExcluido.pago.plazo,
                    "periodo" : sujetoExcluido.pago.periodo
                }
            ],
            "observaciones": sujetoExcluido.observaciones,
        },
        "apendice": []
    }
    for operacion in operacionesSujetoExcluido:
        operacionesData = {
            "numItem" : operacion.numItem,
            "tipoItem" : operacion.tipoItem,
            "codigo" : operacion.codigo,
            "uniMedida": operacion.uniMedida.codigo,
            "cantidad" : operacion.cantidad,
            "montoDescu": operacion.montoDescu,
            "compra": operacion.compra,
            "retencion": operacion.retencion,
            "descripcion" : operacion.descripcion,
            "precioUni": operacion.precioUni
        }
        sujetoData['cuerpoDocumento'].append(operacionesData)
    
    for apendices in apendiceSujetoExcluido:
        apendicesData = {
            "campo": apendices.campo,
            "etiquta": apendices.etiquta,
            "valor": apendices.valor
        }
        sujetoData['apendice'].append(apendicesData)
    
    return JsonResponse(sujetoData, safe=False)
    
@login_required(redirect_field_name='/ingresar')
class Transmitir(View):
    
    def obtenerFactura(self,*args, **kwargs):
        id = self.kwargs.get('id')
        factura = sujetoExcluidoList(id)
        return factura
    @csrf_exempt
    def transmitir(self, codigoGeneracion,*args, **kwargs):
        id = self.kwargs.get('id')
        
        #Generando el pdf a partir del json 
        jsonData = self.obtenerFactura()
        buffer = io.BytesIO()
        # Crear una respuesta de tipo PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="SujetoExcluido.pdf"'
        # Crear el objeto PDF
        pdf = canvas.Canvas(response, pagesize=letter)
        width, height = letter
        # Extraer datos del JSON y escribirlos en el PDF
        text = "Data from JSON:\n"
        for key, value in jsonData.items():
            text += f"{key}: {value}\n"

        pdf.drawString(100, height - 100, text)

        # Finalizar el PDF
        pdf.showPage()
        pdf.save()
        
        pdf = buffer.getvalue()
        buffer.close()
        
        sujetoExcluido = get_object_or_404(SujetoExcluido, pk=id)
        idIdentificador = sujetoExcluido.identificador.id
        identificador = get_object_or_404(Identificador, pk=idIdentificador)
        user = get_object_or_404(User, pk=self.user.pk)
        entidadId = user.entidad.id
        entidad = Entidad.objects.filter(id=entidadId)
        authHacienda = ParametrosAuthHacienda.objects.filter(entidad=entidad.id)
        privateKey = authHacienda.privateKey
        url_auth = 'https://apitest.dtes.mh.gob.sv/seguridad/auth'
        parametros_auth = {
            'content_Type' : 'application/x-www-form-urlencoded',
            'user_agent ': authHacienda.userAgent,
            'user' : authHacienda.user,
            'pwd' : authHacienda.pwd,
            }
        if requests.method == 'POST':
            url_auth = 'https://apitest.dtes.mh.gob.sv/seguridad/auth'
            
            try:
                acesso = requests.post(url_auth, params=parametros_auth).json()  
                responseHacienda = ResponseHacienda(nombre="Auth de Hacienda", datosJason=acesso, sujetoExcluido=sujetoExcluido)
                responseHacienda.save()
                
                if acesso['status'] == "OK":
                    token = acesso['body']['token']
                    private = open('clave_privada.pem', 'r')
                    factura = self.obtenerFactura()
                    encoded = jwt.encode(factura, privateKey, algorithm="HS256")
                    url_recepcion = 'https://apitest.dtes.mh.gob.sv/fesv/recepciondte'
                    parametros_recepcion = {
                        'Authorization': token,
                        'User-Agent': authHacienda.userAgent,
                        'content-Type': 'application/JSON',
                        'ambiente': identificador.ambiente,
                        'idEnvio': identificador.id,
                        'version': identificador.version,
                        'tipoDte': identificador.tipoDte.codigo,
                        'documento': encoded,
                        'codigoGeneracion': codigoGeneracion,
                    }
                    try:
                        transmitir = requests.post(url_recepcion, params=parametros_recepcion).json()
                        responseHacienda = ResponseHacienda(nombre="Transmicion de factura a  Hacienda", datosJason=transmitir, sujetoExcluido=sujetoExcluido)
                        responseHacienda.save()
                        if(transmitir['codigoMsg']=="001"):
                            sujetoExcluido.objects.update(transmitido=True)
                            # Envía un correo electrónico con la factura Electrnica
                            subject = 'Factura Sujeto Excluido'
                            body = f'Hola {sujetoExcluido.receptor.nombre},\n\nse le a emitido una factura de sujeto excluido'
                            from_email = sujetoExcluido.emisor.email  
                            to_email = sujetoExcluido.receptor.email
                            email =  EmailMessage(subject, body, from_email, to_email)
                            jsonContent = json.dumps(jsonData, indent=4)
                            email.attach('data.json', jsonContent, 'application/json')
                            email.attach('data.pdf', pdf, 'application/pdf')
                            email.send()
                    except:
                        messages.danger(self.request, 'Ocurrio un problema en la transmision de la factura' + transmitir['status'])
                    stastus_code = acesso['status']
                    messages.success(self.request, 'Se logueo con exito en hacienda', stastus_code)
                    return redirect(reverse_lazy('sujetoExcluidoDetailView', kwargs={'pk':id}))
                
                else:
                    stastus_code = acesso.status_code
                    messages.success(self.request, 'Ocurrio un error con las credenciales' + acesso['status'])
                    return redirect('authHacienda', pk=authHacienda.pk)
                
            except requests.exceptions.RequestException as e:
                messages.success(self.request, 'Ocurrio un error al hacer la solicitud a la api de hacienda ' + str(e))
            return redirect(reverse_lazy('sujetoExcluidoDetailView', kwargs={'pk':id}))
        else:
            messages.success(self.request, 'Error esta vista solo admite solicitudes POST, error 405')
            return redirect(reverse_lazy('sujetoExcluidoDetailView', kwargs={'pk':id}))
@login_required(redirect_field_name='/ingresar')
class FormaPagoView(View):
    
    login_url = '/ingresar/'
    template_name = 'forma_pago_view.html'
    model = FormaPago
    
    def get_context_data(self, **kwargs) :
        context = super(FormaPagoView, self).get_context(**kwargs)
        formaPago = FormaPago.objects.all()
        context['registro'] = formaPago
        return context

@login_required(redirect_field_name='/ingresar')   
class FormaPagoCreateView(UserPassesTestMixin,CreateView):
    
    login_url = '/ingresar'
    template_name = 'forma_pago_form.html'
    form_class = FormaPagoForm
    model = FormaPago
    
    def get_success_url(self):
        origin = self.request.POST.get('origin')
        if origin == 'pago':
            formapago_id = self.request.POST.get('formapago_id')
            if formapago_id:
                return redirect('pagoUpdate', pk=formapago_id)
            else:
                return redirect('pagoCreate')
        else:
            return redirect('panel_facturas')
    
    def post(self, request, *args, **kwargs):
        pk=self.kwargs.get("pk")
        codigo = request.POST.get("codigo")
        valor = request.POST.get("valor")
        formaPago= FormaPago.objects.create(codigo=codigo, valor=valor)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a creado la forma de pago: "+ codigo + " " + valor + "con exito")
        return redirect('formaPagoList')

@login_required(redirect_field_name='/ingresar')
class FormaPagoUpdateView(UserPassesTestMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'forma_pago_form.html'
    form_class = FormaPagoForm
    
    def get_success_url(self):
        origin = self.request.POST.get('origin')
        if origin == 'pago':
            formapago_id = self.request.POST.get('formapago_id')
            if formapago_id:
                return redirect('pagoUpdate', pk=formapago_id)
            else:
                return redirect('pagoCreate')
        else:
            return redirect('panel_facturas')

    def post(self, request, *args, **kwargs):
        pk=self.kwargs.get("pk")
        codigo = request.POST.get("codigo")
        valor = request.POST.get("valor")
        FormaPago.objects.update(codigo=codigo, valor=valor)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a actualizado la forma de pago: "+ codigo + " " + valor + "con exito")
        return redirect('formaPagoList')

@login_required(redirect_field_name='/ingresar')
class PagoView(View):
    
    login_url = '/ingresar/'
    template_name = 'pago_view.html'
    model = Pago
    
    def get_context_data(self, **kwargs) :
        context = super(Pago, self).get_context(**kwargs)
        pago = Pago.objects.all()
        context['registro'] = pago
        return context

@login_required(redirect_field_name='/ingresar')    
class PagoCreateView(UserPassesTestMixin,CreateView):
    
    login_url = '/ingresar'
    template_name = 'pago_form.html'
    form_class = PagoForm
    model = Pago
    
    def get_success_url(self):
        return reverse_lazy('pagoList')
    
    def post(self, request, *args, **kwargs):
        pk=self.kwargs.get("pk")
        codigo = request.POST.get("codigo")
        formaPagoId = request.POST.get("formaPago")
        formaPago = FormaPago.objects.get(id=formaPagoId)
        montoPago = request.POS.get("montoPago")
        referencia = request.POST.get("referencia")
        plazo = request.POST.get("plazo")
        periodo = request.POST.get("periodo")
        user = request.user
        entidad = user.Usuarios.all()
        pago= Pais.objects.create(codigo=codigo, formaPago=formaPago, montoPago=montoPago, referencia=referencia, plazo=plazo, periodo=periodo, entidad=entidad)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a creado el pago: "+ codigo + " " + montoPago + "con exito")
        return redirect('pagoList')

@login_required(redirect_field_name='/ingresar')
class PagoUpdateView(UserPassesTestMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'pago_form.html'
    form_class = PagoForm
    
    def get_success_url(self):
        return reverse_lazy('paisList')

    def post(self, request, *args, **kwargs):
        pk=self.kwargs.get("pk")
        codigo = request.POST.get("codigo")
        formaPagoId = request.POST.get("formaPago")
        formaPago = FormaPago.objects.get(id=formaPagoId)
        montoPago = request.POS.get("montoPago")
        referencia = request.POST.get("referencia")
        plazo = request.POST.get("plazo")
        periodo = request.POST.get("periodo")
        Pago.objects.update(codigo=codigo, formaPago=formaPago, montoPago=montoPago, referencia=referencia, plazo=plazo, periodo=periodo)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a actualizado el pago: "+ codigo + " " + "con exito")
        return redirect('pagoList')

@login_required(redirect_field_name='/ingresar')
class ApendiceView(DetailView):
    """Muestra los datos de las apendices registradas en el sistema"""
    
    login_url = '/ingresar/'
    template_name = 'apendice_view.html'
    model = Apendice
    
    def get_success_url(self):
        id= self.kwargs['id']
        return reverse_lazy('sujetoExcluidoDetailView', kwargs={'pk':id})
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        apendice = get_object_or_404(Apendice, pk=context['object'].id)
        context['apendice'] = apendice
        context['show'] = True
        return context

@login_required(redirect_field_name='/ingresar')
class ApendiceCreateView(UserPassesTestMixin, CreateView):
    login_url = '/ingresar'
    template_name = 'apendice_form.html'
    form_class = ApendiceForm
    model = Apendice
    
    def get_success_url(self):
        return reverse_lazy('sujetoExcluidoDetailView', kwargs={'pk':id})
    
    def post(self, request, *args, **kwargs):
        id=self.kwargs.get("pk")
        campo = request.POST.get("campo")
        etiqueta = request.POST.get("etiqueta")
        valor = request.POST.get("valor")
        sujetoExcluido = get_object_or_404(SujetoExcluido, pk=id)
        user = request.user
        entidad = user.Usuarios.all()
        apendice = Apendice.objects.create(campo=campo, etiqueta=etiqueta, valor=valor, sujetoExcluido=sujetoExcluido, entidad=entidad)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a creado la panedice: "+ campo + " " + valor + "con exito")
        return redirect(reverse_lazy('sujetoExcluidoDetailView', kwargs={'pk':id}))

@login_required(redirect_field_name='/ingresar')
class ApendiceUpdateView(UserPassesTestMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'apendice_form.html'
    form_class = ApendiceForm
    
    def get_success_url(self):
        id=self.kwargs.get("pk")
        return reverse_lazy('sujetoExcluidoDetailView', kwargs={'pk':id})

    def post(self, request, *args, **kwargs):
        id=self.kwargs.get("pk")
        campo = request.POST.get("campo")
        etiqueta = request.POST.get("etiqueta")
        valor = request.POST.get("valor")
        Apendice.objects.update(campo=campo, etiqueta=etiqueta, valor=valor)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a actualizado el apendice: "+ campo + " " + valor + "con exito")
        return redirect(reverse_lazy('sujetoExcluidoDetailView', kwargs={'pk':id}))

@login_required(redirect_field_name='/ingresar')
class TipoDocumentoView(View):
    
    login_url = '/ingresar/'
    template_name = 'tipo_documento_view.html'
    model = TipoDocumento
    
    def get_context_data(self, **kwargs) :
        context = super(TipoDocumento, self).get_context(**kwargs)
        tipoDocumento= TipoDocumento.objects.all()
        context['registro'] = tipoDocumento
        return context

@login_required(redirect_field_name='/ingresar')    
class TipoDocumentoCreateView(UserPassesTestMixin,CreateView):
    
    login_url = '/ingresar'
    template_name = 'tipo_documento_form.html'
    form_class = TipoDocumentoForm
    model = TipoDocumento
    
    def get_success_url(self):
        return reverse_lazy('tipoDocumentoList')
    
    def post(self, request, *args, **kwargs):
        pk=self.kwargs.get("pk")
        codigo = request.POST.get("codigo")
        valor = request.POST.get("valor")
        tipoDocumento= TipoDocumento.objects.create(codigo=codigo, valor=valor)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a creado el tipo de documento : "+ codigo + " " + valor + "con exito")
        return redirect('tipoDocumentoList')

@login_required(redirect_field_name='/ingresar')
class TipoDocumentoUpdateView(UserPassesTestMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'tipo_documento_form.html'
    form_class = TipoDocumentoForm
    
    def get_success_url(self):
        return reverse_lazy('tipoDocumentoList')

    def post(self, request, *args, **kwargs):
        pk=self.kwargs.get("pk")
        codigo = request.POST.get("codigo")
        valor = request.POST.get("valor")
        TipoDocumento.objects.update(codigo=codigo, valor=valor)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a actualizado el tipo de documento: "+ codigo + " " + valor + "con exito")
        return redirect('tipoDocumentoList')

@login_required(redirect_field_name='/ingresar')
class IdentificadorView(View):
    
    login_url = '/ingresar/'
    template_name = 'identificador_view.html'
    model = Identificador
    
    def get_context_data(self, **kwargs) :
        context = super(Identificador, self).get_context(**kwargs)
        identificador = Identificador.objects.all()
        context['registro'] = identificador
        return context

@login_required(redirect_field_name='/ingresar')    
class IdentificadorCreateView(UserPassesTestMixin,CreateView):
    
    login_url = '/ingresar'
    template_name = 'identificador_form.html'
    form_class = IdentificadorForm
    model = Identificador
    
    def get_success_url(self):
        origin = self.request.POST.get('origin')
        if origin == 'sujetoexcluido':
            sujetoExcluido_id = self.request.POST.get('sujetoExcluido_id')
            if sujetoExcluido_id:
                return redirect('sujetoExcluidoUpdate', pk=sujetoExcluido_id)
            else:
                return redirect('sujetoExcluidoCreate')
        elif origin == 'comprobantedonacion':
            comprobanteDonacion_id = self.request.POST.get('comprobanteDonacion_id')
            if comprobanteDonacion_id:
                return redirect('comprobanteDonacionUpdate', pk=comprobanteDonacion_id)
            else:
                return redirect('comprobanteDonacionCreate')
        else:
            return redirect('identificadorList')
    
    def post(self, request, *args, **kwargs):
        pk=self.kwargs.get("pk")
        version = request.POST.get("version")
        ambiente = request.POST.get("ambiente")
        tipoDteId = request.POST.get("tipoDte")
        tipoDte = TipoDocumento.objects.get(id=tipoDteId)
        tipoModelo = request.POST.get("tipoModelo")
        tipoOperacion = request.POST.get("tipoOperacion")
        tipoContingencia = request.POST.get("tipoContingencia")
        motivoContin = request.POST.get("motivoContin")
        fechaEmi = request.POST.get("fechaEmi")
        tipoMoneda = request.POST.get("tipoMoneda")
        user = request.user
        entidad = user.Usuarios.all()
        identificador= Identificador.objects.create(version=version, ambiente=ambiente, tipoDte=tipoDte,  
                                                    tipoModelo=tipoModelo, tipoOperacion=tipoOperacion, tipoContingencia=tipoContingencia, motivoContin=motivoContin,
                                                    fechaEmision=fechaEmi, tipoMoneda=tipoMoneda, entidad=entidad)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a creado el identificador: "+ version  + " "  + "con exito")
        return redirect('identificadorList')

@login_required(redirect_field_name='/ingresar')
class IdentificadorUpdateView(UserPassesTestMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'identificador_form.html'
    form_class = IdentificadorForm
    
    def get_success_url(self):
        origin = self.request.POST.get('origin')
        if origin == 'sujetoexcluido':
            sujetoExcluido_id = self.request.POST.get('sujetoExcluido_id')
            if sujetoExcluido_id:
                return redirect('sujetoExcluidoUpdate', pk=sujetoExcluido_id)
            else:
                return redirect('sujetoExcluidoCreate')
        elif origin == 'comprobantedonacion':
            comprobanteDonacion_id = self.request.POST.get('comprobanteDonacion_id')
            if comprobanteDonacion_id:
                return redirect('comprobanteDonacionUpdate', pk=comprobanteDonacion_id)
            else:
                return redirect('comprobanteDonacionCreate')
        else:
            return redirect('identificadorList')

    def post(self, request, *args, **kwargs):
        pk=self.kwargs.get("pk")
        version = request.POST.get("version")
        ambiente = request.POST.get("ambiente")
        tipoDteId = request.POST.get("tipoDte")
        tipoDte = TipoDocumento.objects.get(id=tipoDteId)
        numeroControl = request.POST.get("numeroControl")
        codigoGeneracion = request.POST.get("codigoGeneracion")
        tipoModelo = request.POST.get("tipoModelo")
        tipoOperacion = request.POST.get("tipoOperacion")
        tipoContingencia = request.POST.get("tipoContingencia")
        motivoContin = request.POST.get("motivoContin")
        fechaEmi = request.POST.get("fechaEmi")
        tipoMoneda = request.POST.get("tipoMoneda")
        Identificador.objects.update(version=version, ambiente=ambiente, tipoDte=tipoDte, numeroControl=numeroControl,codigoGeneracion=codigoGeneracion, 
                                                    tipoModelo=tipoModelo, tipoOperacion=tipoOperacion, tipoContingencia=tipoContingencia, motivoContin=motivoContin,
                                                    fechaEmision=fechaEmi, tipoMoneda=tipoMoneda)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a actualizado el identificador: "+ version + " " + numeroControl + " " + codigoGeneracion + " "  + "con exito")
        return redirect(self.get_success_url())

@login_required(redirect_field_name='/ingresar')
class ReceptorView(View):
    
    login_url = '/ingresar/'
    template_name = 'receptor_view.html'
    model = Receptor
    
    def get_context_data(self, **kwargs) :
        context = super(Receptor, self).get_context(**kwargs)
        receptor = receptor.objects.all()
        context['registro'] = receptor
        return context

@login_required(redirect_field_name='/ingresar')    
class ReceptorCreateView(UserPassesTestMixin,CreateView):
    
    login_url = '/ingresar'
    template_name = 'receptor_form.html'
    form_class = ReceptorForm
    model = Receptor
    
    def get_success_url(self):
        origin = self.request.POST.get('origin')
        if origin == 'sujetoexcluido':
            sujetoExcluido_id = self.request.POST.get('sujetoExcluido_id')
            if sujetoExcluido_id:
                return redirect('sujetoExcluidoUpdate', pk=sujetoExcluido_id)
            else:
                return redirect('sujetoExcluidoCreate')
        elif origin == 'comprobantedonacion':
            comprobanteDonacion_id = self.request.POST.get('comprobanteDonacion_id')
            if comprobanteDonacion_id:
                return redirect('comprobanteDonacionUpdate', pk=comprobanteDonacion_id)
            else:
                return redirect('comprobanteDonacionCreate')
        else:
            return redirect('identificadorList')
    
    def post(self, request, *args, **kwargs):
        pk=self.kwargs.get("pk")
        tipo = request.POST.get('tipo')
        homologado = request.POST.get('homologado')
        numero = request.POST.get('numero')
        nombre = request.POST.get('nombre')
        actividadEconomicaId = request.POST.get('actividadEconomica')
        actividadEconomica = get_object_or_404(ActividadEconomica,id=actividadEconomicaId)
        direccionReceptorId = request.POST.get('direccionReceptor')
        direccionReceptor = get_object_or_404(Direccion,id=direccionReceptorId)
        cellphone = request.POST.get('cellphone')
        email = request.POST.get('email')
        user = request.user
        entidad = user.Usuarios.all()
        receptor = Receptor.objects.create(tipo=tipo, homologado=homologado, numero=numero,nombre=nombre,actividadEconomica=actividadEconomica,
                                           direccionReceptor=direccionReceptor, cellphone=cellphone, email=email, entidad=entidad)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a creado el receptor:"+ nombre +" con exito")
        return redirect(self.get_success_url())

@login_required(redirect_field_name='/ingresar')
class ReceptorUpdateView(UserPassesTestMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'receptor_form.html'
    form_class = ReceptorForm
    model = Receptor
    
    def get_success_url(self):
        origin = self.request.POST.get('origin')
        if origin == 'sujetoexcluido':
            sujetoExcluido_id = self.request.POST.get('sujetoExcluido_id')
            if sujetoExcluido_id:
                return redirect('sujetoExcluidoUpdate', pk=sujetoExcluido_id)
            else:
                return redirect('sujetoExcluidoCreate')
        elif origin == 'comprobantedonacion':
            comprobanteDonacion_id = self.request.POST.get('comprobanteDonacion_id')
            if comprobanteDonacion_id:
                return redirect('comprobanteDonacionUpdate', pk=comprobanteDonacion_id)
            else:
                return redirect('comprobanteDonacionCreate')
        else:
            return redirect('identificadorList')

    def post(self, request, *args, **kwargs):
        pk=self.kwargs.get("pk")
        tipo = request.POST.get('tipo')
        homologado = request.POST.get('homologado')
        numero = request.POST.get('numero')
        nombre = request.POST.get('nombre')
        actividadEconomicaId = request.POST.get('actividadEconomica')
        actividadEconomica = get_object_or_404(ActividadEconomica,id=actividadEconomicaId)
        direccionReceptorId = request.POST.get('direccionReceptor')
        direccionReceptor = get_object_or_404(Direccion,id=direccionReceptorId)
        cellphone = request.POST.get('cellphone')
        email = request.POST.get('email')
        receptor = Receptor.objects.update(tipo=tipo, homologado=homologado, numero=numero,nombre=nombre,actividadEconomica=actividadEconomica,
                                           direccionReceptor=direccionReceptor, cellphone=cellphone, email=email)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a creado el receptor:"+ nombre +" con exito")
        return redirect(self.get_success_url())

@login_required(redirect_field_name='/ingresar')
class OtroDocumentoAsociadoView(View):
    
    login_url = '/ingresar/'
    template_name = 'otro_documento_asociado_view.html'
    model = OtroDocumentoAsociado
    
    def get_context_data(self, **kwargs) :
        context = super(OtroDocumentoAsociado, self).get_context(**kwargs)
        otroDocumentoAsociado = OtroDocumentoAsociado.objects.all()
        context['otroDocumentoAsociado'] = otroDocumentoAsociado
        return context

@login_required(redirect_field_name='/ingresar')    
class OtroDocumentoAsociadoCreateView(UserPassesTestMixin,CreateView):
    
    login_url = '/ingresar'
    template_name = 'otro_documento_asociado_form.html'
    form_class = OtroDocumentoAsociadoForm
    
    def get_success_url(self):
        p = self.kwargs
        id = p.get("pk")
        return reverse_lazy('otroDocumentoDetailView', kwargs={'pk': id})
    
    def form_valid(self, form):
        return super().form_valid(form)
    

@login_required(redirect_field_name='/ingresar')
class OtroDocumentoAsociadoUpdateView(UserPassesTestMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'otro_documento_asociado_form.html'
    form_class = OtroDocumentoAsociadoForm
    
    def get_success_url(self):
        p = self.kwargs
        id = p.get("pk")
        return reverse_lazy('otroDocumentoDetailView', kwargs={'pk': id})
    
    def form_valid(self, form):
        return super().form_valid(form)

@login_required(redirect_field_name='/ingresar')
class CuerpoDocumentoView(View):
    
    login_url = '/ingresar/'
    template_name = 'cuerpo_documento_view.html'
    model = CuerpoDocumento
    
    def get_context_data(self, **kwargs) :
        context = super(CuerpoDocumento, self).get_context(**kwargs)
        cuerpoDocumento = CuerpoDocumento.objects.all()
        context['cuerpoDocumento'] = cuerpoDocumento
        return context

@login_required(redirect_field_name='/ingresar')    
class CuerpoDocumentoCreateView(UserPassesTestMixin,CreateView):
    
    login_url = '/ingresar'
    template_name = 'cuerpo_documento_form.html'
    form_class = CuerpoDocumentoForm
    
    def get_success_url(self):
        p = self.kwargs
        id = p.get("pk")
        return reverse_lazy('cuerpoDocumentoDetailView', kwargs={'pk': id})
    
    def form_valid(self, form):
        return super().form_valid(form)

@login_required(redirect_field_name='/ingresar')
class CuerpoDocumentoUpdateView(UserPassesTestMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'cuerpo_documento_form.html'
    form_class = CuerpoDocumentoForm
    model = CuerpoDocumento
    
    def get_success_url(self):
        p = self.kwargs
        id = p.get("pk")
        return reverse_lazy('cuerpoDocumentoDetailView', kwargs={'pk': id})
    
    def form_valid(self, form):
        return super().form_valid(form)

@login_required(redirect_field_name='/ingresar')
class PagoDonacionView(View):
    
    login_url = '/ingresar/'
    template_name = 'pago_donacion_view.html'
    model = PagoDonacion
    
    def get_context_data(self, **kwargs) :
        context = super(PagoDonacion, self).get_context(**kwargs)
        pagoDonacion = PagoDonacion.objects.all()
        context['pagoDonacion'] = PagoDonacion
        return context

@login_required(redirect_field_name='/ingresar')    
class PagoDonacionCreateView(UserPassesTestMixin,CreateView):
    
    login_url = '/ingresar'
    template_name = 'pago_donacion_form.html'
    form_class = PagoDonacionForm
    model = PagoDonacion
    
    def get_success_url(self):
        return reverse_lazy('pagoDonacionList')
    
    def post(self, request, *args, **kwargs):
        pk=self.kwargs.get("pk")
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a creado un pago a donacion con exito")
        return redirect('pagoDonacionList')

@login_required(redirect_field_name='/ingresar')
class PagoDonacionUpdateView(UserPassesTestMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'pago_donacion_form.html'
    form_class = PagoDonacionForm
    model = PagoDonacion
    
    def get_success_url(self):
        return reverse_lazy('pagoDonacionList')

    def post(self, request, *args, **kwargs):
        pk=self.kwargs.get("pk")
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a actualizado un pago a donacion con exito")
        return redirect('pagoDonacionList')