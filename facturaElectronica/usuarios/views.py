from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, View, TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model
from django.views.generic import ListView
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
@login_required(redirect_field_name='/ingresar')
class ActividadEconomicaDetailView(DetailView):
    
    login_url = '/ingresar/'
    template_name = 'actividad_economica_view.html'
    model: ActividadEconomica
    
    def get_context_data(self, **kwargs) :
        id=self.kwargs['pk']
        context = super(ActividadEconomicaDetailView, self).get_context(**kwargs)
        actividadEconomica = ActividadEconomica.objects.filter(id=id)
        context['actividadEconomica'] = actividadEconomica
        return context

@login_required(redirect_field_name='/ingresar')
class ActividadEconomicaCreateView(UserPassesTestMixin, CreateView):
    login_url = '/ingresa/'
    template_name = 'actividad_economica_form.html'
    model = ActividadEconomica
    form_class = ActividadEconomicaForm
    
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

@login_required(redirect_field_name='/ingresar')    
class ActividadEconomicaUpdateView(UserPassesTestMixin, UpdateView):
    login_url = '/ingresa/'
    template_name = 'auth_hacienda_form.html'
    model = ActividadEconomica
    form_class = ActividadEconomicaForm
    
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
 
@login_required(redirect_field_name='/ingresar')   
class EntidadDetailView(DetailView):
    
    login_url = '/ingresar/'
    template_name = 'entidad_view.html'
    model: Entidad
    
    def get_context_data(self, **kwargs) :
        id=self.kwargs['pk']
        context = super(Entidad, self).get_context(**kwargs)
        Entidad = Entidad.objects.filter(id=id)
        context['entidad'] = Entidad
        return context

@login_required(redirect_field_name='/ingresar')
class EntidadCreateView(UserPassesTestMixin, CreateView):
    login_url = '/ingresa/'
    template_name = 'entidad_form.html'
    model = Entidad
    form_class = EntidadForm
    
    def get_success_url(self):
        id=self.kwargs['pk']
        return reverse_lazy('paisList')
    
    def post(self, request, *args, **kwargs):
        pk=self.kwargs.get("pk")
        razonSocial = request.POST.get("razonSocial")
        direccionEmisor = request.POST.get("direccionEmisor")
        cellphone = request.POST.get("cellphone")
        codEstableMH = request.POST.get("codEstableMH")
        codEstable = request.POST.get("codEstable")
        codPuntoVentaMH = request.POST.get("codPuntoVentaMH")
        codPuntoVenta = request.POST.get("codPuntoVenta")
        email = request.POST.get("email")
        nit = request.POST.get("nit")
        nrc = request.POST.get("nrc")
        idActividadEconomica = request.POST.get("actividadEconomica")
        actividadEconomica = get_object_or_404(ActividadEconomica, pk=idActividadEconomica)
        entidad= Entidad.objects.create(razonSocial=razonSocial, direccionEmisor=direccionEmisor, cellphone=cellphone, 
                                        codEstableMH=codEstableMH, codEstable=codEstable, codPuntoVentaMH=codPuntoVentaMH, 
                                        codPuntoVenta=codPuntoVenta, email=email, nit=nit, nrc=nrc, actividadEconomica=actividadEconomica)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se ha agregado una nueva Entidad "+ 
                             razonSocial + " " + nit + "con exito")
        return redirect('paisList')

@login_required(redirect_field_name='/ingresar')
class EntidadUpdateView(UserPassesTestMixin, UpdateView):
    login_url = '/ingresa/'
    template_name = 'entidad_form.html'
    model = Entidad
    form_class = EntidadForm
    
    def get_success_url(self):
        id=self.kwargs['pk']
        return reverse_lazy('paisList')
    
    def post(self, request, *args, **kwargs):
        pk=self.kwargs.get("pk")
        razonSocial = request.POST.get("razonSocial")
        direccionEmisor = request.POST.get("direccionEmisor")
        cellphone = request.POST.get("cellphone")
        codEstableMH = request.POST.get("codEstableMH")
        codEstable = request.POST.get("codEstable")
        codPuntoVentaMH = request.POST.get("codPuntoVentaMH")
        codPuntoVenta = request.POST.get("codPuntoVenta")
        email = request.POST.get("email")
        nit = request.POST.get("nit")
        nrc = request.POST.get("nrc")
        idActividadEconomica = request.POST.get("actividadEconomica")
        actividadEconomica = get_object_or_404(ActividadEconomica, pk=idActividadEconomica)
        entidad= Entidad.objects.update(razonSocial=razonSocial, direccionEmisor=direccionEmisor, cellphone=cellphone, 
                                        codEstableMH=codEstableMH, codEstable=codEstable, codPuntoVentaMH=codPuntoVentaMH, 
                                        codPuntoVenta=codPuntoVenta, email=email, nit=nit, nrc=nrc, actividadEconomica=actividadEconomica)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se han actualizado los parametros de la Entidad "+ 
                             razonSocial + " " + nit + "con exito")
        return redirect('paisList')

