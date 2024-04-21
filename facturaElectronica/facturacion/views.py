from django.shortcuts import render
from calendar import month
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http.response import HttpResponse
from .models import *
from .forms import *
from datetime import datetime, timedelta, date
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.views.generic.dates import MonthArchiveView, YearArchiveView
from django.views.generic.list import ListView
from django.views.generic import DetailView, View
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse, JsonResponse
# Create your views here.
    
class PaisView(View):
    
    login_url = '/ingresar/'
    template_name = 'pais_view.html'
    model = Pais
    
    def get_context_data(self, **kwargs) :
        context = super(Pais, self).get_context(**kwargs)
        pais = Pais.objects.all()
        context['registro'] = pais
        return context
    
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

class DepartamentoView(View):
    
    login_url = '/ingresar/'
    template_name = 'departamento_view.html'
    model = Departamento
    
    def get_context_data(self, **kwargs) :
        context = super(Departamento, self).get_context(**kwargs)
        departamento = Departamento.objects.all()
        context['registro'] = departamento
        return context
    
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

class MunicipioView(View):
    
    login_url = '/ingresar/'
    template_name = 'municipio_view.html'
    model = Municipio
    
    def get_context_data(self, **kwargs) :
        context = super(Municipio, self).get_context(**kwargs)
        municipio = Municipio.objects.all()
        context['registro'] = municipio
        return context
    
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

class DireccionView(View):
    
    login_url = '/ingresar/'
    template_name = 'direccion_view.html'
    model = Direccion
    
    def get_context_data(self, **kwargs) :
        context = super(Direccion, self).get_context(**kwargs)
        direccion = Direccion.objects.all()
        context['registro'] = direccion
        return context
    
class DireccionCreateView(UserPassesTestMixin,CreateView):
    
    login_url = '/ingresar'
    template_name = 'direccion_form.html'
    form_class = DireccionForm
    model = Direccion
    
    def get_success_url(self):
        return reverse_lazy('direccionList')
    
    def post(self, request, *args, **kwargs):
        pk=self.kwargs.get("pk")
        complementoDireccion = request.POST.get("complementoDireccion")
        municipioId = request.POST.get("municipio")
        municipio = Municipio.objects.get(id=municipioId)
        direccion= Direccion.objects.create(complementoDireccion=complementoDireccion, municipio=municipio)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a creado la direccion: "+ complementoDireccion + " "  + "con exito")
        return redirect('direccionList')

class DireccionUpdateView(UserPassesTestMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'direccion_form.html'
    form_class = DireccionForm
    
    def get_success_url(self):
        return reverse_lazy('direccionList')

    def post(self, request, *args, **kwargs):
        pk=self.kwargs.get("pk")
        complementoDireccion = request.POST.get("complementoDireccion")
        municipioId = request.POST.get("municipio")
        municipio = Municipio.objects.get(id=municipioId)
        Direccion.objects.update(complementoDireccion=complementoDireccion, municipio=municipio)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a actualizado la direccion: "+ complementoDireccion + " " + "con exito")
        return redirect('direccionList')

class UnidadMedidaView(View):
    
    login_url = '/ingresar/'
    template_name = 'unidad_medida_view.html'
    model = UnidadMedida
    
    def get_context_data(self, **kwargs) :
        context = super(UnidadMedida, self).get_context(**kwargs)
        unidadMedida = UnidadMedida.objects.all()
        context['registro'] = unidadMedida
        return context
    
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

class OperacionSujetoExluidoView(View):
    
    login_url = '/ingresar'
    template_name = 'operacion_sujeto_exluido_view.html'
    model = OperacionesSujetoExcluido
    
    def get_context_data(self, **kwargs) :
        context = super(OperacionesSujetoExcluido, self).get_context(**kwargs)
        operacionesSujetoExcluido = OperacionesSujetoExcluido.objects.all()
        context['registro'] = operacionesSujetoExcluido
        return context

class OperacionSujetoExcluidoCreateView(UserPassesTestMixin, CreateView):
    
    login_url = '/ingresar'
    template_name = 'operacion_sujeto_excluido_form.html'
    form_class = OperacionesSujetoExcluidoForm
    model = OperacionesSujetoExcluido
    
    def get_success_url(self):
        return reverse_lazy('operacionesSujetoExcluidoList')
    
    def post(self, request, *args, **kwargs):
        pk=self.kwargs.get("pk")
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a creado la operacion del sujeto excluido con exito")
        return redirect('operacionesSujetoExcluidoList')

class OperacionSujetoExcluidoUpdateView(UserPassesTestMixin, UpdateView):
    
    login_url = '/ingresar'
    template_name = 'operacion_sujeto_excluido_form.html'
    form_class = OperacionesSujetoExcluidoForm
    model = OperacionesSujetoExcluido
    
    def get_success_url(self):
        return reverse_lazy('operacionesSujetoExcluidoList')
    
    def post(self, request, *args, **kwargs):
        pk=self.kwargs.get("pk")
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a actualizado la operacion del sujeto excluido con exito")
        return redirect('operacionesSujetoExcluidoList')


class SujetoExcluidoMonthView(MonthArchiveView):
    """Muestra la lista de sujetos excluidos por mes"""

    login_url='/ingresar/'
    """queryset = SujetoExcluido.objects.all()"""
    data_field = "fechaEmi"
    template_name='sujeto_excluido_month.html'
    allow_empty = True
    allow_future = True

    def get_context_data(self, **kwargs) :
        context = super(SujetoExcluido, self).get_context(**kwargs)
        sujeto = SujetoExcluido.objects.all()
        context['registro'] = sujeto
        return context

class SujetoExcluidoView(DetailView):
    """Muestra los datos de un sujeto excluido en especifico"""

    login_url = '/ingresar/'
    template_name = 'sujeto_excluido_by_id_view.html'
    model = SujetoExcluido

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)    


