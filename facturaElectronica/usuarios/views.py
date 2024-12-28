from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, View, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model
from django.views.generic import ListView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse

def is_system_superuser(user):
    return user.is_system_superuser

def user_has_permission(user, permission):
    return user.is_system_superuser or user.is_entidad_superuser or user.has_permission(permission)

class BienvenidaView(TemplateView):
    template_name = 'bienvenida.html'

class IndexView(LoginRequiredMixin,TemplateView):
    template_name = 'index.html'
# Create your views here.
class ActividadEconomicaDetailView(LoginRequiredMixin,DetailView):
    
    login_url = '/ingresar/'
    template_name = 'actividad_economica_view.html'
    model: ActividadEconomica
    
    def get_context_data(self, **kwargs) :
        id=self.kwargs['pk']
        context = super(ActividadEconomicaDetailView, self).get_context(**kwargs)
        actividadEconomica = ActividadEconomica.objects.filter(id=id)
        context['actividadEconomica'] = actividadEconomica
        return context

class ActividadEconomicaCreateView(LoginRequiredMixin, CreateView):
    login_url = '/ingresa/'
    template_name = 'actividad_economica_form.html'
    model = ActividadEconomica
    form_class = ActividadEconomicaForm
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_administrativo')
    
    def form_valid(self, form):
        actividadEconomica = form.save(commit=False)        
        actividadEconomica.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))
class ActividadEconomicaUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/ingresa/'
    template_name = 'actividad_economica_form.html'
    model = ActividadEconomica
    form_class = ActividadEconomicaForm
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_administrativo')
    
    def form_valid(self, form):
        actividadEconomica = form.save(commit=False)        
        actividadEconomica.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))
    
class EntidadDetailView(LoginRequiredMixin,DetailView):
    
    login_url = '/ingresar/'
    template_name = 'info_entidad.html'
    model: Entidad
    context_object_name = 'entidad'
    
    def get_object(self):       
        entidad = self.request.user.entidad
        
        
        if entidad is None:
            return "El ususario no esta asociado a ninguna Entidad"
        else:
            entidad = get_object_or_404(Entidad, pk=entidad.pk)
            return entidad

class EntidadCreateView(LoginRequiredMixin, CreateView):
    model = Entidad
    form_class = EntidadForm
    template_name = 'entidad_form.html'
    success_url = reverse_lazy('verEntidad')
    
    def get_initial(self):
        initial = super().get_initial()
        initial['direccionEmisor'] = self.request.GET.get('direccionEmisor')
        initial['actividadEconomica'] = self.request.GET.get('actividadEconomica')
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['direccionEmisor_id'] = self.request.GET.get('direccionEmisor')
        context['actividadEconomica_id'] = self.request.GET.get('actividadEconomica')
        return context
    
    def form_valid(self, form):
        
        entidad = form.save(commit=False)        
        entidad.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))
    

class EntidadUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/ingresa/'
    template_name = 'entidad_form.html'
    model = Entidad
    form_class = EntidadForm
    
    def get_success_url(self):
        id=self.kwargs['pk']
        return reverse_lazy('verEntidad')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        entidad = self.get_object()
        context['direccionEmisor_id'] = entidad.direccionEmisor.id if entidad.direccionEmisor else None
        context['actividadEconomica_id'] = entidad.actividadEconomica.id if entidad.actividadEconomica else None
        return context
    
    def form_valid(self, form):
        
        entidad = form.save(commit=False)        
        entidad.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))

class ParametrosHaciendaDetailView(LoginRequiredMixin,DetailView):
    
    login_url = '/ingresar/'
    template_name = 'auth_hacienda_view.html'
    model: ParametrosAuthHacienda
    context_object_name = "parametro"
    
    def get_object(self) :
        entidad = self.request.user.entidad
        if entidad is None:
            return  None    
        else:
            try:
                return ParametrosAuthHacienda.objects.get(entidad=entidad)  
            except ParametrosAuthHacienda.DoesNotExist:
                return None                

class ParametrosAuthHaciendaCreateView(LoginRequiredMixin, CreateView):
    template_name = 'auth_hacienda_form.html'
    model = ParametrosAuthHacienda
    form_class = ParametrosAuthHaciendaForm
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_administrativo')
    
    def form_valid(self, form):
        
        form.instance.entidad = self.request.user.entidad
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))

class ParametrosAuthHaciendaUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'auth_hacienda_form.html'
    model = ParametrosAuthHacienda
    form_class = ParametrosAuthHaciendaForm
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('panel_administrativo')
    
    def form_valid(self, form):
        parametros =  form.save(commit=False)
        parametros.entidad = self.request.user.entidad
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))

class CustomLoginView(LoginView):
    template_name = 'login.html'
    form_class = CustomAuthenticationForm
    success_url = reverse_lazy('panel_facturas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Aquí puedes agregar datos adicionales al contexto si es necesario
        return context
    
class UserListView (LoginRequiredMixin,ListView):
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

class SystemAdminRegistrationView(CreateView):
    model = CustomUser
    form_class = SystemAdminRegistrationForm
    template_name = 'register_system_admin.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_system_superuser = True
        user.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return HttpResponse("Formulario no válido: {}".format(form.errors))

class EntityAdminRegistrationView(CreateView):
    model = CustomUser
    form_class = CustomUserForm
    template_name = 'register_entity_admin.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_entidad_superuser = True
        user.entidad = form.cleaned_data['entidad']
        user.save()
        return super().form_valid(form)

@method_decorator(user_passes_test(lambda u: u.is_superuser or u.has_permission('add_user')), name='dispatch')
class UserCreateView(CreateView):
    model = CustomUser
    form_class = CustomUserForm
    template_name = 'create_user.html'
    success_url = reverse_lazy('index_user')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['usuario'] = self.request.user
        return kwargs
    
    def form_valid(self, form):
        user = form.save(commit=False)
        if self.request.user.is_system_superuser:
            user.is_system_superuser = form.cleaned_data['is_system_superuser']
        user.save()
        form.save_m2m()
        return redirect(self.success_url)

@method_decorator(user_passes_test(lambda u: u.is_superuser or u.has_permission('edit_user')), name='dispatch')
class UserUpdateView(UpdateView):
    model = CustomUser
    fields = ['name', 'lastname', 'email', 'actividadEconomica','is_system_superuser','is_entidad_superuser', 'entidad','password']
    template_name = 'edit_user.html'
    success_url = reverse_lazy('index_user')

    def get_queryset(self):
        if self.request.user.is_system_superuser:
            return CustomUser.objects.all()
        return CustomUser.objects.filter(entidad=self.request.user.entidad)

@method_decorator(user_passes_test(lambda u: u.is_superuser or u.has_permission('delete_user')), name='dispatch')
class UserDeleteView(DeleteView):
    model = CustomUser
    template_name = 'delete_user.html'
    success_url = reverse_lazy('index_user')

    def get_queryset(self):
        if self.request.user.is_system_superuser:
            return CustomUser.objects.all()
        return CustomUser.objects.filter(entidad=self.request.user.entidad)

@method_decorator(user_passes_test(is_system_superuser), name='dispatch')
class UserListView(ListView):
    model = CustomUser
    template_name = 'user_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        if self.request.user.is_system_superuser:
            return CustomUser.objects.all()
        return CustomUser.objects.filter(entidad=self.request.user.entidad)

class UserDetailView(LoginRequiredMixin, DetailView):
    login_url = '/ingresar/'
    template_name = 'ver_user.html'
    model = CustomUser
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = get_object_or_404(CustomUser, pk=context['object'].id)
        context['user'] = user
        context['show'] = True
        return context