from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import validate_ipv46_address

# Create your models here.
class Device(models.Model):

	class DeviceTypes (models.TextChoices):
	#	__empty__ = _('Selecione')
		JUNIPER = 'JU', _("Juniper")
		CISCO 	= 'CI', _("Cisco")
		EXTREME = 'EX', _("Extreme")
		HUAWEI 	= 'HU', _("Huawei")

	class SiteTypes (models.TextChoices):
		__empty__ = _('Estados do Brasil')
		Acre			 = "AC", _("Acre")
		Alagoas			 = "AL", _("Alagoas")
		Amapa			 = "AP", _("Amapá")
		Amazonas		 = "AM", _("Amazonas")
		Bahia			 = "BA", _("Bahia")
		Ceara			 = "CE", _("Ceará")
		DistritoFederal	 = "DF", _("Distrito Federal")
		EspiritoSanto	 = "ES", _("Espírito Santo")
		Goias			 = "GO", _("Goiás")
		Maranhao		 = "MA", _("Maranhão")
		MatoGrosso 		 = "MT", _("Mato Grosso")
		MatoGrossodoSul	 = "MS", _("Mato Grosso do Sul")
		MinasGerais		 = "MG", _("Minas Gerais")
		Para 			 = "PA", _("Pará")
		Paraiba			 = "PB", _("Paraíba")
		Parana			 = "PR", _("Paraná")
		Pernambuco		 = "PE", _("Pernambuco")
		Piaui			 = "PI", _("Piauí")
		Roraima			 = "RR", _("Roraima")
		Rondonia		 = "RO", _("Rondônia")
		RiodeJaneiro	 = "RJ", _("Rio de Janeiro")
		RioGrandedoNorte = "RN", _("Rio Grande do Norte")
		RioGrandedoSul	 = "RS", _("Rio Grande do Sul")
		SantaCatarina	 = "SC", _("Santa Catarina")
		SaoPaulo 		 = "SP", _("São Paulo")
		Sergipe 		 = "SE", _("Sergipe")
		Tocantins 		 = "TO", _("Tocantins")

	nome 			= models.CharField(max_length=12, verbose_name="Nome",)
	descricao 		= models.TextField(verbose_name="Descrição",)
	site 			= models.CharField(max_length=2, choices=SiteTypes.choices, verbose_name="Site",)
	device_type 	= models.CharField(max_length=2, choices=DeviceTypes.choices, verbose_name="Device Type",)
	ipaddress 		= models.GenericIPAddressField(protocol='both', unpack_ipv4=False, validators=[validate_ipv46_address], verbose_name="IP address",)
	sshport 		= models.CharField(max_length=4, verbose_name="SSH port",)
	gruporouter		= models.ForeignKey('gruporouters.GrupoRouter',on_delete=models.CASCADE,)
