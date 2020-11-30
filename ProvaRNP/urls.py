"""ProvaRNP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pages.views import home_view
from pages.views import inventario_view
from pages.views import auditoria_view
from pages.views import relatorios_view
from pages.views import admin1_view
from pages.views import perfil_view
from pages.views import cadastrargrupo_view
from pages.views import editargrupo_view

from pages.views import cadastrardevice_view
from pages.views import listardevices_view
from pages.views import editardevice_view



urlpatterns = [
	path('', home_view, name='home'),
	path('home/', home_view, name='home'),

    path('cadastrargrupo/', cadastrargrupo_view, name='home'),
    path('editargrupo/', editargrupo_view, name='home'),

    path('cadastrardevice/', cadastrardevice_view, name='home'),
    path('listardevices/', listardevices_view, name='home'),
    path('editardevice/', editardevice_view, name='home'),

	path('inventario/', inventario_view, name='inventario'),
	path('auditoria/', auditoria_view, name='auditoria'),
	path('relatorios/', relatorios_view, name='relatorios'),
	path('admin1/', admin1_view, name='admin1'),
	path('perfil/', perfil_view, name='perfil'),

    path('admin/', admin.site.urls),
]
