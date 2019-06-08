from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Item(models.Model):

	name = models.CharField(max_length=100, verbose_name="Pavadinimas")
	category = models.CharField(max_length=100, verbose_name="Tipas")
	color = models.CharField(max_length=100, verbose_name="Spalva")
	condition = models.CharField(max_length=100, verbose_name="Būklė")
	description = models.TextField(verbose_name="Aprašymas")

	class Meta:
		verbose_name = "Daiktas"
		verbose_name_plural = "Daiktai"

class ItemState(models.Model):
	
	UserModel = get_user_model()
	user = models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True)
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	date = models.DateField(verbose_name="Data")
	state = models.BooleanField()

	class Meta:
		unique_together = ('user', 'item')