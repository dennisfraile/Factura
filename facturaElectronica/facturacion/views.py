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
from io import BytesIO
from email.mime.application import MIMEApplication
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from decimal import Decimal
from uuid import UUID
import datetime
from django.http import HttpResponseRedirect
import base64
# Create your views here.

@login_required(redirect_field_name='/ingresar')
def get_opercionSujetoExcluido(request):
    operacionesSujetoExccluido = OperacionesSujetoExcluido.objects.all()
    return JsonResponse(list(operacionesSujetoExccluido), safe = False)

class IndexView(LoginRequiredMixin,TemplateView):
    template_name = 'index_factura.html'
    
   
    
class PaisView(LoginRequiredMixin,View):
    
    login_url = '/ingresar/'
    template_name = 'pais_view.html'
    model = Pais
    
    def get_context_data(self, **kwargs) :
        context = super(Pais, self).get_context(**kwargs)
        pais = Pais.objects.all()
        context['registro'] = pais
        return context
    
class PaisCreateView(LoginRequiredMixin,CreateView):
    
    login_url = '/ingresar'
    template_name = 'forms comunes/pais_form.html'
    form_class = PaisForm
    model = Pais
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')
    

class PaisUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'forms comunes/pais_form.html'
    form_class = PaisForm
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')


class DepartamentoView(LoginRequiredMixin,View):
    
    login_url = '/ingresar/'
    template_name = 'departamento_view.html'
    model = Departamento
    
    def get_context_data(self, **kwargs) :
        context = super(Departamento, self).get_context(**kwargs)
        departamento = Departamento.objects.all()
        context['registro'] = departamento
        return context
   
class DepartamentoCreateView(LoginRequiredMixin,CreateView):
    
    login_url = '/ingresar'
    template_name = 'forms comunes/departamento_form.html'
    form_class = DepartamentoForm
    model = Departamento
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')
    

class DepartamentoUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'forms comunes/departamento_form.html'
    form_class = DepartamentoForm
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')   

    

class MunicipioView(LoginRequiredMixin,View):
    
    login_url = '/ingresar/'
    template_name = 'municipio_view.html'
    model = Municipio
    
    def get_context_data(self, **kwargs) :
        context = super(Municipio, self).get_context(**kwargs)
        municipio = Municipio.objects.all()
        context['registro'] = municipio
        return context
    
class MunicipioCreateView(LoginRequiredMixin,CreateView):
    
    login_url = '/ingresar'
    template_name = 'forms comunes/municipio_form.html'
    form_class = MunicipioForm
    model = Municipio
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')
    
    def get_initial(self):
        initial = super().get_initial()
        initial['departamento'] = self.request.GET.get('departamento')
        return initial
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['departamento_id'] = self.request.GET.get('departamento')
        return context
    
    

class MunicipioUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'forms comunes/municipio_form.html'
    form_class = MunicipioForm
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['departamento_id'] = self.get_object().departamento.id if self.get_object().departamento else None
        return context



class DireccionView(LoginRequiredMixin,View):
    
    login_url = '/ingresar/'
    template_name = 'direccion_view.html'
    model = Direccion
    
    def get_context_data(self, **kwargs) :
        context = super(Direccion, self).get_context(**kwargs)
        direccion = Direccion.objects.all()
        context['registro'] = direccion
        return context
    
class DireccionCreateView(LoginRequiredMixin,CreateView):
    
    login_url = '/ingresar'
    template_name = 'forms comunes/direccion_form.html'
    form_class = DireccionForm
    model = Direccion
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')    
    
    
    def get_initial(self):
        initial = super().get_initial()
        initial['municipio'] = self.request.GET.get('municipio')
        return initial
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['municipio_id'] = self.request.GET.get('municipio')
        return context
    
    def form_valid(self, form):
        direccion = form.save(commit=False) 
        direccion.entidad = self.request.user.entidad      
        direccion.save()
        messages.add_message(request=self.request, level=messages.SUCCESS, message= "Se a creado la direccion: con exito")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))
    
    

class DireccionUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'forms comunes/direccion_form.html'
    form_class = DireccionForm
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['municipio_id'] = self.get_object().municipio.id if self.get_object().municipio else None
        return context

    def form_valid(self, form):
        direccion = form.save(commit=False) 
        direccion.entidad = self.request.user.entidad       
        direccion.save()
        messages.add_message(request=self.request, level=messages.SUCCESS, message= "Se a creado la direccion: con exito")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))

class UnidadMedidaView(LoginRequiredMixin,View):
    
    login_url = '/ingresar/'
    template_name = 'unidad_medida_view.html'
    model = UnidadMedida
    
    def get_context_data(self, **kwargs) :
        context = super(UnidadMedida, self).get_context(**kwargs)
        unidadMedida = UnidadMedida.objects.all()
        context['registro'] = unidadMedida
        return context
   
class UnidadMedidaCreateView(LoginRequiredMixin,CreateView):
    
    login_url = '/ingresar'
    template_name = 'forms comunes/unidad_medida_form.html'
    form_class = UnidadMedidaForm
    model = UnidadMedida
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')
    

class UnidadMedidaUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'forms comunes/unidad_medida_form.html'
    form_class = UnidadMedidaForm
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')


class OperacionSujetoExcluidoView(LoginRequiredMixin,View):
    
    login_url = '/ingresar'
    template_name = 'operacion_sujeto_exluido_view.html'
    model = OperacionesSujetoExcluido
    
    def get_context_data(self, **kwargs) :
        context = super(OperacionesSujetoExcluido, self).get_context(**kwargs)
        operacionesSujetoExcluido = OperacionesSujetoExcluido.objects.all()
        context['registro'] = operacionesSujetoExcluido
        return context

class OperacionSujetoExcluidoCreateView(LoginRequiredMixin, CreateView):
    
    login_url = '/ingresar'
    template_name = 'sujeto excluido/operacion_sujeto_excluido_form.html'
    form_class = OperacionesSujetoExcluidoForm
    model = OperacionesSujetoExcluido
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['usuario'] = self.request.user
        return kwargs
    
    def get_initial(self):
        initial = super().get_initial()
        initial['unidadMedida'] = self.request.GET.get('unidadMedida')
        return initial
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['unidadMedida_id'] = self.request.GET.get('unidadMedida')
        return context
    
    def form_valid(self, form):
        operacion = form.save(commit=False) 
        id=self.kwargs.get("id")
        sujetoExcluido = get_object_or_404(SujetoExcluido, pk=id)
        operacion.entidad = self.request.user.entidad
        operacion.sujetoExcluido = sujetoExcluido       
        operacion.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))
    

class OperacionSujetoExcluidoUpdateView(LoginRequiredMixin, UpdateView):
    
    login_url = '/ingresar'
    template_name = 'sujeto excluido/operacion_sujeto_excluido_form.html'
    form_class = OperacionesSujetoExcluidoForm
    model = OperacionesSujetoExcluido
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')
    
    def form_valid(self, form):
        operacion = form.save(commit=False) 
        operacion.entidad = self.request.user.entidad      
        operacion.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['uniMedida_id'] = self.get_object().uniMedida.id if self.get_object().uniMedida else None
        return context

class OperacionSujetoExcluidoDetailView(LoginRequiredMixin, DetailView):
    login_url = '/ingresar/'
    template_name = 'sujeto excluido/operacion_sujeto_excluido_by_id_view.html'
    model = OperacionesSujetoExcluido
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        operacionSujetoExcluido = get_object_or_404(OperacionesSujetoExcluido, pk=context['object'].id)
        context['operacion'] = operacionSujetoExcluido
        context['show'] = True
        return context

class SujetoExcluidoMonthView(LoginRequiredMixin,MonthArchiveView):
    """Muestra la lista de sujetos excluidos por mes"""

    login_url='/ingresar/'
    queryset = SujetoExcluido.objects.all()
    date_field = "fecha"
    template_name='sujeto excluido/sujeto_excluido_month.html'
    allow_empty = True
    allow_future = True

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        sujeto = SujetoExcluido.objects.filter(entidad=self.request.user.entidad)
        context['registro'] = sujeto
        return context
    
    # # Devuelve el mes actual en formato MM

class SujetoExcluidoDetailView(LoginRequiredMixin,DetailView):
    """Muestra los datos de un sujeto excluido en especifico"""

    login_url = '/ingresar/'
    template_name = 'sujeto excluido/sujeto_excluido_by_id_view.html'
    model = SujetoExcluido
    context_object_name = 'sujetoExcluido'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        sujetoExcluido = self.object  # Obtenemos el objeto SujetoExcluido actual
        
        try:
            # Intentamos obtener Identificador, OperacionesSujetoExcluido y Apendice si existen
            identificador = Identificador.objects.get(sujetoExcluido=sujetoExcluido)
            operaciones_sujeto_excluido = OperacionesSujetoExcluido.objects.filter(sujetoExcluido=sujetoExcluido)
            apendice = Apendice.objects.filter(sujetoExcluido=sujetoExcluido)
            
            context['identificador'] = identificador
            context['operacionesSujetoExcluido'] = operaciones_sujeto_excluido
            context['apendices'] = apendice
            context['show'] = True
        
        except Identificador.DoesNotExist:
            #Si no hay Identificador, asignamos None al contexto
            context['identificador'] = None
            
        except OperacionesSujetoExcluido.DoesNotExist:
            # Si no hay OperacionesSujetoExcluido, asignamos None al contexto
            context['operacionesSujetoExcluido'] = None
        
        except Apendice.DoesNotExist:
            # Si no hay Apendice, asignamos None al contexto
            context['apendices'] = None
        
        return context 

class SujetoExcluidoCreateView(LoginRequiredMixin, CreateView):
    login_url = '/ingresar/'
    template_name = 'sujeto excluido/sujeto_excluido_form.html'
    model = SujetoExcluido
    form_class = SujetoExcluidoForm

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')
    
    
    def get_initial(self):
        initial = super().get_initial()
        initial['identificador'] = self.request.GET.get('identificador')
        initial['receptor'] = self.request.GET.get('receptor')
        initial['pago'] = self.request.GET.get('pago')
        return initial
    

    def form_valid(self, form):
        form.instance.emisor = self.request.user.entidad
        form.instance.entidad = self.request.user.entidad  # Assuming you want to assign the first entity related to the user
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['identificador_id'] = self.request.GET.get('identificador_id')
        context['receptor_id'] = self.request.GET.get('receptor_id')
        context['pago_id'] = self.request.GET.get('pago_id')
        return context        

class SujetoExcluidoUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/ingresar/'
    model = SujetoExcluido
    template_name = 'sujeto excluido/sujeto_excluido_form.html'
    form_class = SujetoExcluidoForm
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')

    def form_valid(self, form):
        form.instance.entidad = self.request.user.entidad  # Assuming you want to assign the first entity related to the user
        return super().form_valid(form)

    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['receptor_id'] = self.object.receptor.id if self.object.receptor else None
        context['pago_id'] = self.object.pago.id if self.object.pago else None
        return context

class FormaPagoView(LoginRequiredMixin,View):
    
    login_url = '/ingresar/'
    template_name = 'forma_pago_view.html'
    model = FormaPago
    
    def get_context_data(self, **kwargs) :
        context = super(FormaPagoView, self).get_context(**kwargs)
        formaPago = FormaPago.objects.all()
        context['registro'] = formaPago
        return context
   
class FormaPagoCreateView(LoginRequiredMixin,CreateView):
    
    login_url = '/ingresar'
    template_name = 'sujeto excluido/forma_pago_form.html'
    form_class = FormaPagoForm
    model = FormaPago
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')

class FormaPagoUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'sujeto excluido/forma_pago_form.html'
    form_class = FormaPagoForm
    model = FormaPago
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')

class PagoView(LoginRequiredMixin,View):
    
    login_url = '/ingresar/'
    template_name = 'pago_view.html'
    model = Pago
    
    def get_context_data(self, **kwargs) :
        context = super(Pago, self).get_context(**kwargs)
        pago = Pago.objects.all()
        context['registro'] = pago
        return context
    
class PagoCreateView(LoginRequiredMixin,CreateView):
    
    login_url = '/ingresar'
    template_name = 'sujeto excluido/pago_form.html'
    form_class = PagoForm
    model = Pago
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')
    
    def get_initial(self):
        initial = super().get_initial()
        initial['formaPago'] = self.request.GET.get('formaPago')
        return initial
    
    def form_valid(self, form):
        # Asignar la entidad actual al formulario antes de guardarlo
        form.instance.entidad = self.request.user.entidad  # Ajusta esto según cómo obtienes la entidad actual del usuario
        return super().form_valid(form)
    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formaPago_id'] = self.request.GET.get('formaPago_id')
        return context

class PagoUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'sujeto excluido/pago_form.html'
    form_class = PagoForm
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')

    def form_valid(self, form):
        # Asignar la entidad actual al formulario antes de guardarlo
        form.instance.entidad = self.request.user.entidad  # Ajusta esto según cómo obtienes la entidad actual del usuario
        return super().form_valid(form)
    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formaPago_id'] = self.object.formaPago.id if self.object.formaPago else None
        return context

class ApendiceView(LoginRequiredMixin,DetailView):
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

class ApendiceCreateView(LoginRequiredMixin, CreateView):
    login_url = '/ingresar'
    template_name = 'forms comunes/apendice_form.html'
    form_class = ApendiceForm
    model = Apendice
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')
    
    def get_initial(self):
        initial = super().get_initial()
        initial['sujetoExcluido'] = self.request.GET.get('sujetoExcluido')
        initial['comprobanteDonacion'] = self.request.GET.get('comprobanteDonacion')
        return initial
    
    def form_valid(self, form):
        origin = self.request.GET.get('origin')
        print(origin)
        id = self.kwargs.get('id')
        
        if origin == 'sujetoExcluido':
            sujetoExcluido = get_object_or_404(SujetoExcluido, pk=id)
            form.instance.sujetoExcluido = sujetoExcluido
        elif origin == 'comprobanteDonacion':
            comprobanteDonacion = get_object_or_404(ComprobanteDonacion, pk=id)
            form.instance.comprobanteDonacion = comprobanteDonacion
        else:
            # Genera un mensaje de error y redirige a la página de panel_facturas
            messages.error(self.request, 'Origen del apedice no válido')
            return HttpResponseRedirect(reverse_lazy('panel_facturas'))
        # Asignar la entidad actual al formulario antes de guardarlo
        form.instance.entidad = self.request.user.entidad  # Ajusta esto según cómo obtienes la entidad actual del usuario
        return super().form_valid(form)
    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sujetoExcluido_id'] = self.request.GET.get('sujetoExcluido_id')
        context['comprobanteDonacion_id'] = self.request.GET.get('comprobanteDonacion_id')
        return context

class ApendiceUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'formas comunes/apendice_form.html'
    form_class = ApendiceForm
    model = Apendice
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')
    
    def form_valid(self, form):
        # Asignar la entidad actual al formulario antes de guardarlo
        form.instance.entidad = self.request.user.entidad  # Ajusta esto según cómo obtienes la entidad actual del usuario
        return super().form_valid(form)
    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sujetoExcluido_id'] = self.object.sujetoExcluido.id if self.object.sujetoExcluido else None
        context['comprobanteDonacion_id'] = self.object.comprobanteDonacion.id if self.object.comprobanteDonacion else None
        return context

class TipoDocumentoView(LoginRequiredMixin,View):
    
    login_url = '/ingresar/'
    template_name = 'tipo_documento_view.html'
    model = TipoDocumento
    
    def get_context_data(self, **kwargs) :
        context = super(TipoDocumento, self).get_context(**kwargs)
        tipoDocumento= TipoDocumento.objects.all()
        context['registro'] = tipoDocumento
        return context
    
class TipoDocumentoCreateView(LoginRequiredMixin,CreateView):
    
    login_url = '/ingresar'
    template_name = 'forms comunes/tipo_documento_form.html'
    form_class = TipoDocumentoForm
    model = TipoDocumento
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')
    
class TipoDocumentoUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'forms comunes/tipo_documento_form.html'
    form_class = TipoDocumentoForm
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')
    
class IdentificadorView(LoginRequiredMixin,View):
    
    login_url = '/ingresar/'
    template_name = 'identificador_view.html'
    model = Identificador
    
    def get_context_data(self, **kwargs) :
        context = super(Identificador, self).get_context(**kwargs)
        identificador = Identificador.objects.all()
        context['registro'] = identificador
        return context
   
class IdentificadorCreateView(LoginRequiredMixin,CreateView):
    
    login_url = '/ingresar'
    template_name = 'forms comunes/identificador_form.html'
    model = Identificador
    form_class = IdentificadorForm
    
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')
    
    def form_valid(self, form):
        origin = self.request.GET.get('origin')
        print(origin)
        id = self.kwargs.get('pk')
        
        if origin == 'sujetoExcluido':
            sujetoExcluido = get_object_or_404(SujetoExcluido, pk=id)
            form.instance.sujetoExcluido = sujetoExcluido
        elif origin == 'comprobanteDonacion':
            comprobanteDonacion = get_object_or_404(ComprobanteDonacion, pk=id)
            form.instance.comprobanteDonacion = comprobanteDonacion
        else:
            # Genera un mensaje de error y redirige a la página de panel_facturas
            messages.error(self.request, 'Origen del identificador no válido')
            return HttpResponseRedirect(reverse_lazy('panel_facturas'))
        # Asignar la entidad actual al formulario antes de guardarlo
        form.instance.entidad = self.request.user.entidad  # Ajusta esto según cómo obtienes la entidad actual del usuario
        return super().form_valid(form)
    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))
    

class IdentificadorUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'forms comunes/identificador_form.html'
    model = Identificador
    form_class = IdentificadorForm
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')

    def form_valid(self, form):
        # Asegúrate de que la entidad no se modifique durante la actualización
        form.instance.entidad = self.object.entidad
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))
    
class ReceptorView(LoginRequiredMixin,View):
    
    login_url = '/ingresar/'
    template_name = 'receptor_view.html'
    model = Receptor
    
    def get_context_data(self, **kwargs) :
        context = super(Receptor, self).get_context(**kwargs)
        receptor = receptor.objects.all()
        context['registro'] = receptor
        return context
    
class ReceptorCreateView(LoginRequiredMixin,CreateView):
    
    login_url = '/ingresar'
    template_name = 'forms comunes/receptor_form.html'
    form_class = ReceptorForm
    model = Receptor
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')
    
    def get_initial(self):
        initial = super().get_initial()
        initial['actividadEconomica'] = self.request.GET.get('actividadEconomica')
        initial['direccionReceptor'] = self.request.GET.get('direccionReceptor')
        return initial
    
    def form_valid(self, form):
        # Asegúrate de que la entidad no se modifique durante la actualización
        form.instance.entidad = self.request.user.entidad
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['actividadEconomica_id'] = self.request.GET.get('actividadEconomica_id')
        context['direccionReceptor_id'] = self.request.GET.get('direccionReceptor_id')
        return context


class ReceptorUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'forms comunes/receptor_form.html'
    form_class = ReceptorForm
    model = Receptor
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')

    def form_valid(self, form):
        # Asegúrate de que la entidad no se modifique durante la actualización
        form.instance.entidad = self.request.user.entidad
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['actividadEconomica_id'] = self.object.actividadEconomica.id if self.object.actividadEconomica else None
        context['direccionReceptor_id'] = self.object.direccionReceptor.id if self.object.direccionReceptor else None
        return context

class OtroDocumentoAsociadoView(LoginRequiredMixin,View):
    
    login_url = '/ingresar/'
    template_name = 'comprobante donacion/otro_documento_asociado_view.html'
    model = OtroDocumentoAsociado
    
    def get_context_data(self, **kwargs) :
        context = super(OtroDocumentoAsociado, self).get_context(**kwargs)
        otroDocumentoAsociado = OtroDocumentoAsociado.objects.all()
        context['otroDocumentoAsociado'] = otroDocumentoAsociado
        return context
    
class OtroDocumentoAsociadoCreateView(LoginRequiredMixin,CreateView):
    
    login_url = '/ingresar'
    template_name = 'comprobante donacion/otro_documento_asociado_form.html'
    form_class = OtroDocumentoAsociadoForm
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')
    
    def form_valid(self, form):
        id=self.kwargs.get("id")
        comprobanteDonacion = get_object_or_404(ComprobanteDonacion, pk=id)
        # Asegúrate de que la entidad no se modifique durante la actualización
        form.instance.entidad = self.request.user.entidad
        form.instance.comprobanteDonacion = comprobanteDonacion
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))
    
    

class OtroDocumentoAsociadoUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'comprobante donacion/otro_documento_asociado_form.html'
    form_class = OtroDocumentoAsociadoForm
    model = OtroDocumentoAsociado
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')

    def form_valid(self, form):
        # Asegúrate de que la entidad no se modifique durante la actualización
        form.instance.entidad = self.request.user.entidad
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))
    

class CuerpoDocumentoView(LoginRequiredMixin,View):
    
    login_url = '/ingresar/'
    template_name = 'comprobante donacion/cuerpo_documento_view.html'
    model = CuerpoDocumento
    
    def get_context_data(self, **kwargs) :
        context = super(CuerpoDocumento, self).get_context(**kwargs)
        cuerpoDocumento = CuerpoDocumento.objects.all()
        context['cuerpoDocumento'] = cuerpoDocumento
        return context
   
class CuerpoDocumentoCreateView(LoginRequiredMixin,CreateView):
    
    login_url = '/ingresar'
    template_name = 'comprobante donacion/cuerpo_documento_form.html'
    form_class = CuerpoDocumentoForm
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')
    
    def get_initial(self):
        initial = super().get_initial()
        initial['unidadMedida'] = self.request.GET.get('unidadMedida')
        return initial
    
    def form_valid(self, form):
        id=self.kwargs.get("id")
        comprobanteDonacion = get_object_or_404(ComprobanteDonacion, pk=id)
        # Asegúrate de que la entidad no se modifique durante la actualización
        form.instance.entidad = self.request.user.entidad
        form.instance.comprobanteDonacion = comprobanteDonacion
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['uniMedida_id'] = self.request.GET.get('uniMedida_id')
        return context
    
class CuerpoDocumentoUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'comprobante donacion/cuerpo_documento_form.html'
    form_class = CuerpoDocumentoForm
    model = CuerpoDocumento
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')
    
    def form_valid(self, form):
        # Asegúrate de que la entidad no se modifique durante la actualización
        form.instance.entidad = self.request.user.entidad
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['uniMedida_id'] = self.object.uniMedida.id if self.object.uniMedida else None
        return context

class PagoDonacionView(LoginRequiredMixin,View):
    
    login_url = '/ingresar/'
    template_name = 'comprobante donacion/pago_donacion_view.html'
    model = PagoDonacion
    
    def get_context_data(self, **kwargs) :
        context = super(PagoDonacion, self).get_context(**kwargs)
        pagoDonacion = PagoDonacion.objects.all()
        context['pagoDonacion'] = PagoDonacion
        return context
    
class PagoDonacionCreateView(LoginRequiredMixin,CreateView):
    
    login_url = '/ingresar'
    template_name = 'comprobante donacion/pago_donacion_form.html'
    form_class = PagoDonacionForm
    model = PagoDonacion
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')
    
    def form_valid(self, form):
        # Asegúrate de que la entidad no se modifique durante la actualización
        form.instance.entidad = self.request.user.entidad
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))
    

class PagoDonacionUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'comprobante donacion/pago_donacion_form.html'
    form_class = PagoDonacionForm
    model = PagoDonacion
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')
    
    def form_valid(self, form):
        # Asegúrate de que la entidad no se modifique durante la actualización
        form.instance.entidad = self.request.user.entidad
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))

class ComprobanteDonacionMonthView(LoginRequiredMixin,MonthArchiveView):
    """Muestra la lista de sujetos excluidos por mes"""

    login_url='/ingresar/'
    date_field = "fecha"
    queryset = ComprobanteDonacion.objects.all()
    template_name='comprobante donacion/comprobante_donacion_month.html'
    allow_empty = True
    allow_future = True

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        comprobante = ComprobanteDonacion.objects.filter(entidad=self.request.user.entidad)
        context['registro'] = comprobante
        return context
    
    def get_year(self):
        return timezone.now().year

    def get_month(self):
        return timezone.now().strftime('%m')  # Devuelve el mes actual en formato MM

class ComprobanteDonacionDetailView(LoginRequiredMixin,DetailView):
    """Muestra los datos de un comprobante de donacion en especifico"""

    login_url = '/ingresar/'
    template_name = 'comprobante donacion/comprobante_donacion_by_id_view.html'
    model = ComprobanteDonacion
    context_object_name = 'comprobanteDonacion'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        comprobanteDonacion = self.object #Obtenemos el comprobante de donacion actual
        
        try:
            #intentamos obtener identificador, cuerpos de documento, otros documentos y apendices si exixten 
            identificador = Identificador.objects.get(comprobanteDonacion=comprobanteDonacion)
            cuerpoDocumento = CuerpoDocumento.objects.filter(comprobanteDonacion=comprobanteDonacion)
            otroDocumentoAsociado = OtroDocumentoAsociado.objects.filter(comprobanteDonacion=comprobanteDonacion)
            apendice = Apendice.objects.filter(comprobanteDonacion=comprobanteDonacion)
            context['identificador'] = identificador
            context['otroDocumentoAsociado'] = otroDocumentoAsociado
            context['cuerpoDocumento'] = cuerpoDocumento
            context['apendices'] = apendice
            context['show'] = True
            return context   
        
        except Identificador.DoesNotExist:
            context['identificador'] = None
        
        except CuerpoDocumento.DoesNotExist:
            context['cuerpoDocumento'] = None
        
        except OtroDocumentoAsociado.DoesNotExist:
            context['otroDocumentoAsociado'] = None
        
        except Apendice.DoesNotExist:
            context['apendice'] = None
        
        return context

class ComprobanteDonacionCreateView(LoginRequiredMixin, CreateView):
    
    login_url = '/ingresar/'
    template_name = 'comprobante donacion/comprobante_donacion_form.html'
    model = ComprobanteDonacion
    form_class = ComprobanteDonacionForm
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')
    
    def get_initial(self):
        initial = super().get_initial()
        initial['receptor'] = self.request.GET.get('receptor')
        initial['pagoDonacion'] = self.request.GET.get('pagoDonacion')
        return initial
    

    def form_valid(self, form):
        form.instance.emisor = self.request.user.entidad
        form.instance.entidad = self.request.user.entidad  # Assuming you want to assign the first entity related to the user
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['receptor_id'] = self.request.GET.get('receptor_id')
        context['pago_id'] = self.request.GET.get('pago_id')
        return context   
        
class ComprobanteDonacionUpdateView(LoginRequiredMixin, UpdateView):
    
    login_url = '/ingresar/'
    model = ComprobanteDonacion
    template_name = 'comprobante donacion/comprobante_donacion_form.html'
    form_class = ComprobanteDonacionForm    
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')

    def form_valid(self, form):
        form.instance.entidad = self.request.user.entidad  # Assuming you want to assign the first entity related to the user
        return super().form_valid(form)

    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['receptor_id'] = self.object.receptor.id if self.object.receptor else None
        context['pago_id'] = self.object.pago.id if self.object.pago else None
        return context


class FacturaElectronicaMonthView(LoginRequiredMixin,MonthArchiveView):
    """Muestra la lista de facturas electronicas y credito fiscal por mes"""

    login_url='/ingresar/'
    date_field = "fecha"
    queryset = FacturaElectronica.objects.all()
    template_name='factura electronica/factura_electronica_month.html'
    allow_empty = True
    allow_future = True

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        factura = FacturaElectronica.objects.filter(entidad=self.request.user.entidad)
        context['registro'] = factura
        return context
    
    def get_year(self):
        return timezone.now().year

    def get_month(self):
        return timezone.now().strftime('%m')  # Devuelve el mes actual en formato MM

class FacturaElectronicaDetailView(LoginRequiredMixin,DetailView):
    """Muestra los datos de una factura electronica o credito fiscal en especifico"""

    login_url = '/ingresar/'
    template_name = 'factura electronica/factura_electronica_by_id_view.html'
    model = FacturaElectronica
    context_object_name = 'facturaElectronica'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        facturaElectronica = self.object #Obtenemos la factra eletronica o credito fiscal actual
        
        try:
            #intentamos obtener identificador, cuerpos de documento, otros documentos y apendices si exixten 
            identificador = Identificador.objects.get(facturaElectronica=facturaElectronica)
            extencion = Extencion.objects.filter(facturaElectronica=facturaElectronica)
            documentoRelacionado = DocumentoRelacionado.objects.filter(facturaElectronica=facturaElectronica)
            otroDocumento = OtroDocumento.objects.filter(facturaElectronica=facturaElectronica)
            ventaTercero = VentaTercero.objects.filter(facturaElectronica=facturaElectronica)
            documento = Documento.objects.filter(facturaElectronica=facturaElectronica)
            apendice = Apendice.objects.filter(facturaElectronica=facturaElectronica)
            context['identificador'] = identificador
            context['documentoRelacionado'] = documentoRelacionado
            context['otroDocumento'] = otroDocumento
            context['ventaTercero'] = ventaTercero
            context['documento'] = documento
            context['extencion'] = extencion
            context['apendice'] = apendice
            context['show'] = True
            return context   
        
        except Identificador.DoesNotExist:
            context['identificador'] = None
        
        except DocumentoRelacionado.DoesNotExist:
            context['documentoRelacionado'] = None
        
        except OtroDocumento.DoesNotExist:
            context['otroDocumento'] = None
        
        except VentaTercero.DoesNotExist:
            context['ventaTercero'] = None
        
        except Documento.DoesNotExist:
            context['documento'] = None
        
        except Extencion.DoesNotExist:
            context['extencion'] = None
        
        except Apendice.DoesNotExist:
            context['apendice'] = None
        
        return context

class FacturaElectronicaCreateView(LoginRequiredMixin, CreateView):
    
    login_url = '/ingresar/'
    template_name = 'factura electronica/factura_electronica_form.html'
    model = FacturaElectronica
    form_class = FacturaElectronicaForm
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')
    
    def get_initial(self):
        initial = super().get_initial()
        initial['receptor'] = self.request.GET.get('receptor')
        initial['pago'] = self.request.GET.get('pago')
        return initial
    

    def form_valid(self, form):
        form.instance.emisor = self.request.user.entidad
        form.instance.entidad = self.request.user.entidad  # Assuming you want to assign the first entity related to the user
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['receptor_id'] = self.request.GET.get('receptor_id')
        context['pago_id'] = self.request.GET.get('pago_id')
        return context   
        