class FormaPagoView(View):
    
    login_url = '/ingresar/'
    template_name = 'forma_pago_view.html'
    model = FormaPago
    
    def get_context_data(self, **kwargs) :
        context = super(FormaPago, self).get_context(**kwargs)
        formaPago = FormaPago.objects.all()
        context['registro'] = formaPago
        return context
    
class FormaPagoCreateView(UserPassesTestMixin,CreateView):
    
    login_url = '/ingresar'
    template_name = 'forma_pago_form.html'
    form_class = FormaPagoForm
    model = FormaPago
    
    def get_success_url(self):
        return reverse_lazy('formaPagoList')
    
    def post(self, request, *args, **kwargs):
        pk=self.kwargs.get("pk")
        codigo = request.POST.get("codigo")
        valor = request.POST.get("valor")
        formaPago= FormaPago.objects.create(codigo=codigo, valor=valor)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a creado la forma de pago: "+ codigo + " " + valor + "con exito")
        return redirect('formaPagoList')

class FormaPagoUpdateView(UserPassesTestMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'forma_pago_form.html'
    form_class = FormaPagoForm
    
    def get_success_url(self):
        return reverse_lazy('formaPagoList')

    def post(self, request, *args, **kwargs):
        pk=self.kwargs.get("pk")
        codigo = request.POST.get("codigo")
        valor = request.POST.get("valor")
        FormaPago.objects.update(codigo=codigo, valor=valor)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a actualizado la forma de pago: "+ codigo + " " + valor + "con exito")
        return redirect('formaPagoList')

class PagoView(View):
    
    login_url = '/ingresar/'
    template_name = 'pago_view.html'
    model = Pago
    
    def get_context_data(self, **kwargs) :
        context = super(Pago, self).get_context(**kwargs)
        pago = Pago.objects.all()
        context['registro'] = pago
        return context
    
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
        pago= Pais.objects.create(codigo=codigo, formaPago=formaPago, montoPago=montoPago, referencia=referencia, plazo=plazo, periodo=periodo)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a creado el pago: "+ codigo + " " + montoPago + "con exito")
        return redirect('pagoList')

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

class ApendiceView(DetailView):
    """Muestra los datos de las apendices registradas en el sistema"""
    
    login_url = '/ingresar/'
    template_name = 'apendice_view.html'
    model = Apendice
    
    def get_context_data(self, **kwargs) :
        context = super(Apendice, self).get_context(**kwargs)
        apendice = Apendice.objects.all()
        context['registro'] = apendice
        return context

class ApendiceCreateView(UserPassesTestMixin, CreateView):
    login_url = '/ingresar'
    template_name = 'apendice_form.html'
    form_class = ApendiceForm
    model = Apendice
    
    def get_success_url(self):
        return reverse_lazy('apendiceList')
    
    def post(self, request, *args, **kwargs):
        pk=self.kwargs.get("pk")
        campo = request.POST.get("campo")
        etiqueta = request.POST.get("etiqueta")
        valor = request.POST.get("valor")
        apendice = Apendice.objects.create(campo=campo, etiqueta=etiqueta, valor=valor)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a creado la panedice: "+ campo + " " + valor + "con exito")
        return redirect('apendiceList')

class ApendiceUpdateView(UserPassesTestMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'apendice_form.html'
    form_class = ApendiceForm
    
    def get_success_url(self):
        return reverse_lazy('apendiceList')

    def post(self, request, *args, **kwargs):
        pk=self.kwargs.get("pk")
        campo = request.POST.get("campo")
        etiqueta = request.POST.get("etiqueta")
        valor = request.POST.get("valor")
        Apendice.objects.update(campo=campo, etiqueta=etiqueta, valor=valor)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a actualizado el apendice: "+ campo + " " + valor + "con exito")
        return redirect('apendiceList')

class TipoDocumentoView(View):
    
    login_url = '/ingresar/'
    template_name = 'tipo_documento_view.html'
    model = TipoDocumento
    
    def get_context_data(self, **kwargs) :
        context = super(TipoDocumento, self).get_context(**kwargs)
        tipoDocumento= TipoDocumento.objects.all()
        context['registro'] = tipoDocumento
        return context
    
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

class IdentificadorView(View):
    
    login_url = '/ingresar/'
    template_name = 'identificador_view.html'
    model = Identificador
    
    def get_context_data(self, **kwargs) :
        context = super(Identificador, self).get_context(**kwargs)
        identificador = Identificador.objects.all()
        context['registro'] = identificador
        return context
    
class IdentificadorCreateView(UserPassesTestMixin,CreateView):
    
    login_url = '/ingresar'
    template_name = 'identificador_form.html'
    form_class = IdentificadorForm
    model = Identificador
    
    def get_success_url(self):
        return reverse_lazy('identificadorList')
    
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
        identificador= Identificador.objects.create(version=version, ambiente=ambiente, tipoDte=tipoDte, numeroControl=numeroControl,codigoGeneracion=codigoGeneracion, 
                                                    tipoModelo=tipoModelo, tipoOperacion=tipoOperacion, tipoContingencia=tipoContingencia, motivoContin=motivoContin,
                                                    fechaEmision=fechaEmi, tipoMoneda=tipoMoneda)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a creado el identificador: "+ version + " " + numeroControl + " " + codigoGeneracion + " "  + "con exito")
        return redirect('identificadorList')

class IdentificadorUpdateView(UserPassesTestMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'identificador_form.html'
    form_class = IdentificadorForm
    
    def get_success_url(self):
        return reverse_lazy('identificadorList')

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
        return redirect('identificadorList')

class EmisorView(View):
    
    login_url = '/ingresar/'
    template_name = 'emisor_view.html'
    model = Emisor
    
    def get_context_data(self, **kwargs) :
        context = super(Emisor, self).get_context(**kwargs)
        emisor = Emisor.objects.all()
        context['registro'] = emisor
        return context
    
class EmisorCreateView(UserPassesTestMixin,CreateView):
    
    login_url = '/ingresar'
    template_name = 'emisor_form.html'
    form_class = EmisorForm
    model = Emisor
    
    def get_success_url(self):
        return reverse_lazy('emisorList')
    
    def post(self, request, *args, **kwargs):
        pk=self.kwargs.get("pk")
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a creado el emisor con exito")
        return redirect('emisorList')

class EmisorUpdateView(UserPassesTestMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'emisor_form.html'
    form_class = EmisorForm
    model = Emisor
    
    def get_success_url(self):
        return reverse_lazy('emisorList')

    def post(self, request, *args, **kwargs):
        pk=self.kwargs.get("pk")
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a actualizado el emisor con exito")
        return redirect('emisorList')

class ReceptorView(View):
    
    login_url = '/ingresar/'
    template_name = 'receptor_view.html'
    model = Receptor
    
    def get_context_data(self, **kwargs) :
        context = super(Receptor, self).get_context(**kwargs)
        receptor = receptor.objects.all()
        context['registro'] = receptor
        return context
    
class ReceptorCreateView(UserPassesTestMixin,CreateView):
    
    login_url = '/ingresar'
    template_name = 'receptor_form.html'
    form_class = ReceptorForm
    model = Emisor
    
    def get_success_url(self):
        return reverse_lazy('receptorList')
    
    def post(self, request, *args, **kwargs):
        pk=self.kwargs.get("pk")
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a creado el receptor con exito")
        return redirect('recpetorList')

class ReceptorUpdateView(UserPassesTestMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'receptor_form.html'
    form_class = ReceptorForm
    model = Receptor
    
    def get_success_url(self):
        return reverse_lazy('receptorList')

    def post(self, request, *args, **kwargs):
        pk=self.kwargs.get("pk")
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a actualizado el receptor con exito")
        return redirect('receptorList')

class OtroDocumentoAsociadoView(View):
    
    login_url = '/ingresar/'
    template_name = 'otro_documento_asociado_view.html'
    model = OtroDocumentoAsociado
    
    def get_context_data(self, **kwargs) :
        context = super(OtroDocumentoAsociado, self).get_context(**kwargs)
        otroDocumentoAsociado = OtroDocumentoAsociado.objects.all()
        context['registro'] = otroDocumentoAsociado
        return context
    
class OtroDocumentoAsociadoCreateView(UserPassesTestMixin,CreateView):
    
    login_url = '/ingresar'
    template_name = 'otro_documento_asociado_form.html'
    form_class = OtroDocumentoAsociadoForm
    model = OtroDocumentoAsociado
    
    def get_success_url(self):
        return reverse_lazy('otroDocumentoAsociadoList')
    
    def post(self, request, *args, **kwargs):
        pk=self.kwargs.get("pk")
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a creado el otro documento asociado con exito")
        return redirect('otroDocumentoAsociadoList')

class OtroDocumentoAsociadoUpdateView(UserPassesTestMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'otro_documento_asociado_form.html'
    form_class = OtroDocumentoAsociadoForm
    model = OtroDocumentoAsociado
    
    def get_success_url(self):
        return reverse_lazy('otroDocumentoAsociadoList')

    def post(self, request, *args, **kwargs):
        pk=self.kwargs.get("pk")
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a actualizado otro documento asociado con exito")
        return redirect('otroDocumentoAsociadoList')

class CuerpoDocumentoView(View):
    
    login_url = '/ingresar/'
    template_name = 'cuerpo_documento_view.html'
    model = CuerpoDocumento
    
    def get_context_data(self, **kwargs) :
        context = super(CuerpoDocumento, self).get_context(**kwargs)
        cuerpoDocumento = CuerpoDocumento.objects.all()
        context['registro'] = cuerpoDocumento
        return context
    
class CuerpoDocumentoCreateView(UserPassesTestMixin,CreateView):
    
    login_url = '/ingresar'
    template_name = 'cuerpo_documento_form.html'
    form_class = CuerpoDocumentoForm
    model = CuerpoDocumento
    
    def get_success_url(self):
        return reverse_lazy('cuerpoDocumentoList')
    
    def post(self, request, *args, **kwargs):
        pk=self.kwargs.get("pk")
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a creado el cuerpo del documento con exito")
        return redirect('cuerpoDocumentoList')

class CuerpoDocumentoUpdateView(UserPassesTestMixin, UpdateView):
    login_url = '/ingresar'
    template_name = 'cuerpo_documento_form.html'
    form_class = CuerpoDocumentoForm
    model = CuerpoDocumento
    
    def get_success_url(self):
        return reverse_lazy('cuerpoDocumentoList')

    def post(self, request, *args, **kwargs):
        pk=self.kwargs.get("pk")
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se a actualizado el cuerpo del documento con exito")
        return redirect('cuerpoDocumentoList')

class PagoDonacionView(View):
    
    login_url = '/ingresar/'
    template_name = 'pago_donacion_view.html'
    model = OtroDocumentoAsociado
    
    def get_context_data(self, **kwargs) :
        context = super(PagoDonacion, self).get_context(**kwargs)
        pagoDonacion = PagoDonacion.objects.all()
        context['registro'] = PagoDonacion
        return context
    
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