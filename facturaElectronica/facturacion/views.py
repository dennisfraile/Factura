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
        return super().get_success_url()
    

class PaisUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'forms comunes/pais_form.html'
    form_class = PaisForm
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return super().get_success_url()


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
        return super().get_success_url()
    

class DepartamentoUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'forms comunes/departamento_form.html'
    form_class = DepartamentoForm
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return super().get_success_url()    

    

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
        return super().get_success_url()
    
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
        return super().get_success_url()
    
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
        return super().get_success_url()    
    
    
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
        entidad = get_object_or_404(Entidad, razonSocial=self.request.user.entidad)
        direccion.entidad = entidad       
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
        return super().get_success_url()

    
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
        return super().get_success_url()
    

class UnidadMedidaUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'forms comunes/unidad_medida_form.html'
    form_class = UnidadMedidaForm
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return super().get_success_url()


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
        return super().get_success_url()
    
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
        return super().get_success_url()
    
    def form_valid(self, form):
        operacion = form.save(commit=False) 
        operacion.entidad = self.request.user.entidad      
        operacion.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['unidadMedida_id'] = self.get_object().unidadMedida.id if self.get_object().unidadMedida else None
        return context

class OperacionSujetoExcluidoDetailView(LoginRequiredMixin, DetailView):
    login_url = '/ingresar/'
    template_name = 'sujeto excluido/operacion_sujeto_excluido_by_id.html'
    model = OperacionesSujetoExcluido
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return super().get_success_url()
    
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
        sujeto = SujetoExcluido.objects.all(entidad=self.request.user.entidad)
        context['registro'] = sujeto
        return context

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
            identificador = Identificador.objects.filter(sujetoExcluido=sujetoExcluido)
            operaciones_sujeto_excluido = OperacionesSujetoExcluido.objects.filter(sujetoExcluido=sujetoExcluido)
            apendice = Apendice.objects.filter(sujetoExcluido=sujetoExcluido)
            
            context['identificador'] = identificador
            context['operacionesSujetoExcluido'] = operaciones_sujeto_excluido
            context['apendices'] = apendice
            context['show'] = True
        
        except identificador.DoesNotExist:
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
        return super().get_success_url()
    
    
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
    template_name = 'sujeto excluido/sujeto_excluido_create_view.html'
    form_class = SujetoExcluidoForm
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return super().get_success_url()

    def form_valid(self, form):
        form.instance.entidad = self.request.user.entidad  # Assuming you want to assign the first entity related to the user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['identificador_id'] = self.object.identificador.id if self.object.identificador else None
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
        return super().get_success_url()

class FormaPagoUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'sujeto excluido/forma_pago_form.html'
    form_class = FormaPagoForm
    model = FormaPago
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return super().get_success_url()


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
        return super().get_success_url()
    
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
        return super().get_success_url()

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
        return super().get_success_url()
    
    def get_initial(self):
        initial = super().get_initial()
        initial['sujetoExcluido'] = self.request.GET.get('sujetoExcluido')
        initial['comprobanteDonacion'] = self.request.GET.get('comprobanteDonacion')
        return initial
    
    def form_valid(self, form):
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
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return super().get_success_url()
    
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
        return super().get_success_url()
    
class TipoDocumentoUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'forms comunes/tipo_documento_form.html'
    form_class = TipoDocumentoForm
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return super().get_success_url()
    
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
        return super().get_success_url()
    
    def form_valid(self, form):
        origin = self.request.POST.get('origin')
        id = self.kwargs.get('pk')
        
        if origin == 'sujetoExcluido':
            sujetoExcluido = get_object_or_404(SujetoExcluido, pk=id)
            form.instance.sujetoExcluido = sujetoExcluido
        else:
            comprobanteDonacion = get_object_or_404(ComprobanteDonacion, pk=id)
            form.instance.comprobanteDonacion = comprobanteDonacion
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
        return super().get_success_url()

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
        return super().get_success_url()
    
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
        return super().get_success_url()

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
    template_name = 'otro_documento_asociado_view.html'
    model = OtroDocumentoAsociado
    
    def get_context_data(self, **kwargs) :
        context = super(OtroDocumentoAsociado, self).get_context(**kwargs)
        otroDocumentoAsociado = OtroDocumentoAsociado.objects.all()
        context['otroDocumentoAsociado'] = otroDocumentoAsociado
        return context
    