class FacturaElectronicaUpdateView(LoginRequiredMixin, UpdateView):
    
    login_url = '/ingresar/'
    model = FacturaElectronica
    template_name = 'factura electronica/factura_electronica_form.html'
    form_class = FacturaElectronicaForm    
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')

    def form_valid(self, form):
        form.instance.entidad = self.request.user.entidad  # Assuming you want to assign the first entity related to the user
        return super().form_valid(form)

    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['receptor_id'] = self.object.receptor.id if self.object.receptor else None
        context['pago_id'] = self.object.pago.id if self.object.pago else None
        return context

class TributoCreateView(LoginRequiredMixin,CreateView):
    
    login_url = '/ingresar'
    template_name = 'factura electronica/tributo_form.html'
    form_class = TributoForm
    model = Tributo
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')
    

class TributoUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'factura electronica/tributo_form.html'
    form_class = TributoForm
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')

class TributoResumenCreateView(LoginRequiredMixin,CreateView):
    
    login_url = '/ingresar'
    template_name = 'factura electronica/tributo_resumen_form.html'
    form_class = TributoResumenForm
    model = TributoResumen
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')
    

class TributoResumenUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'factura electronica/tributo_resumen_form.html'
    form_class = TributoResumenForm
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')

class PagoFacturaDetailView(LoginRequiredMixin, DetailView):
    login_url = '/ingresar/'
    template_name = 'factura electronica/pago_factura_by_id.html'
    model = PagoFactura
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pagoFactura = get_object_or_404(PagoFactura, pk=context['object'].id)
        context['pago'] = pagoFactura
        context['show'] = True
        return context

class PagoFacturaCreateView(LoginRequiredMixin,CreateView):
    
    login_url = '/ingresar'
    template_name = 'factura electronica/pago_factura_form.html'
    form_class = PagoFacturaForm
    model = PagoFactura
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')
    

class PagoFacturaUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'factura electronica/pago_factura_form.html'
    form_class = PagoFacturaForm
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')

class ExtencionDetailView(LoginRequiredMixin, DetailView):
    login_url = '/ingresar/'
    template_name = 'factura electronica/extencion_by_id.html'
    model = Extencion
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        extencion = get_object_or_404(Extencion, pk=context['object'].id)
        context['extencion'] = extencion
        context['show'] = True
        return context

class ExtencionCreateView(LoginRequiredMixin,CreateView):
    
    login_url = '/ingresar'
    template_name = 'factura electronica/extencion_form.html'
    form_class = ExtencionForm
    model = Extencion
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')
    
    def form_valid(self, form):
        id=self.kwargs.get("pk")
        facturaElectronica = get_object_or_404(FacturaElectronica, pk=id)
        form.instance.entidad = self.request.user.entidad  
        form.instance.facturaEletronica = facturaElectronica
        return super().form_valid(form)

    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))
    

class ExtencionUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'factura electronica/extencion_form.html'
    form_class = ExtencionForm
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')
    
    def form_valid(self, form):

        form.instance.entidad = self.request.user.entidad  
        return super().form_valid(form)

    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))

class DocumentoRelacionadoDetailView(LoginRequiredMixin, DetailView):
    login_url = '/ingresar/'
    template_name = 'factura electronica/documento_relacionado_by_id.html'
    model = DocumentoRelacionado
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        documentoRelacionado = get_object_or_404(DocumentoRelacionado, pk=context['object'].id)
        context['documentoRelacionado'] = documentoRelacionado
        context['show'] = True
        return context

class DocumentoRelacionadoCreateView(LoginRequiredMixin,CreateView):
    
    login_url = '/ingresar'
    template_name = 'factura electronica/documento_relacionado_form.html'
    form_class = DocumentoRelacionadoForm
    model = DocumentoRelacionado
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')
    
    def form_valid(self, form):
        id=self.kwargs.get("pk")
        facturaElectronica = get_object_or_404(FacturaElectronica, pk=id)
        form.instance.entidad = self.request.user.entidad  
        form.instance.facturaEletronica = facturaElectronica
        return super().form_valid(form)

    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))
    

class DocumentoRelacionadoUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'factura electronica/documento_relacionado_form.html'
    form_class = DocumentoRelacionadoForm
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')
    
    def form_valid(self, form):

        form.instance.entidad = self.request.user.entidad  
        return super().form_valid(form)

    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))

class MedicoDetailView(LoginRequiredMixin, DetailView):
    login_url = '/ingresar/'
    template_name = 'factura electronica/medico_by_id.html'
    model = Extencion
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        medico = get_object_or_404(Medico, pk=context['object'].id)
        context['medico'] = medico
        context['show'] = True
        return context

class MedicoCreateView(LoginRequiredMixin,CreateView):
    
    login_url = '/ingresar'
    template_name = 'factura electronica/medico_form.html'
    form_class = MedicoForm
    model = Medico
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')
    
    def form_valid(self, form):
        form.instance.entidad = self.request.user.entidad  
        return super().form_valid(form)

    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))
    

class MedicoUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'factura electronica/medico_form.html'
    form_class = MedicoForm
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')
    
    def form_valid(self, form):

        form.instance.entidad = self.request.user.entidad  
        return super().form_valid(form)

    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))

class OtroDocumentoDetailView(LoginRequiredMixin, DetailView):
    login_url = '/ingresar/'
    template_name = 'factura electronica/otro_documento_by_id.html'
    model = OtroDocumento
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        otroDocumento = get_object_or_404(OtroDocumento, pk=context['object'].id)
        context['otroDocumento'] = otroDocumento
        context['show'] = True
        return context

class OtroDocumentoCreateView(LoginRequiredMixin,CreateView):
    
    login_url = '/ingresar'
    template_name = 'factura electronica/otro_documento_form.html'
    form_class = OtroDocumentoForm
    model = OtroDocumento
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')
    
    def form_valid(self, form):
        id=self.kwargs.get("pk")
        facturaElectronica = get_object_or_404(FacturaElectronica, pk=id)
        form.instance.entidad = self.request.user.entidad  
        form.instance.facturaEletronica = facturaElectronica
        return super().form_valid(form)

    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))
    

class OtroDocumentoUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'factura electronica/otro_documento_form.html'
    form_class = OtroDocumentoForm
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')
    
    def form_valid(self, form):

        form.instance.entidad = self.request.user.entidad  
        return super().form_valid(form)

    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))

class VentaTerceroDetailView(LoginRequiredMixin, DetailView):
    login_url = '/ingresar/'
    template_name = 'factura electronica/venta_tercero_by_id.html'
    model = VentaTercero
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ventaTercero = get_object_or_404(VentaTercero, pk=context['object'].id)
        context['ventaTercero'] = ventaTercero
        context['show'] = True
        return context

class VentaTerceroCreateView(LoginRequiredMixin,CreateView):
    
    login_url = '/ingresar'
    template_name = 'factura electronica/venta_tercero_form.html'
    form_class = VentaTerceroForm
    model = VentaTercero
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')
    
    def form_valid(self, form):
        id=self.kwargs.get("pk")
        facturaElectronica = get_object_or_404(FacturaElectronica, pk=id)
        form.instance.entidad = self.request.user.entidad  
        form.instance.facturaEletronica = facturaElectronica
        return super().form_valid(form)

    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))
    

class VentaTerceroUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'factura electronica/venta_tercero_form.html'
    form_class = VentaTerceroForm
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')
    
    def form_valid(self, form):

        form.instance.entidad = self.request.user.entidad  
        return super().form_valid(form)

    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))

class DocumentoDetailView(LoginRequiredMixin, DetailView):
    login_url = '/ingresar/'
    template_name = 'factura electronica/documento_by_id.html'
    model = Documento
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        documento = get_object_or_404(Documento, pk=context['object'].id)
        context['documento'] = documento
        context['show'] = True
        return context

class DocumentoCreateView(LoginRequiredMixin,CreateView):
    
    login_url = '/ingresar'
    template_name = 'factura electronica/documento_form.html'
    form_class = DocumentoForm
    model = Documento
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')
    
    def form_valid(self, form):
        id=self.kwargs.get("pk")
        facturaElectronica = get_object_or_404(FacturaElectronica, pk=id)
        form.instance.entidad = self.request.user.entidad  
        form.instance.facturaEletronica = facturaElectronica
        return super().form_valid(form)

    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))
    

class DocumentoUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'factura electronica/documento_form.html'
    form_class = DocumentoForm
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')
    
    def form_valid(self, form):

        form.instance.entidad = self.request.user.entidad  
        return super().form_valid(form)

    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))

class FacturaElectronicaDetailView(LoginRequiredMixin, DetailView):
    login_url = '/ingresar/'
    template_name = 'factura electronica/factura_electronica_by_id.html'
    model = FacturaElectronica
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        facturaElectronica = get_object_or_404(FacturaElectronica, pk=context['object'].id)
        context['facturaElectronica'] = FacturaElectronica
        context['show'] = True
        return context

class FacturaElectronicaCreateView(LoginRequiredMixin,CreateView):
    
    login_url = '/ingresar'
    template_name = 'factura electronica/factura_electronica_form.html'
    form_class = FacturaElectronicaForm
    model = FacturaElectronica
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')
    
    def form_valid(self, form):
        form.instance.entidad = self.request.user.entidad  
        return super().form_valid(form)

    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))
    

class FacturaElectronicaUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'factura electronica/factura_electronica_form.html'
    form_class = FacturaElectronicaForm
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_facturas')
    
    def form_valid(self, form):

        form.instance.entidad = self.request.user.entidad  
        return super().form_valid(form)

    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))

class ResponseHaciendaBySujetoExcluidoListView(ListView):
    model = ResponseHacienda
    template_name = 'sujeto excluido/response_hacienda_by_sujeto_excluido_list.html'
    context_object_name = 'responses'

    def get_queryset(self):
        queryset = super().get_queryset()
        sujeto_excluido_id = self.kwargs['pk']
        if sujeto_excluido_id:
            queryset = queryset.filter(sujetoExcluido_id=sujeto_excluido_id)
        return queryset.order_by('-created')

class ResponseHaciendaByComprobanteDonacionListView(ListView):
    model = ResponseHacienda
    template_name = 'comprobante donacion/response_hacienda_by_comprobante_donacion_list.html'
    context_object_name = 'responses'

    def get_queryset(self):
        queryset = super().get_queryset()
        comprobante_donacion_id= self.kwargs['pk']
        if comprobante_donacion_id:
            queryset = queryset.filter(comprobanteDonacion_id=comprobante_donacion_id)
        return queryset.order_by('-created')