@login_required(redirect_field_name='/ingresar')
class ParametrosHaciendaDetailView(DetailView):
    
    login_url = '/ingresar/'
    template_name = 'parametros_auth_hacienda_view.html'
    model: ParametrosAuthHacienda
    
    def get_context_data(self, **kwargs) :
        id=self.kwargs['pk']
        context = super(ParametrosAuthHacienda, self).get_context(**kwargs)
        parametroAuthHacienda = ParametrosAuthHacienda.objects.filter(id=id)
        context['parametro'] = parametroAuthHacienda
        return context

@login_required(redirect_field_name='/ingresar')
class ParametrosAuthHaciendaCreateView(UserPassesTestMixin, CreateView):
    login_url = '/ingresa/'
    template_name = 'auth_hacienda_form.html'
    model = ParametrosAuthHacienda
    form_class = ParametrosAuthHaciendaForm
    
    def get_success_url(self):
        id=self.kwargs['pk']
        return reverse_lazy('paisList')
    
    def post(self, request, *args, **kwargs):
        pk=self.kwargs.get("pk")
        user = request.user
        userAgent = request.POST.get("userAgent")
        nit = request.POST.get("nit")
        pwd = request.POST.get("pwd")
        privateKey = request.POST.get("privateKey")
        entidad = user.Usuarios.all()
        parametrosAuthHacienda= ParametrosAuthHacienda.objects.create(userAgent=userAgent, nit=nit, pwd=pwd, privateKey=privateKey, entidad=entidad)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se han agregado los parametros de auth de"+ 
                             "hacienda para esta entidad: "+ userAgent + " " + nit + "con exito")
        return redirect('paisList')

@login_required(redirect_field_name='/ingresar')
class ParametrosAuthHaciendaUpdateView(UserPassesTestMixin, UpdateView):
    login_url = '/ingresa/'
    template_name = 'auth_hacienda_form.html'
    model = ParametrosAuthHacienda
    form_class = ParametrosAuthHaciendaForm
    
    def get_success_url(self):
        id=self.kwargs['pk']
        return reverse_lazy('paisList')
    
    def post(self, request, *args, **kwargs):
        pk=self.kwargs.get("pk")
        userAgent = request.POST.get("userAgent")
        nit = request.POST.get("nit")
        pwd = request.POST.get("pwd")
        privateKey = request.POST.get("privateKey")
        parametrosAuthHacienda= ParametrosAuthHacienda.objects.update(userAgent=userAgent, nit=nit, pwd=pwd, privateKey=privateKey)
        messages.add_message(request=request, level=messages.SUCCESS, message= "Se han actualizado los parametros de auth de"+ 
                             "hacienda para esta entidad: "+ userAgent + " " + nit + "con exito")
        return redirect('paisList')

class CustomLoginView(LoginView):
    template_name = 'login.html'
    form_class = UserForm
    success_url = reverse_lazy('panel_facturas')

    def get_success_url(self):
        return self.success_url
    
class UserListView (ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'users'
    
    def get_queryset(self):
        entidad_id = self.kwargs.get('entidad_id')
        return User.objects.filter(entidad__id=entidad_id)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        entidad_id = self.kwargs.get('entidad_id')
        context['entidad'] = Entidad.objects.get(id=entidad_id)
        return context

@staff_member_required
def redirect_to_add_user(request):
    return redirect('/admin/auth/user/add/')