class OtroDocumentoAsociadoCreateView(LoginRequiredMixin,CreateView):
    
    login_url = '/ingresar'
    template_name = 'otro_documento_asociado_form.html'
    form_class = OtroDocumentoAsociadoForm
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return super().get_success_url()
    
    def form_valid(self, form):
        id=self.kwargs.get("id")
        comprobanteDonacion = get_object_or_404(ComprobanteDonacion, id=id)
        # Asegúrate de que la entidad no se modifique durante la actualización
        form.instance.entidad = self.request.user.entidad
        form.instance.comprobanteDonacion = comprobanteDonacion
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))
    
    

class OtroDocumentoAsociadoUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'otro_documento_asociado_form.html'
    form_class = OtroDocumentoAsociadoForm
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return super().get_success_url()

    def form_valid(self, form):
        # Asegúrate de que la entidad no se modifique durante la actualización
        form.instance.entidad = self.request.user.entidad
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))
    

class CuerpoDocumentoView(LoginRequiredMixin,View):
    
    login_url = '/ingresar/'
    template_name = 'cuerpo_documento_view.html'
    model = CuerpoDocumento
    
    def get_context_data(self, **kwargs) :
        context = super(CuerpoDocumento, self).get_context(**kwargs)
        cuerpoDocumento = CuerpoDocumento.objects.all()
        context['cuerpoDocumento'] = cuerpoDocumento
        return context
   
class CuerpoDocumentoCreateView(LoginRequiredMixin,CreateView):
    
    login_url = '/ingresar'
    template_name = 'cuerpo_documento_form.html'
    form_class = CuerpoDocumentoForm
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return super().get_success_url()
    
    def get_initial(self):
        initial = super().get_initial()
        initial['unidadMedida'] = self.request.GET.get('unidadMedida')
        return initial
    
    def form_valid(self, form):
        id=self.kwargs.get("id")
        comprobanteDonacion = get_object_or_404(ComprobanteDonacion, id=id)
        # Asegúrate de que la entidad no se modifique durante la actualización
        form.instance.entidad = self.request.user.entidad
        form.instance.comprobanteDonacion = comprobanteDonacion
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['unidadMedida_id'] = self.request.GET.get('unidadMedida_id')
        return context
    
class CuerpoDocumentoUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'cuerpo_documento_form.html'
    form_class = CuerpoDocumentoForm
    model = CuerpoDocumento
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return super().get_success_url()
    
    def form_valid(self, form):
        # Asegúrate de que la entidad no se modifique durante la actualización
        form.instance.entidad = self.request.user.entidad
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['unidadMedida_id'] = self.object.unidadMedida.id if self.object.unidadMedida else None
        return context

class PagoDonacionView(LoginRequiredMixin,View):
    
    login_url = '/ingresar/'
    template_name = 'pago_donacion_view.html'
    model = PagoDonacion
    
    def get_context_data(self, **kwargs) :
        context = super(PagoDonacion, self).get_context(**kwargs)
        pagoDonacion = PagoDonacion.objects.all()
        context['pagoDonacion'] = PagoDonacion
        return context
    
class PagoDonacionCreateView(LoginRequiredMixin,CreateView):
    
    login_url = '/ingresar'
    template_name = 'pago_donacion_form.html'
    form_class = PagoDonacionForm
    model = PagoDonacion
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return super().get_success_url()
    
    def form_valid(self, form):
        # Asegúrate de que la entidad no se modifique durante la actualización
        form.instance.entidad = self.request.user.entidad
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))
    

class PagoDonacionUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'pago_donacion_form.html'
    form_class = PagoDonacionForm
    model = PagoDonacion
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return super().get_success_url()
    
    def form_valid(self, form):
        # Asegúrate de que la entidad no se modifique durante la actualización
        form.instance.entidad = self.request.user.entidad
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))