class ResponseHaciendaByFacturaElectronicaListView(ListView):
    model = ResponseHacienda
    template_name = 'factura electronica/response_hacienda_by_factura_electronica_list.html'
    context_object_name = 'responses'

    def get_queryset(self):
        queryset = super().get_queryset()
        factura_electronica_id= self.kwargs['pk']
        if factura_electronica_id:
            queryset = queryset.filter(factura_electronica_id=factura_electronica_id)
        return queryset.order_by('-created')
#Creando los Json correspondiente a cada factura


def sujetoExcluidoList(id):
    sujetoExcluido = SujetoExcluido.objects.get(id=id)
    identificador = Identificador.objects.get(sujetoExcluido=sujetoExcluido)
    operacionesSujetoExcluido = OperacionesSujetoExcluido.objects.filter(sujetoExcluido=sujetoExcluido)
    fechaEmi = sujetoExcluido.fechaTransmicion.date().isoformat()
    horaEmi = sujetoExcluido.fechaTransmicion.strftime("%H:%M:%S")
    
    def serialize(obj):
        if isinstance(obj,(datetime.date, datetime.datetime)):
            return obj.isoformat()
        if isinstance(obj, Decimal):
            return float(obj)
        if isinstance(obj, UUID):
            return str(obj)
        if isinstance(obj, TipoDocumento):
            return str(obj)
        if isinstance(obj, FormaPago):
            return str(obj)
        raise TypeError("Type not serializable")
    
    sujetoData = {
        'identificacion': {
            'version': int(identificador.version),
            'ambiente': identificador.ambiente,
            'tipoDte': identificador.tipoDte.codigo,
            'numeroControl': identificador.numeroControl,
            'codigoGeneracion': str(identificador.codigoGeneracion).upper(),
            'tipoModelo': int(identificador.tipoModelo),
            'tipoOperacion': int(identificador.tipoOperacion),
            'tipoContingencia': int(identificador.tipoContingencia) if identificador.tipoContingencia else None,
            'motivoContin': identificador.motivoContin,
            'fecEmi': fechaEmi,
            'horEmi': horaEmi,
            'tipoMoneda': identificador.tipoMoneda
        },
        'emisor': {
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
            "nombre": sujetoExcluido.receptor.nombre,
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
            "totalCompra" : serialize(sujetoExcluido.totalCompra),
            "descu" : serialize(sujetoExcluido.descu),
            "totalDescu" : serialize(sujetoExcluido.totalDescu),
            "subTotal" : serialize(sujetoExcluido.subTotal),
            "ivaRete1" : serialize(sujetoExcluido.ivaRete1),
            "reteRenta" : serialize(sujetoExcluido.reteRenta),
            "totalPagar" : serialize(sujetoExcluido.totalPagar),
            "totalLetras" : sujetoExcluido.totalLetras,
            "condicionOperacion" : int(sujetoExcluido.condicionOperacion),
            "pagos" : [
                {
                    "codigo" : sujetoExcluido.pago.formaPago.codigo,
                    "montoPago" : serialize(sujetoExcluido.pago.montoPago),
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
            "tipoItem" : int(operacion.tipoItem),
            "codigo" : operacion.codigo,
            "uniMedida": int(operacion.uniMedida.codigo),
            "cantidad" : serialize(operacion.cantidad),
            "montoDescu": serialize(operacion.montoDescu),
            "compra": serialize(operacion.compra),
            "descripcion" : operacion.descripccion,
            "precioUni": serialize(operacion.precioUni)
        }
        sujetoData['cuerpoDocumento'].append(operacionesData)
    apendiceSujetoExcluido = Apendice.objects.filter(sujetoExcluido=sujetoExcluido)
    if apendiceSujetoExcluido.exists():
        for apendices in apendiceSujetoExcluido:
            apendicesData = {
                "campo": apendices.campo,
                "etiqueta": apendices.etiqueta,
                "valor": apendices.valor
            }
            sujetoData['apendice'].append(apendicesData)
    else:
        sujetoData['apendice'] = None
    
    return sujetoData


def comprobanteDonacionList(id):
    comprobanteDonacion = ComprobanteDonacion.objects.get(id=id)
    identificador = Identificador.objects.filter(comprobanteDonacion=comprobanteDonacion)
    otroDocumentoAsociado = OtroDocumentoAsociado.objects.filter(comprobanteDonacion=comprobanteDonacion)
    cuerpoDocumento = CuerpoDocumento.objects.filter(comprobanteDonacion=comprobanteDonacion)
    apendiceComprobanteDonacion = Apendice.objects.filter(comprobanteDonacion=comprobanteDonacion)
    fechaEmi = comprobanteDonacion.fechaTransmicion.date().isoformat()
    horaEmi = comprobanteDonacion.fechaTransmicion.strftime("%H:%M:%S")
    
    def serialize(obj):
        if isinstance(obj,(datetime.date, datetime.datetime)):
            return obj.isoformat()
        if isinstance(obj, Decimal):
            return float(obj)
        if isinstance(obj, UUID):
            return str(obj)
        if isinstance(obj, TipoDocumento):
            return str(obj)
        if isinstance(obj, FormaPago):
            return str(obj)
        raise TypeError("Type not serializable")
    
    comprobanteData = {
        'identificacion': {
            'version': int(identificador.version),
            'ambiente': identificador.ambiente,
            'tipoDte': identificador.tipoDte.codigo,
            'numeroControl': identificador.numeroControl,
            'codigoGeneracion': str(identificador.codigoGeneracion).upper(),
            'tipoModelo': int(identificador.tipoModelo),
            'tipoOperacion': int(identificador.tipoOperacion),
            'tipoContingencia': int(identificador.tipoContingencia) if identificador.tipoContingencia else None,
            'motivoContin': identificador.motivoContin,
            'fechaEmi': fechaEmi,
            'horaEmi': horaEmi,
            'tipoMoneda': identificador.tipoMoneda
        },
        'donatorio': {
            "tipoDocumento":"nit",
            "numDocumento": comprobanteDonacion.emisor.nit,
            "nrc": comprobanteDonacion.emisor.nrc,
            "nombre": comprobanteDonacion.emisor.razonSocial,
            "codActividad": comprobanteDonacion.emisor.actividadEconomica.codigo,
            "descActividad": comprobanteDonacion.emisor.actividadEconomica.valor,
            "nombreComercial": comprobanteDonacion.emisor.razonSocial,
            "tipoEstablecimiento": comprobanteDonacion.tipoEstablecimiento,
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
            "valorTotal" : serialize(comprobanteDonacion.valorTotal),
            "totalLetras" : comprobanteDonacion.totalLetras,
            "pagos" : [],
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
    
    for cuerpoDoc in cuerpoDocumento:
        cuerpoDocumentoData = {
            "numItem": serialize(cuerpoDoc.numItem),
            "tipoDonacion": int(cuerpoDoc.tipoDonacion),
            "cantidad": serialize(cuerpoDoc.cantidad),
            "codigo": cuerpoDoc.codigo,
            "uniMedida": cuerpoDoc.uniMedida.codigo,
            "descripccion": cuerpoDoc.descripccion,
            "depreciacion": serialize(cuerpoDoc.depreciacion),
            "montoDescu": serialize(cuerpoDoc.montoDescu),
            "valorUni": serialize(cuerpoDoc.valorUni),
            "valor": serialize(cuerpoDoc.valor)
        }
        comprobanteData['cuerpoDocumento'].append(cuerpoDocumentoData)
    
    if apendiceComprobanteDonacion.exists():
        for apendices in apendiceComprobanteDonacion:
            apendicesData = {
                "campo": apendices.campo,
                "etiquta": apendices.etiquta,
                "valor": apendices.valor
            }
            comprobanteData['apendice'].append(apendicesData)
    else:
        comprobanteData['apendice'] = None
    
    if comprobanteDonacion.pago.exists():
        pagoData ={
            "codigo" : comprobanteDonacion.pago.codigo,
            "montoPago" : serialize(comprobanteDonacion.pago.montoPago),
            "referencia" : comprobanteDonacion.pago.referencia,
        }
        comprobanteData["resumen"]["pagos"].append(pagoData)
    else:
        comprobanteData["resumen"]["pagos"] = None
    
    return comprobanteData

def facturaElectronicaList(id):
    facturaElectronica = ComprobanteDonacion.objects.get(id=id)
    identificador = Identificador.objects.filter(facturaElectronica=facturaElectronica)
    extencion = Extencion.objects.filter(facturaElectronica=facturaElectronica)
    documentoRelacionado = DocumentoRelacionado.objects.filter(facturaElectronica=facturaElectronica)
    otroDocumento = OtroDocumento.objects.filter(facturaElectronica=facturaElectronica)
    ventaTercero = VentaTercero.objects.filter(facturaElectronica=facturaElectronica)
    documento = Documento.objects.filter(facturaElectronica=facturaElectronica)
    apendiceFacturaElectronica = Apendice.objects.filter(facturaElectronica=facturaElectronica)
    fechaEmi = facturaElectronica.fechaTransmicion.date().isoformat()
    horaEmi = facturaElectronica.fechaTransmicion.strftime("%H:%M:%S")
    
    def serialize(obj):
        if isinstance(obj,(datetime.date, datetime.datetime)):
            return obj.isoformat()
        if isinstance(obj, Decimal):
            return float(obj)
        if isinstance(obj, UUID):
            return str(obj)
        if isinstance(obj, TipoDocumento):
            return str(obj)
        if isinstance(obj, FormaPago):
            return str(obj)
        raise TypeError("Type not serializable")
    
    facturaData = {
        'identificacion': {
            'version': int(identificador.version),
            'ambiente': identificador.ambiente,
            'tipoDte': identificador.tipoDte.codigo,
            'numeroControl': identificador.numeroControl,
            'codigoGeneracion': str(identificador.codigoGeneracion).upper(),
            'tipoModelo': int(identificador.tipoModelo),
            'tipoOperacion': int(identificador.tipoOperacion),
            'tipoContingencia': int(identificador.tipoContingencia) if identificador.tipoContingencia else None,
            'motivoContin': identificador.motivoContin,
            'fechaEmi': fechaEmi,
            'horaEmi': horaEmi,
            'tipoMoneda': identificador.tipoMoneda
        },
        "documentoRelacionado":[],
        'emisor': {
            "nit": facturaElectronica.emisor.nit,
            "nrc": facturaElectronica.emisor.nrc,
            "nombre": facturaElectronica.emisor.razonSocial,
            "codActividad": facturaElectronica.emisor.actividadEconomica.codigo,
            "descActividad": facturaElectronica.emisor.actividadEconomica.valor,
            "nombreComercial": facturaElectronica.emisor.razonSocial,
            "tipoEstablecimiento": facturaElectronica.tipoEstablecimiento,
            "direccion": {
                "departamento": facturaElectronica.emisor.direccionEmisor.municipio.departamento.codigo,
                "municipio": facturaElectronica.emisor.direccionEmisor.municipio.codigo,
                "complemento": facturaElectronica.emisor.direccionEmisor.complementoDireccion,
            },
            "telefono": facturaElectronica.emisor.cellphone,
            "correo": facturaElectronica.emisor.email,
            "codEstableMH": facturaElectronica.emisor.codEstableMH,
            "codEstable": facturaElectronica.emisor.codEstable,
            "codPuntoVentaMH": facturaElectronica.emisor.codPuntoVentaMH,
            "codPuntoVenta": facturaElectronica.emisor.codPuntoVenta,
            
        },
        "receptor": {
            "tipoDocumento": facturaElectronica.receptor.tipo,
            "numDocumento": facturaElectronica.receptor.numero,
            "nrc": facturaElectronica.receptor.nrc,
            "nombre": facturaElectronica.receptor.receptor.nombre,
            "codActividad": facturaElectronica.receptor.actividadEconomica.codigo,
            "descActividad": facturaElectronica.receptor.actividadEconomica.valor,
            "direccion": {
                "departamento": facturaElectronica.receptor.direccionReceptor.municipio.departamento.codigo,
                "municipio": facturaElectronica.receptor.direccionReceptor.municipio.codigo,
                "complemento": facturaElectronica.receptor.direccionReceptor.complementoDireccion
            },
            "telefono": facturaElectronica.receptor.cellphone,
            "correo": facturaElectronica.receptor.email,
        },
        "otrosDocumentos":[],
        "ventaTercero": {
            "nit": ventaTercero.nit,
            "nombre": ventaTercero.nombre
        },
        "cuerpoDocumento":[],
        "resumen": {
            "totalNoSuj" : serialize(facturaElectronica.totalNoSuj),
            "totalExenta" : serialize(facturaElectronica.totalExenta),
            "totalGravada" : serialize(facturaElectronica.totalGravada),
            "subTotalVentas" : serialize(facturaElectronica.subTotalVentas),
            "descuNoSuj" : serialize(facturaElectronica.descuNoSuj),
            "descuExenta" : serialize(facturaElectronica.descuExenta),
            "descuGravada" : serialize(facturaElectronica.descuGravada),
            "porcentajeDescuento" : serialize(facturaElectronica.porcentajeDescuento),
            "totalDescu" : serialize(facturaElectronica.totalDescu),
            "tributos" : {
                "codigo" : facturaElectronica.tributo.codigo,
                "descripcion" : facturaElectronica.tributo.descripcion,
                "valor" : serialize(facturaElectronica.tributo.valor), 
            },
            "subtotal" : serialize(facturaElectronica.subtotal),
            "ivaRete1" : serialize(facturaElectronica.ivaRete1),
            "reteRenta" : serialize(facturaElectronica.reteRenta),
            "montoTotalOperacion" : serialize(facturaElectronica.montoTotalOperacion),
            "totalNoGravado" : serialize(facturaElectronica.totalNoGravado),
            "totalPagar" : serialize(facturaElectronica.totalPagar),
            "totalLetras" : facturaElectronica.totalLetras,
            "totalIva" : serialize(facturaElectronica.totalIva),
            "saldoFavor" : serialize(facturaElectronica.saldoFavor),
            "condicionOperacion" : facturaElectronica.condicionOperacion,
            "pagos" : [],
            "numPagoElectronica" : facturaElectronica.numPagoElectronica,
        },
        "Extencion" : {
            "nombEntrega" : extencion.nombEntrega,
            "docuEntrega" : extencion.docuEntrega,
            "nombRecibe" : extencion.nombRecibe,
            "docuRecibe" : extencion.docuRecibe,
            "observaciones" : extencion.observaciones,
            "placaVehiculo" : extencion.placaVehiculo,
        },
        "apendice": []
    }
    for documento in documentoRelacionado:
        documentoRelacionadoData = {
            "tipoDocumento" : documento.tipoDocumento,
            "tipoGeneracion" : documento.tipoGeneracion,
            "numeroDocumento" : documento.numeroDocumento,
            "fechaEmision" : documento.fechaEmision.date().isoformat(),
        }
        facturaData['otrosDocumentos'].append(documentoRelacionadoData)
    
    for otroDoc in otroDocumento:
        otroDocumentoData = {
            "codDocAsociado": otroDoc.codDocAsociado,
            "descDocumento": otroDoc.descDocumento,
            "detalleDocumento": otroDoc.detalleDocumento,
            "medico": {
                "nombre" : otroDoc.medico.nombre,
                "nit" : otroDoc.medico.nit,
                "docIdentificacion" : otroDoc.medico.docIdentificacion,
                "tipoServicio" : otroDoc.medico.tipoServicio,
            },
        }
        facturaData['cuerpoDocumento'].append(otroDocumentoData)
    
    if apendiceFacturaElectronica.exists():
        for apendices in apendiceFacturaElectronica:
            apendicesData = {
                "campo": apendices.campo,
                "etiquta": apendices.etiquta,
                "valor": apendices.valor
            }
            facturaData['apendice'].append(apendicesData)
    else:
        facturaData['apendice'] = None
    
    if facturaElectronica.pago.exists():
        pagoData ={
            "codigo" : facturaElectronica.pago.codigo,
            "montoPago" : serialize(facturaElectronica.pago.montoPago),
            "referencia" : facturaElectronica.pago.referencia,
            "plazo" : facturaElectronica.pago.plazo,
            "periodo" : serialize(facturaElectronica.pago.periodo),
        }
        facturaData["resumen"]["pagos"].append(pagoData)
    else:
        facturaData["resumen"]["pagos"] = None
    
    return facturaData

#Creando los PDF's para cada Factura


def cargarDatosFactura(factura):
    # Si 'factura' es una cadena JSON, conviértelo a un diccionario
    if isinstance(factura, str):
        datos = json.loads(factura)
    # Si 'factura' es un diccionario ya parseado, úsalo directamente
    elif isinstance(factura, dict):
        datos = factura
    else:
        raise ValueError("El parámetro 'factura' debe ser una cadena JSON o un diccionario")
    
    return datos



def crearFacturaSujetoExcluido(datos):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    ancho, alto = letter
    margen = 50
    espaciado = 15
    y_pos = alto - margen

    # Encabezado de la factura
    c.setFont("Helvetica-Bold", 20)
    c.drawString(margen, y_pos, "Factura de Sujeto Excluido")
    y_pos -= 2 * espaciado

    # Identificador
    c.setFont("Helvetica-Bold", 14)
    c.drawString(margen, y_pos, "Identificador")
    y_pos -= 2 * espaciado

    identificador = datos["identificacion"]
    c.setFont("Helvetica", 10)
    info_identificador = [
        f'Version: {identificador["version"]}, Tipo: {identificador["tipoDte"]}, Numero de Control: {identificador["numeroControl"]}',
        f'Codigo de Generacion: {identificador["codigoGeneracion"]}, Fecha: {identificador["fecEmi"]}, Hora: {identificador["horEmi"]}',
        f'Modelo de Facturacion: {identificador["tipoModelo"]}, Tipo de Transmision: {identificador["tipoOperacion"]}',
        f'Tipo de Contingencia: {identificador["tipoContingencia"]}, Motivo: {identificador["motivoContin"]}, Moneda: {identificador["tipoMoneda"]}'
    ]
    for info in info_identificador:
        c.drawString(margen, y_pos, info)
        y_pos -= espaciado

    y_pos -= 2 * espaciado
    # Información del Emisor
    c.setFont("Helvetica-Bold", 14)
    c.drawString(margen, y_pos, "Datos del Emisor de la Factura")
    y_pos -= 2 * espaciado

    emisor = datos["emisor"]
    direccion = emisor["direccion"]
    c.setFont("Helvetica", 10)
    info_emisor = [
        f'NIT: {emisor["nit"]}, NRC: {emisor["nrc"]}',
        f'Razon Social: {emisor["nombre"]}',
        f'Actividad Economica: {emisor["descActividad"]}, Email: {emisor["correo"]}',
        f'Codigo Establecimiento MH: {emisor["codEstableMH"]}, Contribuyente: {emisor["codEstable"]}',
        f'Direccion: {direccion["complemento"]}, {direccion["municipio"]}, {direccion["departamento"]}, Telefono: {emisor["telefono"]}'
    ]
    for info in info_emisor:
        c.drawString(margen, y_pos, info)
        y_pos -= espaciado

    y_pos -= 2 * espaciado
    # Información del Sujeto Excluido
    c.setFont("Helvetica-Bold", 14)
    c.drawString(margen, y_pos, "Datos del Sujeto Excluido")
    y_pos -= 2 * espaciado

    sujeto_excluido = datos["sujetoExcluido"]
    direccion_s = sujeto_excluido["direccion"]
    c.setFont("Helvetica", 10)
    info_sujeto = [
        f'Nombre: {sujeto_excluido["nombre"]}, Tipo Documento: {sujeto_excluido["tipoDocumento"]}, Documento: {sujeto_excluido["numDocumento"]}',
        f'Actividad Economica: {sujeto_excluido["descActividad"]}',
        f'Email: {sujeto_excluido["correo"]}, Telefono: {sujeto_excluido["telefono"]}',
        f'Direccion: {direccion_s["complemento"]}, {direccion_s["municipio"]}, {direccion_s["departamento"]}'
    ]
    for info in info_sujeto:
        c.drawString(margen, y_pos, info)
        y_pos -= espaciado

    y_pos -= 2 * espaciado
    # Operaciones (Tabla)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(margen, y_pos, "Operaciones")
    y_pos -= 2 * espaciado

    c.setFont("Helvetica-Bold", 10)
    c.drawString(margen, y_pos, "Item")
    c.drawString(margen + 50, y_pos, "Tipo")
    c.drawString(margen + 100, y_pos, "Codigo")
    c.drawString(margen + 150, y_pos, "Cantidad")
    c.drawString(margen + 200, y_pos, "Compra")
    c.drawString(margen + 250, y_pos, "Precio Unitario")
    y_pos -= espaciado

    c.setFont("Helvetica", 10)
    for operacion in datos["cuerpoDocumento"]:
        c.drawString(margen, y_pos, str(operacion["numItem"]))
        c.drawString(margen + 50, y_pos, str(operacion["tipoItem"]))
        c.drawString(margen + 100, y_pos, str(operacion["codigo"]))
        c.drawString(margen + 150, y_pos, str(operacion["cantidad"]))
        c.drawString(margen + 200, y_pos, f'{operacion["compra"]:.2f}')
        c.drawString(margen + 250, y_pos, f'{operacion["precioUni"]:.2f}')
        y_pos -= espaciado

    y_pos -= 2 * espaciado
    # Resumen
    c.setFont("Helvetica-Bold", 14)
    c.drawString(margen, y_pos, "Resumen")
    y_pos -= 2 * espaciado

    resumen = datos["resumen"]
    c.setFont("Helvetica", 10)
    resumen_info = [
        f'Condicion de operacion: {resumen["condicionOperacion"]}, Compra: {resumen["totalCompra"]}, Descuento: {resumen["descu"]}',
        f'Total Descuento: {resumen["totalDescu"]}, Subtotal: {resumen["subTotal"]}, Total a pagar: {resumen["totalPagar"]}',
        f'Total en letras: {resumen["totalLetras"]}'
    ]
    for info in resumen_info:
        c.drawString(margen, y_pos, info)
        y_pos -= espaciado

    if datos['apendice'] == None:
        c.setFont("Helvetica-Bold", 10)
        c.drawString(margen, y_pos, "No hay datos")
    else:   
        #Apendice
        c.setFont("Helvetica-Bold", 10)
        c.drawString(margen + 50, y_pos, "Campo")
        c.drawString(margen + 100, y_pos, "Descripccion")
        c.drawString(margen + 150, y_pos, "Valor")
        y_pos -= espaciado
        
        #Lista de Apendices
        for apendice in datos["apendice"]:
            c.drawString(margen + 50, y_pos, apendice["campo"])
            c.drawString(margen + 100, y_pos, apendice["etiqueta"])
            c.drawString(margen + 150, y_pos, apendice["valor"])
            y_pos -= espaciado
        
        y_pos -= 2 * espaciado
    
    # Guardar el PDF
    c.save()
    buffer.seek(0)

    # Devolver el PDF como una respuesta HTTP
    #response = HttpResponse(buffer.getvalue(), content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="factura_sujeto_excluido.pdf"'
    
    #return response
    return buffer.getvalue()

def generar_pdf_view(request, id):
    # Aquí obtienes los datos necesarios para generar el PDF
    datos = sujetoExcluidoList(id)  # Usas la función que ya tienes para obtener los datos
    
    # Generas el PDF y lo devuelves como respuesta
    return crearFacturaSujetoExcluido(datos)

def crearComprobanteDonacion(datos):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    ancho, alto =letter
    margen = 50
    espaciado = 15
    y_pos = alto - margen
    
    # Encabezado de la factura
    c.setFont("Helvetica-Bold", 20)
    c.drawString(30, alto - 50, "Comprobante de Donacion")
    y_pos -= 2 * espaciado
    
    # Identificador
    c.setFont("Helvetica-Bold", 15)
    c.drawString(margen, y_pos, "Identificador")
    y_pos -= 2 * espaciado
    
    identificador = datos["identiificacion"]
    c.setFont("Helvetica", 10)
    info_identificador = [
        f'Version: {identificador["version"]}, Tipo: {identificador["tipoDte"]}, Numero de Control: {identificador["numeroControl"]}',
        f'Codigo de Generacion: {identificador["codigoGeneracion"]}, Fecha: {identificador["fecEmi"]}, Hora: {identificador["horEmi"]}',
        f'Modelo de Facturacion: {identificador["tipoModelo"]}, Tipo de Transmision: {identificador["tipoOperacion"]}',
        f'Tipo de Contingencia: {identificador["tipoContingencia"]}, Motivo: {identificador["motivoContin"]}, Moneda: {identificador["tipoMoneda"]}'
    ]
    for info in info_identificador:
        c.drawString(margen, y_pos, info)
        y_pos -= espaciado

    y_pos -= 2 * espaciado
    
    # Información del Donatorio
    c.setFont("Helvetica-Bold", 14)
    c.drawString(margen, y_pos, "Datos del Donatorio del Comprobante de Donacion")
    y_pos -= 2 * espaciado
    
    emisor = datos["donatorio"]
    direccion = emisor["direccion"]
    c.setFont("Helvetica-Bold",10)
    info_emisor = [
        f'NIT: {emisor["nit"]}, NRC: {emisor["nrc"]}',
        f'Razon Social: {emisor["nombre"]}, Tipo de establecimiento: {emisor["tipoEstablecimiento"]}',
        f'Actividad Economica: {emisor["descActividad"]}, Nombre Comercial: {emisor["nombreComercial"]}, Email: {emisor["correo"]}',
        f'Codigo Establecimiento MH: {emisor["codEstableMH"]}, Contribuyente: {emisor["codEstable"]}',
        f'Codigo del punto de venta por MH: {emisor["codPuntoVentaMH"]}  Codigo del punto de venta por el contribuyente: {emisor["codPuntoVenta"]}',
        f'Direccion: {direccion["complemento"]}, {direccion["municipio"]}, {direccion["departamento"]}, Telefono: {emisor["telefono"]}'
    ]
    for info in info_emisor:
        c.drawString(margen, y_pos, info)
        y_pos -= espaciado

    y_pos -= 2 * espaciado
    
    # Informacion del Donante 
    c.setFont("Helvetica-Bold", 14)
    c.drawString(margen, y_pos, "Datos del Donante")
    y_pos -= 2 * espaciado
    
    donante = datos["donante"]
    direccionD = datos["direccion"]
    c.setFont("Helvetica-Bold",10)
    info_donante = [
        f'Nombre: {donante["nombre"]}, Tipo Documento: {donante["tipoDocumento"]}, Documento: {donante["numDocumento"]}',
        f'Actividad Economica: {donante["descActividad"]}, NRC: {donante["nrc"]}',
        f'Email: {donante["correo"]}, Telefono: {donante["telefono"]}',
        f'Direccion: {direccionD["complemento"]}, {direccionD["municipio"]}, {direccionD["departamento"]}'
    ]
    for info in info_donante:
        c.drawString(margen, y_pos, info)
        y_pos -= espaciado

    y_pos -= 2 * espaciado
    
    #Otros documentos Asociados
    c.setFont("Helvetica-Bold", 10)
    c.drawString(margen, y_pos, "Item")
    c.drawString(margen + 50, y_pos, "Documento Asociado")
    c.drawString(margen + 100, y_pos, "Identificador del Documento Asociado")
    c.drawString(margen + 150, y_pos, "Descripccion del Documento Asociado")
    y_pos -= espaciado
    
    #Lista de otros Documentos Asociados
    c.setFont("Helvetica", 10)
    for otroDocumento in datos["otrosDocumentos"]:
        c.drawString(margen + 50, y_pos, otroDocumento["codDocAsociado"])
        c.drawString(margen + 100, y_pos,  otroDocumento["descDocumento"])
        c.drawString(margen + 150, y_pos, otroDocumento["detalleDocumento"])
        y_pos -= espaciado
    
    y_pos -= 2 * espaciado
     
    #Cuerpo del Documento
    c.setFont("Helvetica-Bold", 10)
    c.drawString(margen, y_pos, "Operaciones")
    c.drawString(margen + 50, y_pos, "Numero de Item")
    c.drawString(margen + 100, y_pos, "Tipo de Donacion")
    c.drawString(margen + 150, y_pos, "Codigo")
    c.drawString(margen + 200, y_pos, "Unidad de Medida")
    c.drawString(margen + 250, y_pos, "Cantidad")
    c.drawString(margen + 300, y_pos, "Monto")
    c.drawString(margen + 350, y_pos, "Valor Unitario")
    c.drawString(margen + 400, y_pos, "Valor")
    c.drawString(margen + 450, y_pos, "Depreciacion")
    c.drawString(margen + 500, y_pos, "Descripccion")
    y_pos -= espaciado
    
    #Lista de Donaciones
    c.setFont("Helvetica", 10)
    for operaciones in datos["cuerpoDocumento"]:
        numItem = operaciones["numItem"]
        tipoItem = operaciones["tipoDonacion"]
        codigo = operaciones["codigo"]
        uniMedida = operaciones["uniMedida"]
        cantidad = operaciones["cantidad"]
        montoDescu = operaciones["montoDescu"]
        valorUni = operaciones["valorUni"]
        valor = operaciones["valor"]
        depreciacion = operaciones["depreciacion"]
        descripccion = operaciones["descripccion"]
        
        c.drawString(margen + 50, y_pos, numItem)
        c.drawString(margen + 100, y_pos, tipoItem)
        c.drawString(margen + 150, y_pos, codigo)
        c.drawString(margen + 200, y_pos, uniMedida)
        c.drawString(margen + 250, y_pos, cantidad)
        c.drawString(margen + 300, y_pos, f"${montoDescu:.2f}")
        c.drawString(margen + 350, y_pos, f"${valorUni:.2f}")
        c.drawString(margen + 400, y_pos, f"${valor:.2f}")
        c.drawString(margen + 450, y_pos, depreciacion)
        c.drawString(margen + 500, y_pos, descripccion)
        y_pos -= espaciado
    
    y_pos -= 2 * espaciado
    
    #Resumen
    c.setFont("Helvetica-Bold", 14)
    c.drawString(margen, y_pos, "Resumen")
    y_pos -= 2 * espaciado
    
    resumen = datos["resumen"]
    pagos = resumen["pagos"]
    if pagos == None:
        p = f'No hay pagos',
    else:
        p = f'Codigo: {pagos["codigo"]}, Monto del pago: {pagos["montoPagos"]}, Referencia: {pagos["referencia"]}' 
    c.setFont("Helvetica", 10)
    resumen_info = [
       f'Valor total: {resumen["valorTotal"]}, Total en letras: {resumen["totalLetras"]}',
       p,
           
    ]
    for info in resumen_info:
        c.drawString(margen, y_pos, info)
        y_pos -= espaciado
    
    y_pos -= 2 * espaciado
    
    #Apendice
    if datos['apendice'] == None:
        c.setFont("Helvetica-Bold", 10)
        c.drawString(margen, y_pos, "No hay datos")
    else:   
        #Apendice
        c.setFont("Helvetica-Bold", 10)
        c.drawString(margen + 50, y_pos, "Campo")
        c.drawString(margen + 100, y_pos, "Descripccion")
        c.drawString(margen + 150, y_pos, "Valor")
        y_pos -= espaciado
        
        #Lista de Apendices
        for apendice in datos["apendice"]:
            c.drawString(margen + 50, y_pos, apendice["campo"])
            c.drawString(margen + 100, y_pos, apendice["etiqueta"])
            c.drawString(margen + 150, y_pos, apendice["valor"])
            y_pos -= espaciado
        
        y_pos -= 2 * espaciado
    
    #Guardar El PDF
    c.save()
    buffer.seek(0)
    
    return buffer.getvalue()
    
class Transmitir(LoginRequiredMixin,View):
    
    
    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        return self.transmitir(request, *args, **kwargs)
    
    def obtenerFactura(self,*args, **kwargs):
        origin = self.request.POST.get('origin')
        id = self.kwargs.get('pk')
        
        if origin == 'sujetoExcluido':
            factura = sujetoExcluidoList(id)
        else:
            factura = comprobanteDonacionList(id)
        return factura
    
    def convert_base64_private_key_to_pem(self, base64_key):
        # Decodificar la clave base64
        key_der = base64_key.strip()
        
        # Encapsular la clave privada DER en formato PEM
        pem_key = "-----BEGIN PRIVATE KEY-----\n"
        pem_key += '\n'.join([key_der[i:i+64] for i in range(0, len(key_der), 64)])
        pem_key += "\n-----END PRIVATE KEY-----\n"
        
        return pem_key
    
    @csrf_exempt
    def transmitir(self, request,*args, **kwargs):
        id = self.kwargs.get('pk')
        
        #Generando el pdf a partir del json 
        jsonData = self.obtenerFactura(self, *args, **kwargs)
        #jsonData = json.loads(jsonData)  # Convierte el diccionario en JSON
       
        datosFactura = cargarDatosFactura(jsonData)
        print(datosFactura)
        origin = self.request.POST.get('origin')
        try:
            entidad = self.request.user.entidad
            authHacienda = get_object_or_404(ParametrosAuthHacienda,entidad=entidad)
            privateKey = self.convert_base64_private_key_to_pem(authHacienda.privateKey)
            url_auth = 'https://apitest.dtes.mh.gob.sv/seguridad/auth'
               
            parametros_auth = {
                'content_Type' : 'application/x-www-form-urlencoded',
                'User-Agent ': authHacienda.userAgent,
                'user' : authHacienda.nit,
                'pwd' : authHacienda.pwd,
                }

            acceso = requests.post(url_auth, params=parametros_auth).json()
            
            if origin == 'sujetoExcluido':
                sujetoExcluido = get_object_or_404(SujetoExcluido, pk=id)
                identificador = get_object_or_404(Identificador, sujetoExcluido=sujetoExcluido)               
                responseHacienda = ResponseHacienda(
                    nombre="Auth de Hacienda",
                    datosJson=acceso,  # Corregido el nombre del campo y la serialización JSON
                    status=acceso['status'],
                    sujetoExcluido=sujetoExcluido
                )
                responseHacienda.save()
                if acceso['status'] == 'OK':
                    token = acceso['body']['token']
                    
                    factura = self.obtenerFactura()
                    print(factura)
                    encoded = jwt.encode(factura, privateKey, algorithm="RS512")
                    url_recepcion = 'https://apitest.dtes.mh.gob.sv/fesv/recepciondte'
                    headers = {
                        'Authorization':token,
                        'User-Agent': "Piraña3000",
                        'content-Type': 'application/JSON',  # Asegúrate de que sea 'application/json'
                    }
                    
                    data = {
                        'ambiente': identificador.ambiente,
                        'idEnvio': identificador.id,
                        'version': identificador.version,
                        'tipoDte': identificador.tipoDte.codigo,
                        'documento': encoded,
                        'codigoGeneracion': str(identificador.codigoGeneracion).upper(),
                    }
                    
                    try:
                        transmitir = requests.post(url_recepcion, headers=headers, json=data).json()
                        print(transmitir)
                        responseHacienda = ResponseHacienda(
                            nombre="Transmicion de factura a Hacienda",
                            datosJson=transmitir,  # Asegúrate de que los datos sean correctos
                            status=transmitir['codigoMsg'],
                            sujetoExcluido=sujetoExcluido
                        )
                        responseHacienda.save()    
                    except requests.exceptions.HTTPError as e:
                        messages.error(self.request,f"Error en la solicitud: {e}")
                    except ValueError as json_err:
                        messages.error(self.request,f"Error al decodificar JSON: {json_err}")
                        messages.error(self.request,f"Contenido de la respuesta: {transmitir.text}")
                    
                    if transmitir['codigoMsg'] == "001":
                        SujetoExcluido.objects.filter(pk=id).update(transmitido=True)  # Actualizar el campo transmitido
                        # Envía un correo electrónico con la factura electrónica
                        subject = 'Factura Sujeto Excluido'
                        body = f'Hola {sujetoExcluido.receptor.nombre},\n\nse le ha emitido una factura de sujeto excluido.'
                        from_email = sujetoExcluido.emisor.email  
                        to_email = sujetoExcluido.receptor.email
                        email = EmailMessage(subject, body, from_email, [to_email])
                        jsonContent = json.dumps(jsonData, indent=4)
                        pdf_bytes = crearFacturaSujetoExcluido(datosFactura)
                        pdf_sujeto_excluido = MIMEApplication(pdf_bytes, _subtype='pdf')
                        email.attach('data.json', jsonContent, 'application/json')
                        email.attach('data.pdf', pdf_bytes, 'application/pdf')
                        email.send()
                        messages.success(self.request, 'Se ha transmitido la factura correctamente.')
                        return redirect('sujetoExcluidoDetailView', pk=id)
                    else:
                       messages.warning(self.request, 'No se pudo transmitir la factura correctamente.')
                       return redirect('sujetoExcluidoDetailView', pk=id)  
                else:
                    messages.error(self.request, f'Ocurrió un error con las credenciales: {acceso["status"]}')
                    return redirect('updateParametrosHacienda', pk=authHacienda.pk)
            else:
                comprobanteDonacion = get_object_or_404(ComprobanteDonacion, pk=id)
                identificador = get_object_or_404(Identificador, comprobanteDonacion=comprobanteDonacion)
                responseHacienda = ResponseHacienda(
                    nombre="Auth de Hacienda",
                    datosJson=acceso,  # Corregido el nombre del campo y la serialización JSON
                    status=acceso['status'],
                    comprobanteDonacion=ComprobanteDonacion
                )
                responseHacienda.save()

                if acceso['status'] == "OK":
                    token = acceso['body']['token']
                    factura = self.obtenerFactura()
                    encoded = jwt.encode(factura, privateKey, algorithm="HS256")
                    print(encoded)
                    url_recepcion = 'https://apitest.dtes.mh.gob.sv/fesv/recepciondte'

                    headers = {
                        'Authorization':token,
                        'User-Agent': authHacienda.userAgent,
                        'content-Type': 'application/json',  # Asegúrate de que sea 'application/json'
                    }
                    
                    data = {
                        'ambiente': identificador.ambiente,
                        'idEnvio': identificador.id,
                        'version': identificador.version,
                        'tipoDte': identificador.tipoDte.codigo,
                        'documento': encoded,
                        'codigoGeneracion': str(identificador.codigoGeneracion).upper(),
                    }
                    try:
                        transmitir = requests.post(url_recepcion, headers=headers, json=data).json()
                        responseHacienda = ResponseHacienda(
                            nombre="Transmicion de factura a Hacienda",
                            datosJson=transmitir,  # Corregido el nombre del campo y la serialización JSON
                            status=transmitir['status'],
                            comprobanteDonacion=ComprobanteDonacion
                        )
                        responseHacienda.save()
                    except requests.exceptions.HTTPError as e:
                        messages.error(self.request,f"Error en la solicitud: {e}")
                    except ValueError as json_err:
                        messages.error(self.request,f"Error al decodificar JSON: {json_err}")
                        messages.error(self.request,f"Contenido de la respuesta: {transmitir.text}")
                    
                    if transmitir['codigoMsg'] == "001":
                        ComprobanteDonacion.objects.filter(pk=id).update(transmitido=True)  # Actualizar el campo transmitido
                        # Envía un correo electrónico con el comprobante de donación
                        subject = 'Comprobante de Donación'
                        body = f'Hola {comprobanteDonacion.receptor.nombre},\n\nse le ha emitido un Comprobante de Donación.'
                        from_email = comprobanteDonacion.emisor.email  
                        to_email = comprobanteDonacion.receptor.email
                        email = EmailMessage(subject, body, from_email, [to_email])
                        jsonContent = json.dumps(jsonData, indent=4)
                        pdf_bytes = crearFacturaSujetoExcluido(datosFactura)
                        pdf_comprobante_donacion = MIMEApplication(pdf_bytes, _subtype='pdf')
                        email.attach('data.json', jsonContent, 'application/json')
                        email.attach('data.pdf', pdf_bytes, 'application/pdf')
                        email.send()
                    messages.success(self.request, 'Se ha transmitido el comprobante correctamente.')
                    return redirect('comprobanteDonacionDetailView', pk=id)
                else:
                    messages.error(self.request, f'Ocurrió un error con las credenciales: {acceso["status"]}')
                    return redirect('authHacienda', pk=authHacienda.pk)

        except requests.exceptions.RequestException as e:
            messages.error(self.request, f'Ocurrió un error al hacer la solicitud a la API de Hacienda: {str(e)}')
            if origin == 'sujetoExcluido':
                return redirect('sujetoExcluidoDetailView', pk=id)
            else:
                return redirect('comprobanteDonacionDetailView', pk=id)

        except Exception as e:
            messages.error(self.request, f'Ocurrió un error inesperado: {str(e)}')
            if origin == 'sujetoExcluido':
                return redirect('sujetoExcluidoDetailView', pk=id)
            else:
                return redirect('comprobanteDonacionDetailView', pk=id)
            