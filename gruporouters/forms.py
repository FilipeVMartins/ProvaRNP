from django import forms
from .models import GrupoRouter


class GrupoRouterForm (forms.ModelForm):
	class Meta:
		model = GrupoRouter
		fields = [
			'nome',
			'descricao',
		]