class ComprobanteDonacionMonthView(LoginRequiredMixin,MonthArchiveView):
    """Muestra la lista de sujetos excluidos por mes"""

    login_url='/ingresar/'
    data_field = "fecha"
    queryset = ComprobanteDonacion.objects.all()
    template_name='comprobante donacion/comprobante_donacion_month.html'
    allow_empty = True
    allow_future = True

    def get_context_data(self, **kwargs) :
        context = super().get_context(**kwargs)
        comprobante = ComprobanteDonacion.objects.all(entidad=self.request.user.entidad)
        context['registro'] = comprobante
        return context

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
            identificador = get_object_or_404(Identificador, comprobanteDonacion=comprobanteDonacion)
            cuerpoDocumento = CuerpoDocumento.objects.filter(comprobanteDonacion=comprobanteDonacion)
            otroDocumentoAsociado = OtroDocumentoAsociado.objets.filter(comprobanteDonacion=comprobanteDonacion)
            apendice = Apendice.objects.filter(comprobanteDonacion=comprobanteDonacion)
            context['identificador'] = identificador
            context['otroDocumentoAsociado'] = otroDocumentoAsociado
            context['cuerpoDocumento'] = cuerpoDocumento
            context['apendice'] = apendice
            context['show'] = True
            return context   
        
        except identificador.DoesNotExist:
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
    template_name = 'comprobante donacion/comprobante_donacion_create_view.html'
    model = ComprobanteDonacion
    form_class = ComprobanteDonacionForm
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return super().get_success_url()
    
    def get_initial(self):
        initial = super().get_initial()
        initial['identificador'] = self.request.GET.get('identificador')
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
        context['identificador_id'] = self.request.GET.get('identificador_id')
        context['receptor_id'] = self.request.GET.get('receptor_id')
        context['pagoDonacion_id'] = self.request.GET.get('pagoDonacion_id')
        return context   
        
class ComprobanteDonacionUpdateView(LoginRequiredMixin, UpdateView):
    
    login_url = '/ingresar/'
    model = ComprobanteDonacion
    template_name = 'comprobante donacion/comprobante_donacion_create_view.html'
    form_class = ComprobanteDonacionForm    
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return super().get_success_url()

    def form_valid(self, form):
        form.instance.entidad = self.request.user.entidad  # Assuming you want to assign the first entity related to the user
        return super().form_valid(form)

    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['identificador_id'] = self.object.identificador.id if self.object.identificador else None
        context['receptor_id'] = self.object.receptor.id if self.object.receptor else None
        context['pagoDonacion_id'] = self.object.pagoDonacion.id if self.object.pagoDonacion else None
        return context


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

#Creando los Json correspondiente a cada factura


