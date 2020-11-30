from django.shortcuts import render
from django.http import HttpResponse

from gruporouters.models import GrupoRouter
from devices.models import Device

from gruporouters.forms import GrupoRouterForm
from devices.forms import DeviceForm

from django.http import HttpRequest

from django.shortcuts import redirect




# Create your views here.

def home_view(request ,*args, **kwargs): #a view da home será a view de list/pesquisa dos grupos de routers/devices

	#Excluir Grupo
	if request.method == "POST":
		if request.POST.get('opfId1') == "delete":
			GrupoRouter.objects.get( id= request.POST.get('idgrupo')).delete()

			#print ("test", HttpRequest.body, request.POST.get('idgrupo'), objdel)

	#listar grupos
	grupo_list = list(GrupoRouter.objects.all())

	home_context = {
	"grupo_list": grupo_list,
	}
	return render (request, "home.html", home_context)






def cadastrargrupo_view(request ,*args, **kwargs):

	form = GrupoRouterForm(request.POST or None)
	if form.is_valid():
		form.save()
		#form = GrupoRouterForm()
		return redirect('/home')

	cadastrargrupo_context = {
		'form_grupo': form,
	}
	return render (request, "cadastrargrupo.html", cadastrargrupo_context)



    

def editargrupo_view(request ,*args, **kwargs):

	grupo = GrupoRouter.objects.get(id= request.GET.get('idgrupo'))
	form = GrupoRouterForm(request.POST or None, instance=grupo)

	if form.is_valid():
		form.save()
		return redirect('/home')

	editargrupo_context = {
		'form_editgrupo': form,
	}
	return render (request, "editargrupo.html", editargrupo_context)






def listardevices_view(request ,*args, **kwargs):

	#Excluir Device
	if request.method == "POST":
		
		if request.POST.get('opfId1') == "delete":
			Device.objects.get( id= request.POST.get('iddevice')).delete()

	#listar device                                #filtro query pelo
	device_list = list(Device.objects.filter(gruporouter_id= request.GET.get('idgrupo')))

	listardevice_context = {
	"device_list": device_list,
	}

	return render (request, "listardevices.html", listardevice_context)






def cadastrardevice_view(request ,*args, **kwargs):
											#initial = inicia o grupo no clicado anteriormente
	form = DeviceForm(request.POST or None, initial={'gruporouter': request.GET.get('idgrupo')})

	if form.is_valid():
		form.save()
		#form = GrupoRouterForm()
		return redirect('/home')

	cadastrardevice_context = {
		'form_device': form,
	}
	return render (request, "cadastrardevice.html", cadastrardevice_context)





def editardevice_view(request ,*args, **kwargs):



	device = Device.objects.get(id= request.GET.get('iddevice'))
	form = DeviceForm(request.POST or None, instance=device)

	if form.is_valid():
		form.save()
		return redirect('/home')

	editardevice_context = {
		'form_editdevice': form,
	}






	return render (request, "editardevice.html", editardevice_context)






def inventario_view(request ,*args, **kwargs):
	return render (request, "inventario.html", {})

def auditoria_view(request ,*args, **kwargs):
	return render (request, "auditoria.html", {})

def relatorios_view(request ,*args, **kwargs):
	return render (request, "relatorios.html", {})

def admin1_view(request ,*args, **kwargs):
	return render (request, "admin1.html", {})

def perfil_view(request ,*args, **kwargs):
	return render (request, "perfil.html", {})