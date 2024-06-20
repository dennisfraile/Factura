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
        id = self.kwargs.get('pk')
        if id:
            return redirect('municipioUpdate',id)
        else:
            return redirect('municipioCreate')
        

    def post(self, request, *args, **kwargs):
        pk=self.kwargs.get("pk")
        codigo = request.POST.get("codigo")
        valor = request.POST.get("valor")
        Departamento.objects.filter(pk=pk).update(codigo=codigo, valor=valor)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a actualizado el departamento: "+ codigo + " " + valor + "con exito")
        return redirect(self.get_success_url())

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
        id = self.kwargs.get('pk')
        if id:
            return redirect('direccionUpdate',id)
        else:
            return redirect('direccionCreate')
    
    def post(self, request, *args, **kwargs):
        pk=self.kwargs.get("pk")
        codigo = request.POST.get("codigo")
        valor = request.POST.get("valor")
        departamentoId = request.POST.get("departamento")
        departamento = Departamento.objects.get(id=departamentoId)
        municipio= Municipio.objects.create(codigo=codigo, valor=valor, departamento=departamento)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a creado el municipio: "+ codigo + " " + valor + "con exito")
        return redirect(self.get_success_url())

@login_required(redirect_field_name='/ingresar')
class MunicipioUpdateView(UserPassesTestMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'municipio_form.html'
    form_class = MunicipioForm
    
    def get_success_url(self):
        id = self.kwargs.get('pk')
        if id:
            return redirect('direccionUpdate',id)
        else:
            return redirect('direccionCreate')

    def post(self, request, *args, **kwargs):
        pk=self.kwargs.get("pk")
        codigo = request.POST.get("codigo")
        valor = request.POST.get("valor")
        departamentoId = request.POST.get("departamento")
        departamento = Departamento.objects.get(id=departamentoId)
        Municipio.objects.filter(pk=pk).update(codigo=codigo, valor=valor, departamento=departamento)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a actualizado el municipio: "+ codigo + " " + valor + "con exito")
        return redirect(self.get_success_url())

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
        return redirect(self.get_success_url())

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
        Direccion.objects.filter(pk=pk).update(complementoDireccion=complementoDireccion, municipio=municipio)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a actualizado la direccion: "+ complementoDireccion + " " + "con exito")
        return redirect(self.get_success_url())

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
        origin = self.request.POST.get('origin')
        if origin == 'operacionsujetoexcluido':
            operacionSujetoExcluido_id = self.request.POST.get('operacionSujetoExcluido')
            if operacionSujetoExcluido_id:
                return redirect('operacionSujetoExcluidoUpdate', pk=operacionSujetoExcluido_id)
            else:
                return redirect('operacionSujetoExcluidoCreate')
        elif origin == 'cuerpodocumento':
            cuerpoDocumento_id = self.request.POST.get('cuerpoDocumento')
            if cuerpoDocumento_id:
                return redirect('cuerpoDocumentoUpdate', pk=cuerpoDocumento_id)
            else:
                return redirect('cuerpoDocumentoCreate')
        else:
            return redirect('panel_facturas')
    
    def post(self, request, *args, **kwargs):
        pk=self.kwargs.get("pk")
        codigo = request.POST.get("codigo")
        valor = request.POST.get("valor")
        unidadMedida= UnidadMedida.objects.create(codigo=codigo, valor=valor)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a creado la unidad de medida: "+ codigo + " " + valor + "con exito")
        return redirect(self.get_success_url())

@login_required(redirect_field_name='/ingresar')
class UnidadMedidaUpdateView(UserPassesTestMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'unidad_medida_form.html'
    form_class = UnidadMedidaForm
    
    def get_success_url(self):
        origin = self.request.POST.get('origin')
        if origin == 'operacionsujetoexcluido':
            operacionSujetoExcluido_id = self.request.POST.get('operacionSujetoExcluido')
            if operacionSujetoExcluido_id:
                return redirect('operacionSujetoExcluidoUpdate', pk=operacionSujetoExcluido_id)
            else:
                return redirect('operacionSujetoExcluidoCreate')
        elif origin == 'cuerpodocumento':
            cuerpoDocumento_id = self.request.POST.get('cuerpoDocumento')
            if cuerpoDocumento_id:
                return redirect('cuerpoDocumentoUpdate', pk=cuerpoDocumento_id)
            else:
                return redirect('cuerpoDocumentoCreate')
        else:
            return redirect('panel_facturas')

    def post(self, request, *args, **kwargs):
        pk=self.kwargs.get("pk")
        codigo = request.POST.get("codigo")
        valor = request.POST.get("valor")
        UnidadMedida.objects.filter(pk=pk).update(codigo=codigo, valor=valor)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a actualizado la unidad de medida: "+ codigo + " " + valor + "con exito")
        return redirect(self.get_success_url())

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
        pk=self.kwargs.get("pk")
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
        operacion = OperacionesSujetoExcluido.objects.filter(pk=pk).update(numItem=numItem, codigo=codigo, uniMedida=unidadMedida, cantidad=cantidad, 
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
        receptor = get_object_or_404(Receptor, id=receptorId)
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
        id=self.kwargs.get("pk")
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
        sujetoExcluido = SujetoExcluido.objects.filter(pk=id).update(identificador=identificador,emisor=emisor,receptor=receptor,totalCompra=totalCompra,descu=descu,
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
        origin = self.request.POST.get('origin')
        id = self.kwargs.get('id')
        if origin == 'sujetoExclido':
            factura = sujetoExcluidoList(id)
        else:
            factura = comprobanteDonacionList(id)
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
        origin = self.request.POST.get('origin')
        if origin == 'sujetoExcluido':
            sujetoExcluido = get_object_or_404(SujetoExcluido, pk=id)
            idIdentificador = sujetoExcluido.identificador.id
            identificador = get_object_or_404(Identificador, pk=idIdentificador)
        else:
            comprobanteDonacion = get_object_or_404(ComprobanteDonacion, pk=id)
            idIdentificador = comprobanteDonacion.identificador.id
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
                if origin == 'sujetoExcluido':  
                    responseHacienda = ResponseHacienda.objects.create(nombre="Auth de Hacienda", datosJason=acesso, sujetoExcluido=sujetoExcluido)
                else:
                    responseHacienda = ResponseHacienda.objects.create(nombre="Auth de Hacienda", datosJason=acesso, comprobanteDonacion=comprobanteDonacion)
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
                        'codigoGeneracion': identificador.codigoGeneracion,
                    }
                    try:
                        transmitir = requests.post(url_recepcion, params=parametros_recepcion).json()
                        if origin == 'sujetoExcluido':
                            responseHacienda = ResponseHacienda.objects.create(nombre="Transmicion de factura a  Hacienda", datosJason=transmitir, sujetoExcluido=sujetoExcluido)
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
                        else:
                            responseHacienda = ResponseHacienda.objects.create(nombre="Transmicion de factura a  Hacienda", datosJason=transmitir, comprobanteDonacion=comprobanteDonacion)
                            responseHacienda.save()
                            if(transmitir['codigoMsg']=="001"):
                                comprobanteDonacion.objects.update(transmitido=True)
                                # Envía un correo electrónico con la factura Electrnica
                                subject = 'Comprobante de Donacion'
                                body = f'Hola {comprobanteDonacion.receptor.nombre},\n\nse le a emitido un Comprobante de Donacion'
                                from_email = comprobanteDonacion.emisor.email  
                                to_email = comprobanteDonacion.receptor.email
                                email =  EmailMessage(subject, body, from_email, to_email)
                                jsonContent = json.dumps(jsonData, indent=4)
                                email.attach('data.json', jsonContent, 'application/json')
                                email.attach('data.pdf', pdf, 'application/pdf')
                                email.send()
                    except:
                        messages.danger(self.request, 'Ocurrio un problema en la transmision de la factura' + transmitir['status'])
                    stastus_code = acesso['status']
                    messages.success(self.request, 'Se logueo con exito en hacienda', stastus_code)
                    if origin == 'sujetoExcluido':
                        return redirect(reverse_lazy('sujetoExcluidoDetailView', kwargs={'pk':id}))
                    else:
                         return redirect(reverse_lazy('comprobanteDonacionDetailView', kwargs={'pk':id}))
                
                else:
                    stastus_code = acesso.status_code
                    messages.success(self.request, 'Ocurrio un error con las credenciales' + acesso['status'])
                    return redirect('authHacienda', pk=authHacienda.pk)
                
            except requests.exceptions.RequestException as e:
                messages.success(self.request, 'Ocurrio un error al hacer la solicitud a la api de hacienda ' + str(e))
            if origin == 'sujetoExcluido':
                return redirect(reverse_lazy('sujetoExcluidoDetailView', kwargs={'pk':id}))
            else:
                return redirect(reverse_lazy('comprobanteDonacionDetailView', kwargs={'pk':id}))
        else:
            messages.success(self.request, 'Error esta vista solo admite solicitudes POST, error 405')
            if origin == 'sujetoExcluido':
                return redirect(reverse_lazy('sujetoExcluidoDetailView', kwargs={'pk':id}))
            else:
                return redirect(reverse_lazy('comprobanteDonacionDetailView', kwargs={'pk':id}))
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
        return redirect(self.get_success_url())

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
        FormaPago.objects.filter(pk=id).update(codigo=codigo, valor=valor)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a actualizado la forma de pago: "+ codigo + " " + valor + "con exito")
        return redirect(self.get_success_url())

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
        id=self.kwargs.get("pk")
        if id:
            return redirect('sujetoExcluidoUpdate',id)
        else:
            return redirect('sujetoExcluidoCreate')
    
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
        return redirect(self.get_success_url())

@login_required(redirect_field_name='/ingresar')
class PagoUpdateView(UserPassesTestMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'pago_form.html'
    form_class = PagoForm
    
    def get_success_url(self):
        id=self.kwargs.get("pk")
        if id:
            return redirect('sujetoExcluidoUpdate',id)
        else:
            return redirect('sujetoExcluidoCreate')

    def post(self, request, *args, **kwargs):
        pk=self.kwargs.get("pk")
        codigo = request.POST.get("codigo")
        formaPagoId = request.POST.get("formaPago")
        formaPago = FormaPago.objects.get(id=formaPagoId)
        montoPago = request.POS.get("montoPago")
        referencia = request.POST.get("referencia")
        plazo = request.POST.get("plazo")
        periodo = request.POST.get("periodo")
        Pago.objects.filter(pk=pk).update(codigo=codigo, formaPago=formaPago, montoPago=montoPago, referencia=referencia, plazo=plazo, periodo=periodo)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a actualizado el pago: "+ codigo + " " + "con exito")
        return redirect(self.get_success_url())

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
        id=self.kwargs.get("pk")
        origin = self.request.POST.get('origin')
        if origin == 'sujetoExcluido':
            return redirect('sujetoExcluidoDetailView', pk=id)
        elif origin == 'comprobanteDonacion':
            return redirect('comprobanteDonacionDetailView', pk=id)
            
    
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
        return redirect(self.get_success_url())

@login_required(redirect_field_name='/ingresar')
class ApendiceUpdateView(UserPassesTestMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'apendice_form.html'
    form_class = ApendiceForm
    
    def get_success_url(self):
        id=self.kwargs.get("pk")
        origin = self.request.POST.get('origin')
        if origin == 'sujetoExcluido':
            return redirect('sujetoExcluidoDetailView', pk=id)
        elif origin == 'comprobanteDonacion':
            return redirect('comprobanteDonacionDetailView', pk=id)
        

    def post(self, request, *args, **kwargs):
        id=self.kwargs.get("pk")
        campo = request.POST.get("campo")
        etiqueta = request.POST.get("etiqueta")
        valor = request.POST.get("valor")
        Apendice.objects.filter(pk=id).update(campo=campo, etiqueta=etiqueta, valor=valor)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a actualizado el apendice: "+ campo + " " + valor + "con exito")
        return redirect(self.get_success_url())

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
        id=self.kwargs.get("pk")
        if id:
            return redirect('identifacadorUpdate',id)
        else:
            return redirect('identificadorCreate')
        
    
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
        id=self.kwargs.get("pk")
        if id:
            return redirect('identifacadorUpdate',id)
        else:
            return redirect('identificadorCreate')

    def post(self, request, *args, **kwargs):
        pk=self.kwargs.get("pk")
        codigo = request.POST.get("codigo")
        valor = request.POST.get("valor")
        TipoDocumento.objects.filter(pk=id).update(codigo=codigo, valor=valor)
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
            return redirect('panel_facturas')
    
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
        return redirect(self.get_success_url())

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
            return redirect('panel_facturas')

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
        Identificador.objects.filter(pk=pk).update(version=version, ambiente=ambiente, tipoDte=tipoDte, numeroControl=numeroControl,codigoGeneracion=codigoGeneracion, 
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
            return redirect('panel_facturas')
    
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
            return redirect('panel_facturas')

    def post(self, request, *args, **kwargs):
        id=self.kwargs.get("pk")
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
        receptor = Receptor.objects.filter(id=id).update(tipo=tipo, homologado=homologado, numero=numero,nombre=nombre,actividadEconomica=actividadEconomica,
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
        return reverse_lazy('comprobanteDonacionDetailView', kwargs={'pk': id})
    
    def post(self, request, *args, **kwargs):
        id=self.kwargs.get("pk")
        codDocAsociado = request.POST.get('codDocAsociado')
        descDocumento = request.POST.get('descDocumento')
        detalleDocumento = request.POST.get('detalleDocumento')
        user = request.user
        entidad = user.Usuarios.all()
        comprobanteDonacion = get_object_or_404(ComprobanteDonacion, pk=id)
        otroDocumentoAsociado = OtroDocumentoAsociado.objects.create(codDocAsociado=codDocAsociado, descDocumento=descDocumento, detalleDocumento=detalleDocumento,
                                                                     comprobanteDonacion=comprobanteDonacion,entidad=entidad)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a creado un nuevo comprobante de donacion con exito con exito")
        return redirect(self.get_success_url())
    

@login_required(redirect_field_name='/ingresar')
class OtroDocumentoAsociadoUpdateView(UserPassesTestMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'otro_documento_asociado_form.html'
    form_class = OtroDocumentoAsociadoForm
    
    def get_success_url(self):
        p = self.kwargs
        id = p.get("pk")
        return reverse_lazy('comprobanteDonacionDetailView', kwargs={'pk': id})
    
    def post(self, request, *args, **kwargs):
        id=self.kwargs.get("pk")
        codDocAsociado = request.POST.get('codDocAsociado')
        descDocumento = request.POST.get('descDocumento')
        detalleDocumento = request.POST.get('detalleDocumento')
        otroDocumentoAsociado = OtroDocumentoAsociado.objects.filter(id=id).update(codDocAsociado=codDocAsociado, descDocumento=descDocumento, detalleDocumento=detalleDocumento)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a actualizado el comprobante de donacion con exito con exito")
        return redirect(self.get_success_url())

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
        return reverse_lazy('comprobanteDonacionDetailView', kwargs={'pk': id})
    
    def post(self, request, *args, **kwargs):
        id=self.kwargs.get("pk")
        numItem = request.POST.get('numItem')
        tipoDonacion = request.POST.get('tipoDonacion')
        cantidad = request.POST.get('cantidad')
        codigo = request.POST.get('codigo')
        unidadMedidaId = request.POST.get('unidadMedida')
        unidadMedida = get_object_or_404(UnidadMedida, id=unidadMedidaId)
        descripccion = request.POST.get('descripccion')
        depreciacion = request.POST.get('depreciacion')
        montoDescu = request.POST.get('montoDescu')
        valorUni = request.POST.get('valorUni')
        valor = request.POST.get('valor')
        user = request.user
        entidad = user.Usuarios.all()
        comprobanteDonacion = get_object_or_404(ComprobanteDonacion, pk=id)
        cuerpoDocumento = CuerpoDocumento.objects.create(numItem=numItem, tipoDonacion=tipoDonacion, cantidad=cantidad, codigo=codigo,
                                                         uniMedida=unidadMedida, descripccion=descripccion, depreciacion=depreciacion,
                                                         montoDescu=montoDescu, valorUni=valorUni, valor=valor, entidad=entidad, comprobanteDonacion=comprobanteDonacion)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a creado el cuerpo del documento con exito")
        return redirect(self.get_success_url())

@login_required(redirect_field_name='/ingresar')
class CuerpoDocumentoUpdateView(UserPassesTestMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'cuerpo_documento_form.html'
    form_class = CuerpoDocumentoForm
    model = CuerpoDocumento
    
    def get_success_url(self):
        p = self.kwargs
        id = p.get("pk")
        return reverse_lazy('comprobanteDonacionDetailView', kwargs={'pk': id})
    
    def post(self, request, *args, **kwargs):
        id = self.kwargs['pk']
        numItem = request.POST.get('numItem')
        tipoDonacion = request.POST.get('tipoDonacion')
        cantidad = request.POST.get('cantidad')
        codigo = request.POST.get('codigo')
        unidadMedidaId = request.POST.get('unidadMedida')
        unidadMedida = get_object_or_404(UnidadMedida, id=unidadMedidaId)
        descripccion = request.POST.get('descripccion')
        depreciacion = request.POST.get('depreciacion')
        montoDescu = request.POST.get('montoDescu')
        valorUni = request.POST.get('valorUni')
        valor = request.POST.get('valor')
        cuerpoDocumento = CuerpoDocumento.objects.filter(id=id).update(numItem=numItem, tipoDonacion=tipoDonacion, cantidad=cantidad, codigo=codigo,
                                                         uniMedida=unidadMedida, descripccion=descripccion, depreciacion=depreciacion,
                                                         montoDescu=montoDescu, valorUni=valorUni, valor=valor)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a actualizado el cuerpo del documento con exito")
        return redirect(self.get_success_url())

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
        id=self.kwargs.get("pk")
        return reverse_lazy('comprobanteDonacionDetailView', kwargs={'pk': id})
    
    def post(self, request, *args, **kwargs):
        pk=self.kwargs.get("pk")
        codigo = request.POST.get('codido')
        montoPago = request.POST.get('montoPago')
        referencia = request.POST.get('referencia')
        user = request.user
        entidad = user.Usuarios.all()
        pagoDonacion = PagoDonacion.objects.create(codigo=codigo, montoPago=montoPago, referencia=referencia,entidad=entidad)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a creado un pago a donacion con exito")
        return redirect(self.get_success_url())

@login_required(redirect_field_name='/ingresar')
class PagoDonacionUpdateView(UserPassesTestMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'pago_donacion_form.html'
    form_class = PagoDonacionForm
    model = PagoDonacion
    
    def get_success_url(self):
        return reverse_lazy('comprobanteDonacionDetailView', kwargs={'pk': id})

    def post(self, request, *args, **kwargs):
        id = self.kwargs['pk']
        codigo = request.POST.get('codido')
        montoPago = request.POST.get('montoPago')
        referencia = request.POST.get('referencia')
        pagoDonacion = PagoDonacion.objects.filter(id=id).update(codigo=codigo, montoPago=montoPago, referencia=referencia)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a actualizado un pago a donacion con exito")
        return redirect(self.get_success_url())

@login_required(redirect_field_name='/ingresar')
class ComprobanteDonacionMonthView(MonthArchiveView):
    """Muestra la lista de sujetos excluidos por mes"""

    login_url='/ingresar/'
    data_field = "fechaTransmicion"
    template_name='comprobante_donacion_month.html'
    allow_empty = True
    allow_future = True

    def get_context_data(self, **kwargs) :
        context = super(ComprobanteDonacionMonthView, self).get_context(**kwargs)
        comprobante = ComprobanteDonacion.objects.all()
        context['registro'] = comprobante
        return context

@login_required(redirect_field_name='/ingresar')
class ComprobanteDonacionDetailView(DetailView):
    """Muestra los datos de un comprobante de donacion en especifico"""

    login_url = '/ingresar/'
    template_name = 'comprobante_donacion_by_id_view.html'
    model = ComprobanteDonacion

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comprobanteDonacion = ComprobanteDonacion.objects.filter(id=context['object'].id)
        otroDocumentoAsociado = OtroDocumentoAsociado.objects.filter(id=comprobanteDonacion.id) 
        cuerpoDocumento = CuerpoDocumento.objects.filter(id=comprobanteDonacion.id)
        apendice = Apendice.objects.filter(comprobanteDonacion=comprobanteDonacion)
        context['comprobanteDonacion'] = comprobanteDonacion
        context['otroDocumentoAsociado'] = otroDocumentoAsociado
        context['cuerpoDocumento'] = cuerpoDocumento
        context['apendice'] = apendice
        context['show'] = True
        return context   

@login_required(redirect_field_name='/ingresar')
class ComprobanteDonacionCreateView(UserPassesTestMixin, CreateView):
    
    login_url = '/ingresar/'
    template_name = 'comprobante donacion/comprobante_donacion_create_view.html'
    model = ComprobanteDonacion
    
    def get_success_url(self):
        current_date = datetime.datetime.now()
        mes = current_date.month
        año = current_date.year
        return reverse_lazy('comprobanteDonacionMonthView', kwargs={'year':año, 'month':mes})
    
    def post(self, request, *args, **kwargs):
        identificadorId = request.POST.get('identificador')
        identificador = get_object_or_404(Identificador, id=identificadorId)
        entidadId = request.POST.get('emisor')
        emisor = get_object_or_404(Entidad, id=entidadId)
        receptorId = request.POST.get('receptor')
        receptor = get_object_or_404(Receptor, id=receptorId)
        codDomicilio = request.POST.get('codDomicilio')
        valorTotal = request.POST.get('valorTotal')
        totalLetras = request.POST.get('totalLetras')
        pagoDonacionId = request.POST.get('pago')
        pagoDonacion = get_object_or_404(PagoDonacion, pagoDonacionId)
        user = request.user
        entidad = user.Usuarios.all()
        pagoDonacion = PagoDonacion.objects.create(identificador=identificador,emisor=emisor,receptor=receptor,codDomicilio=codDomicilio,valorTotal=valorTotal,totalLetras=totalLetras,
                                                       pagoDonacion=pagoDonacion,entidad=entidad)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a creado el comprobante de donacion con exito")
        return redirect(self.get_success_url())
        

@login_required(redirect_field_name='/ingresar')
class ComprobanteDonacionUpdateView(UserPassesTestMixin, UpdateView):
    
    login_url = '/ingresar/'
    model = SujetoExcluido
    template_name = 'sujeto excluido/sujeto_excluido_create_view.html'    
    
    def get_success_url(self):
        current_date = datetime.datetime.now()
        mes = current_date.month
        año = current_date.year
        return reverse_lazy('comprobanteDonacionMonthView', kwargs={'year':año, 'month':mes})
    
    def post(self, request):
        id = self.kwargs['pk']
        identificadorId = request.POST.get('identificador')
        identificador = get_object_or_404(Identificador, id=identificadorId)
        entidadId = request.POST.get('emisor')
        emisor = get_object_or_404(Entidad, id=entidadId)
        receptorId = request.POST.get('receptor')
        receptor = get_object_or_404(Receptor, id=receptorId)
        codDomicilio = request.POST.get('codDomicilio')
        valorTotal = request.POST.get('valorTotal')
        totalLetras = request.POST.get('totalLetras')
        pagoDonacionId = request.POST.get('pago')
        pagoDonacion = get_object_or_404(PagoDonacion, pagoDonacionId)
        pagoDonacion = PagoDonacion.objects.filter(id=id).update(identificador=identificador,emisor=emisor,receptor=receptor,codDomicilio=codDomicilio,valorTotal=valorTotal,totalLetras=totalLetras,
                                                       pagoDonacion=pagoDonacion)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a actualizado el comprobante de donacion con exito")
        return redirect(self.get_success_url())

def comprobanteDonacionList(self,id):
    comprobanteDonacion = ComprobanteDonacion.objects.get(id=id)
    emisor = User.objects.get(id = comprobanteDonacion.emisor.emisor.id)
    documentoEmisor = emisor.documentos.all()
    entidad = emisor.Usuarios.all()
    receptor = User.objects.get(id=comprobanteDonacion.receptor.receptor.id)
    documentoReceptor = receptor.documentos.all()
    otroDocumentoAsociado = OtroDocumentoAsociado.otrosDocumentos.all()
    cuerpoDocumento = CuerpoDocumento.cuerpoDocumentos.all()
    apendiceComprobanteDonacion = comprobanteDonacion.apendicesDonacion.all()
    fechaEmi = comprobanteDonacion.fechaTransmicion.date()
    horaEmi = comprobanteDonacion.fechaTransmicion.get_formatted_time()
    comprobanteData = []
    
    comprobanteData = {
        'identificacion': {
            'version': comprobanteDonacion.identificador.version,
            'ambiente': comprobanteDonacion.identificador.ambiente,
            'tipoDte': comprobanteDonacion.identificador.tipoDte,
            'numeroControl': comprobanteDonacion.identificador.numeroControl,
            'codigoGeneracion': comprobanteDonacion.identificador.codigoGeneracion,
            'tipoModelo': comprobanteDonacion.identificador.tipoModelo,
            'tipoOperacion': comprobanteDonacion.identificador.tipoOperacion,
            'fechaEmi': fechaEmi,
            'horaEmi': horaEmi,
            'tipoMoneda': comprobanteDonacion.identificador.tipoMoneda
        },
        'donatorio': {
            "tipoDocumento":"nit",
            "numDocumento": comprobanteDonacion.emisor.nit,
            "nrc": comprobanteDonacion.emisor.nrc,
            "nombre": comprobanteDonacion.emisor.razonSocial,
            "codActividad": comprobanteDonacion.emisor.actividadEconomica.codigo,
            "descActividad": comprobanteDonacion.emisor.actividadEconomica.valor,
            "direccion": {
                "departamento": comprobanteDonacion.emisor.direccionEmisor.municipio.departamento.codigo,
                "municipio": comprobanteDonacion.emisor.direccionEmisor.municipio.codigo,
                "complemento": comprobanteDonacion.emisor.direccionEmisor.complementoDireccion,
            },
            "telefono": comprobanteDonacion.emisor.cellphone,
            "correo": comprobanteDonacion.emisor.email,
            "codEstableMH": comprobanteDonacion.emisor.codEstableMH,
            "codEstable": comprobanteDonacion.emisor.codEstable,
            "codPuntoVentaMH": comprobanteDonacion.emisor.codPuntoVentaMH,
            "codPuntoVenta": comprobanteDonacion.emisor.codPuntoVenta,
            
        },
        "donante": {
            "tipoDocumento": comprobanteDonacion.receptor.tipo,
            "numDocumento": comprobanteDonacion.receptor.numero,
            "nrc":comprobanteDonacion.receptor.nrc,
            "nombre": comprobanteDonacion.receptor.receptor.nombre,
            "codActividad": comprobanteDonacion.receptor.actividadEconomica.codigo,
            "descActividad": comprobanteDonacion.receptor.actividadEconomica.valor,
            "direccion": {
                "departamento": comprobanteDonacion.receptor.direccionReceptor.municipio.departamento.codigo,
                "municipio": comprobanteDonacion.receptor.direccionReceptor.municipio.codigo,
                "complemento": comprobanteDonacion.receptor.direccionReceptor.complementoDireccion
            },
            "telefono": comprobanteDonacion.receptor.cellphone,
            "correo": comprobanteDonacion.receptor.email,
            "codDomiciliado": comprobanteDonacion.codDomiciliado,
            "codPais": comprobanteDonacion.codPais,
        },
        "otrosDocumentos":[],
        "cuerpoDocumento":[],
        "resumen": {
            "valorTotal" : comprobanteDonacion.valorTotal,
            "totalLetras" : comprobanteDonacion.totalLetras,
            "pagos" : [
                {
                    "codigo" : comprobanteDonacion.pago.codigo,
                    "montoPago" : comprobanteDonacion.pago.montoPago,
                    "referencia" : comprobanteDonacion.pago.referencia,
                }
            ],
        },
        "apendice": []
    }
    for otroDocumento in otroDocumentoAsociado:
        otrosDocumentosData = {
            "codDocAsociado" : otroDocumento.codDocAsociado,
            "descDocumento" : otroDocumento.descDocumento,
            "detalleDocumento" : otroDocumento.detalleDocumento,
        }
        comprobanteData['otrosDocumentos'].append(otrosDocumentosData)
    
    for cuerpoDocumento in cuerpoDocumento:
        cuerpoDocumentoData = {
            "numItem": cuerpoDocumento.numItem,
            "tipoDonacion": cuerpoDocumento.tipoDonacion,
            "cantidad": cuerpoDocumento.cantidad,
            "codigo": cuerpoDocumento.codigo,
            "uniMedida": cuerpoDocumento.uniMedida.codigo,
            "descripccion": cuerpoDocumento.descripccion,
            "depreciacion": cuerpoDocumento.depreciacion,
            "montoDescu": cuerpoDocumento.montoDescu,
            "valorUni": cuerpoDocumento.valorUni,
            "valor": cuerpoDocumento.valor
        }
        comprobanteData['cuerpoDocumento'].append(cuerpoDocumentoData)
    
    for apendices in apendiceComprobanteDonacion:
        apendicesData = {
            "campo": apendices.campo,
            "etiquta": apendices.etiquta,
            "valor": apendices.valor
        }
        comprobanteData['apendice'].append(apendicesData)
    
    return JsonResponse(comprobanteData, safe=False)