def sujetoExcluidoList(id):
    sujetoExcluido = SujetoExcluido.objects.get(id=id)
    identificador = Identificador.objects.filter(sujetoExcluido=sujetoExcluido)
    operacionesSujetoExcluido = OperacionesSujetoExcluido.objects.filter(sujetoExcluido=sujetoExcluido)
    apendiceSujetoExcluido = Apendice.objects.filter(sujetoExcluido=sujetoExcluido)
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
            'version': identificador.version,
            'ambiente': identificador.ambiente,
            'tipoDte': identificador.tipoDte.codigo,
            'numeroControl': identificador.numeroControl,
            'codigoGeneracion': serialize(identificador.codigoGeneracion),
            'tipoModelo': identificador.tipoModelo,
            'tipoOperacion': identificador.tipoOperacion,
            'tipoContingencia': identificador.tipoContingencia,
            'motivoContin': identificador.motivoContin,
            'fechaEmi': fechaEmi,
            'horaEmi': horaEmi,
            'tipoMoneda': identificador.tipoMoneda
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
            "retencionIVAMH": sujetoExcluido.retencionIVAMH,
            "ivaRete1" : serialize(sujetoExcluido.ivaRete1),
            "reteRenta" : serialize(sujetoExcluido.reteRenta),
            "totalPagar" : serialize(sujetoExcluido.totalPagar),
            "totalLetras" : sujetoExcluido.totalLetras,
            "condicionOperacion" : sujetoExcluido.condicionOperacion,
            "pagos" : [
                {
                    "codigo" : sujetoExcluido.pago.codigo,
                    "formaPago": sujetoExcluido.pago.formaPago.codigo,
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
            "tipoItem" : operacion.tipoItem,
            "codigo" : operacion.codigo,
            "uniMedida": operacion.uniMedida.codigo,
            "cantidad" : operacion.cantidad,
            "montoDescu": serialize(operacion.montoDescu),
            "compra": serialize(operacion.compra),
            "retencion": serialize(operacion.retencion),
            "descripcion" : operacion.descripccion,
            "precioUni": serialize(operacion.precioUni)
        }
        sujetoData['cuerpoDocumento'].append(operacionesData)
    
    for apendices in apendiceSujetoExcluido:
        apendicesData = {
            "campo": apendices.campo,
            "etiqueta": apendices.etiqueta,
            "valor": apendices.valor
        }
        sujetoData['apendice'].append(apendicesData)
    
    return json.dumps(sujetoData, default=serialize)


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
            'version': identificador.version,
            'ambiente': identificador.ambiente,
            'tipoDte': identificador.tipoDte.codigo,
            'numeroControl': identificador.numeroControl,
            'codigoGeneracion': serialize(identificador.codigoGeneracion),
            'tipoModelo': identificador.tipoModelo,
            'tipoOperacion': identificador.tipoOperacion,
            'tipoContingencia': identificador.tipoContingencia,
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
            "pagos" : [
                {
                    "codigo" : comprobanteDonacion.pago.codigo,
                    "montoPago" : serialize(comprobanteDonacion.pago.montoPago),
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
    
    for cuerpoDoc in cuerpoDocumento:
        cuerpoDocumentoData = {
            "numItem": serialize(cuerpoDoc.numItem),
            "tipoDonacion": cuerpoDoc.tipoDonacion,
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
    
    for apendices in apendiceComprobanteDonacion:
        apendicesData = {
            "campo": apendices.campo,
            "etiquta": apendices.etiquta,
            "valor": apendices.valor
        }
        comprobanteData['apendice'].append(apendicesData)
    
    return json.dump(comprobanteData, default=serialize)

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
    ancho, alto =letter
    
    # Encabezado de la factura
    c.setFont("Helvetica-Bold", 20)
    c.drawString(30, alto - 50, "Factura de Sujeto Excluido")
    
    # Identificador
    c.setFont("Helvetica-Bold", 15)
    c.drawString(30, alto - 50, "Identificador")
    identificador = datos["identiificacion"]
    info_identificador1 = f'Version: {identificador["version"]}   Tipo: {identificador["tipoDte"]}   Numero de Control: {identificador["numeroControl"]}'
    info_identificador2 = f'Codigo de Generacion: {identificador["codigoGeneracion"]}   Fecha: {identificador["fechaEmi"]}   Hora: {identificador["horaEmi"]}'
    info_identificador3 = f'Modelo de Facturacion: {identificador["tipoModelo"]}  Tipo de Transmicion: {identificador["tipoOpreacion"]}  Tipo de Contingencion: {identificador["tipoContingencia"]}'
    info_identificador4 = f'Tipo de Contingencion: {identificador["tipoContingencia"]}  Motivo de Contingencia: {identificador["motivoContin"]}  Tipo de moneda: {identificador["tipoMoneda"]}'
    c.setFont("Helvetica-Bold",12)
    c.drawString(30, alto - 80, info_identificador2)
    c.drawString(30, alto - 80, info_identificador1)  
    c.drawString(30, alto - 80, info_identificador3)
    c.drawString(30, alto - 80, info_identificador4)
    
    # Información del Emisor
    c.setFont("Helvetica-Bold", 15)
    c.drawString(30, alto - 50, "Datos del Emisor de la Factura")
    emisor = datos["Emisor"]
    info_emisor = f'NIT: {emisor["nit"]}  NRC: {emisor["nrc"]}  Razon Social: {emisor["razonSocial"]}  Actividad Economica: {emisor["descActividad"]}  Email: {emisor["email"]}'
    info_emisor2 = f'Codigo del establecimiento por MH: {emisor["codEstableMH"]}  Codigo del establecimiento por el contribuyente: {emisor["codEstable"]}'
    info_emisor3 = f'Codigo del punto de venta por MH: {emisor["codPuntoVentaMH"]}  Codigo del punto de venta por el contribuyente: {emisor["codPuntoVenta"]}'
    direccion = datos["direccion"]
    direccion_emisor = f'Direccion: {direccion["complemento"]}, {direccion["municipio"]}, {direccion["departamento"]}  Telefono: {info_emisor["telefono"]}'
    c.setFont("Helvetica-Bold",12)
    c.drawString(30, alto - 80, info_emisor)
    c.drawString(30, alto - 80, direccion_emisor)
    c.drawString(30, alto - 80, info_emisor2)
    c.drawString(30, alto - 80, info_emisor3)
    
    # Informacion del Sujeto Excluido 
    c.setFont("Helvetica-Bold", 15)
    c.drawString(30, alto - 50, "Datos del Sujeto Excluido")
    sujetoExcluido = datos["sujetoExcluido"]
    info_sujeto = f'Nombre: {sujetoExcluido["nombre"]}  Documento: {sujetoExcluido["numDocumento"]}  NRC: {sujetoExcluido["nrc"]}'
    info_sujeto2 = f' Actividad Economica: {sujetoExcluido["descActividad"]}, Email: {sujetoExcluido["email"]}  Telefono: {sujetoExcluido["telefono"]}'
    direccionS = datos["direccion"]
    direccion_sujeto = f'Direccion: {direccionS["complemento"]}, {direccionS["municipio"]}, {direccionS["departamento"]} '
    c.setFont("Helvetica-Bold",12)
    c.drawString(30, alto - 80, info_sujeto)
    c.drawString(30, alto - 80, info_sujeto2)
    c.drawString(30, alto - 80, direccion_sujeto)
    
    #Operaciones
    c.setFont("Helvetica-Bold", 15)
    c.drawString(30, alto - 50, "Operaciones")
    c.drawString(30, alto - 140, "Numero de Item")
    c.drawString(450, alto - 140, "Tipo de Item")
    c.drawString(250, alto - 140, "Codigo")
    c.drawString(450, alto - 140, "Unidad de Medida")
    c.drawString(350, alto - 140, "Cantidad")
    c.drawString(450, alto - 140, "Monto")
    c.drawString(450, alto - 140, "Compra")
    c.drawString(450, alto - 140, "Retencion")
    c.drawString(450, alto - 140, "Precio Unitario")
    c.drawString(450, alto - 140, "Descripccion")
    
    y = alto - 170
    
    #Lista de productos/servicios
    for operaciones in datos["cuerpoDocumento"]:
        numItem = operaciones["numItem"]
        tipoItem = operaciones["tipoItem"]
        codigo = operaciones["codigo"]
        uniMedida = operaciones["uniMedida"]
        cantidad = operaciones["cantidad"]
        montoDescu = operaciones["montoDescu"]
        compra = operaciones["compra"]
        retencion = operaciones["retencion"]
        precioUni = operaciones["precioUni"]
        descripccion = operaciones["descripccion"]
        
        c.drawString(100, y, numItem)
        c.drawString(100, y, tipoItem)
        c.drawString(100, y, codigo)
        c.drawString(150, y, uniMedida)
        c.drawString(150, y, cantidad)
        c.drawString(200, y, f"${montoDescu:.2f}")
        c.drawString(200, y, f"${compra:.2f}")
        c.drawString(200, y, f"${retencion:.2f}")
        c.drawString(200, y, f"${precioUni:.2f}")
        c.drawString(300, y, descripccion)
        
        y -= 20
        
    #Apendice
    c.setFont("Helvetica-Bold", 15)
    c.drawString(30, alto - 50, "Campo")
    c.drawString(30, alto - 140, "Descripccion")
    c.drawString(450, alto - 140, "Valor")
    
    z = alto - 170
    
    #Lista de Apendices
    for apendice in datos["apendice"]:
        campo = apendice["campo"]
        etiqueta = apendice["etiqueta"]
        valor = apendice["valor"]
        
        c.drawString(100, y, campo)
        c.drawString(100, y, etiqueta)
        c.drawString(100, y, valor)
        
        z -= 20
    
    #Guardar el PDF
    c.save()
    buffer.seek(0)
    
    return buffer.getvalue()


@login_required(redirect_field_name='/ingresar')
def crearComprobanteDonacion(datos):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    ancho, alto =letter
    
    # Encabezado de la factura
    c.setFont("Helvetica-Bold", 20)
    c.drawString(30, alto - 50, "Comprobante de Donacion")
    
    # Identificador
    c.setFont("Helvetica-Bold", 15)
    c.drawString(30, alto - 50, "Identificador")
    identificador = datos["identiificacion"]
    info_identificador1 = f'Version: {identificador["version"]}   Tipo: {identificador["tipoDte"]}   Numero de Control: {identificador["numeroControl"]}'
    info_identificador2 = f'Codigo de Generacion: {identificador["codigoGeneracion"]}   Fecha: {identificador["fechaEmi"]}   Hora: {identificador["horaEmi"]}'
    info_identificador3 = f'Modelo de Facturacion: {identificador["tipoModelo"]}  Tipo de Transmicion: {identificador["tipoOpreacion"]}  Tipo de Contingencion: {identificador["tipoContingencia"]}'
    info_identificador4 = f'Tipo de Contingencion: {identificador["tipoContingencia"]}  Motivo de Contingencia: {identificador["motivoContin"]}  Tipo de moneda: {identificador["tipoMoneda"]}'
    c.setFont("Helvetica-Bold",12)
    c.drawString(30, alto - 80, info_identificador2)
    c.drawString(30, alto - 80, info_identificador1)  
    c.drawString(30, alto - 80, info_identificador3)
    c.drawString(30, alto - 80, info_identificador4)
    
    # Información del Donatorio
    c.setFont("Helvetica-Bold", 15)
    c.drawString(30, alto - 50, "Datos del Donatorio del Comprobante de Donacion")
    emisor = datos["Emisor"]
    info_emisor = f'NIT: {emisor["nit"]}  NRC: {emisor["nrc"]}  Razon Social: {emisor["razonSocial"]}  Actividad Economica: {emisor["descActividad"]}  Email: {emisor["email"]}'
    info_emisor2 = f'Codigo del establecimiento por MH: {emisor["codEstableMH"]}  Codigo del establecimiento por el contribuyente: {emisor["codEstable"]}'
    info_emisor3 = f'Codigo del punto de venta por MH: {emisor["codPuntoVentaMH"]}  Codigo del punto de venta por el contribuyente: {emisor["codPuntoVenta"]}'
    direccion = datos["direccion"]
    direccion_emisor = f'Direccion: {direccion["complemento"]}, {direccion["municipio"]}, {direccion["departamento"]}  Telefono: {info_emisor["telefono"]}'
    c.setFont("Helvetica-Bold",12)
    c.drawString(30, alto - 80, info_emisor)
    c.drawString(30, alto - 80, direccion_emisor)
    c.drawString(30, alto - 80, info_emisor2)
    c.drawString(30, alto - 80, info_emisor3)
    
    # Informacion del Donante 
    c.setFont("Helvetica-Bold", 15)
    c.drawString(30, alto - 50, "Datos del Donante")
    sujetoExcluido = datos["sujetoExcluido"]
    info_sujeto = f'Nombre: {sujetoExcluido["nombre"]}  Documento: {sujetoExcluido["numDocumento"]}  NRC: {sujetoExcluido["nrc"]}'
    info_sujeto2 = f' Actividad Economica: {sujetoExcluido["descActividad"]}, Email: {sujetoExcluido["email"]}  Telefono: {sujetoExcluido["telefono"]}'
    direccionS = datos["direccion"]
    direccion_sujeto = f'Direccion: {direccionS["complemento"]}, {direccionS["municipio"]}, {direccionS["departamento"]} '
    c.setFont("Helvetica-Bold",12)
    c.drawString(30, alto - 80, info_sujeto)
    c.drawString(30, alto - 80, info_sujeto2)
    c.drawString(30, alto - 80, direccion_sujeto)
    
    #Otros documentos Asociados
    c.setFont("Helvetica-Bold", 15)
    c.drawString(30, alto - 50, "Documento Asociado")
    c.drawString(30, alto - 140, "Identificador del Documento Asociado")
    c.drawString(450, alto - 140, "Descripccion del Documento Asociado")
    
    y = alto - 170
    
    #Lista de otros Documentos Asociados
    for otroDocumento in datos["otrosDocumentos"]:
        codDocAsociado = otroDocumento["codDocAsociado"]
        descDocumento = otroDocumento["descDocumento"]
        detalleDocumento = otroDocumento["detalleDocumento"]
        
        c.drawString(100, y, codDocAsociado)
        c.drawString(100, y, descDocumento)
        c.drawString(100, y, detalleDocumento)
        
        y -= 20
     
    #Cuerpo del Documento
    c.setFont("Helvetica-Bold", 15)
    c.drawString(30, alto - 50, "Operaciones")
    c.drawString(30, alto - 140, "Numero de Item")
    c.drawString(450, alto - 140, "Tipo de Donacion")
    c.drawString(250, alto - 140, "Codigo")
    c.drawString(450, alto - 140, "Unidad de Medida")
    c.drawString(350, alto - 140, "Cantidad")
    c.drawString(450, alto - 140, "Monto")
    c.drawString(450, alto - 140, "Valor Unitario")
    c.drawString(450, alto - 140, "Valor")
    c.drawString(450, alto - 140, "Depreciacion")
    c.drawString(450, alto - 140, "Descripccion")
    
    x = alto - 170
    
    #Lista de Donaciones
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
        
        c.drawString(100, x, numItem)
        c.drawString(100, x, tipoItem)
        c.drawString(100, x, codigo)
        c.drawString(150, x, uniMedida)
        c.drawString(150, x, cantidad)
        c.drawString(200, x, f"${montoDescu:.2f}")
        c.drawString(200, x, f"${valorUni:.2f}")
        c.drawString(200, x, f"${valor:.2f}")
        c.drawString(200, x, depreciacion)
        c.drawString(300, x, descripccion)
        
        x -= 20
       
    #Apendice
    c.setFont("Helvetica-Bold", 15)
    c.drawString(30, alto - 50, "Campo")
    c.drawString(30, alto - 140, "Descripccion")
    c.drawString(450, alto - 140, "Valor")
    
    z = alto - 170
    
    #Lista de Apendices
    for apendice in datos["apendice"]:
        campo = apendice["campo"]
        etiqueta = apendice["etiqueta"]
        valor = apendice["valor"]
        
        c.drawString(100, z, campo)
        c.drawString(100, z, etiqueta)
        c.drawString(100, z, valor)
        
        z -= 20
    
    #Guardar El PDF
    c.save()
    buffer.seek(0)
    
    return buffer.getvalue()
    
class Transmitir(LoginRequiredMixin,View):
    
    
    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        return self.transmitir(request, *args, **kwargs)
    
    def obtenerFactura(self, request,*args, **kwargs):
        origin = self.request.POST.get('origin')
        id = self.kwargs.get('pk')
        
        if origin == 'sujetoExcluido':
            factura = sujetoExcluidoList(id)
        else:
            factura = comprobanteDonacionList(id)
        return factura
    
    @csrf_exempt
    def transmitir(self, request,*args, **kwargs):
        id = self.kwargs.get('pk')
        
        #Generando el pdf a partir del json 
        jsonData = self.obtenerFactura(request, *args, **kwargs)
        jsonData = json.dumps(jsonData)  # Convierte el diccionario en JSON
       
        datosFactura = cargarDatosFactura(jsonData)
        origin = self.request.POST.get('origin')
        try:
            if origin == 'sujetoExcluido':
                sujetoExcluido = get_object_or_404(SujetoExcluido, pk=id)
                identificador = get_object_or_404(Identificador, pk=sujetoExcluido.identificador.id)
            else:
                comprobanteDonacion = get_object_or_404(ComprobanteDonacion, pk=id)
                identificador = get_object_or_404(Identificador, pk=comprobanteDonacion.identificador.id)
            
            entidad = self.request.user.entidad
            print(entidad)
            authHacienda = get_object_or_404(ParametrosAuthHacienda,entidad=entidad)
            privateKey = authHacienda.privateKey
            print(privateKey)
            url_auth = 'https://apitest.dtes.mh.gob.sv/seguridad/auth'
            
            parametros_auth = {
                'content_Type' : 'application/x-www-form-urlencoded',
                'user_agent ': authHacienda.userAgent,
                'user' : authHacienda.user,
                'pwd' : authHacienda.pwd,
                }

            acceso = requests.post(url_auth, params=parametros_auth).json()

            responseHacienda = ResponseHacienda(
                nombre="Auth de Hacienda",
                datosJason=json.dumps(acceso),  # Corregido el nombre del campo y la serialización JSON
                stastus_code=acceso['status']
            )
            responseHacienda.save()
            
            if acceso['status'] == "OK":
                token = acceso['body']['token']
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

                transmitir = requests.post(url_recepcion, params=parametros_recepcion).json()

                responseHacienda = ResponseHacienda(
                    nombre="Transmicion de factura a Hacienda",
                    datosJason=json.dumps(transmitir),  # Corregido el nombre del campo y la serialización JSON
                    stastus_code=transmitir['status']
                )
                responseHacienda.save()
            
                if transmitir['codigoMsg'] == "001":
                    if origin == 'sujetoExcluido':
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
                        email.attach('data.pdf', pdf_sujeto_excluido, 'application/pdf')
                        email.send()
                    else:
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
                        email.attach('data.pdf', pdf_comprobante_donacion, 'application/pdf')
                        email.send()

                messages.success(self.request, 'Se ha transmitido la factura correctamente.')
                if origin == 'sujetoExcluido':
                    return redirect('sujetoExcluidoDetailView', pk=id)
                else:
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
            