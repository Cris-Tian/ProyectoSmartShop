from django.shortcuts import render
from .models import Marca, Telefono, TelefonoInstance

# Create your views here.
def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    num_telefonos=Telefono.objects.all().count()
    num_instances=TelefonoInstance.objects.all().count()
    # TELEFONOS disponibles (status = 'd')
    num_instances_available=TelefonoInstance.objects.filter(status__exact='d').count()
    
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={'num_telefonos':num_telefonos,'num_instances':num_instances,'num_instances_available':num_instances_available},
    )

def store(request):
    return render(request, 'productos/store.html')
	
def checkout(request):
	return render(request, 'productos/checkout.html')

def ofertas(request):
	return render(request, 'productos/ofertas.html') 

def smartphones(request):
	return render(request, 'productos/smartphones.html') 

def accesorios(request):
	return render(request, 'productos/accesorios.html') 

def caracteristicas(request):
	return render(request, 'productos/caracteristicas.html') 

def check(request):
	return render(request,'productos/crud.html')
	

	
def telefonos_list(request):
    tel = Telefono.objects.all()
    return render(request,'telefono_list.hmtl',{'tel',tel})    


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Telefono
	
class TelefonoCreate(CreateView):
	model = Telefono
	fields = '__all__'
	
class TelefonoUpdate(UpdateView):
	model = Telefono
	fields = ['nombre','marca','ram','procesador','bateria','precio','descripcion']
	
class TelefonoDelete(DeleteView):
	model = Telefono 
	success_url = reverse_lazy('telefonos')	
	
from django.views import generic
class TelefonoDetailView(generic.DetailView):
	model = Telefono
		
from django.views import generic
class TelefonoListView(generic.ListView):
    model = Telefono
	
    #def get_queryset(self):
       # return Telefono.objects.filter(nombre__icontains='s3')[:5] # Get 5 books containing the word s2
   #def get_context_data(self, **kwargs):
    # Call the base implementation first to get a context
       # context = super(TelefonoListView, self).get_context_data(**kwargs)
    # Get the blog from id and add it to the context
      #  context['some_data'] = 'This is just some data'
      #  return context
	
	
