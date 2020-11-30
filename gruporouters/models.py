from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class GrupoRouter(models.Model):

	nome 			= models.CharField(max_length=50, verbose_name="Nome", unique=True)
	descricao 		= models.TextField(verbose_name="Descrição",)
