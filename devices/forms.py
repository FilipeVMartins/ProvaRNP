from django import forms
#from django.forms import ModelForm
from .models import Device

class DeviceForm (forms.ModelForm):
	class Meta:
		model = Device
		fields = (
			'nome',
			'descricao',
			'site',
			'device_type',
			'ipaddress',
			'sshport',
			'gruporouter',
		)