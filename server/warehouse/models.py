from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class ItemType(models.Model):
	name = models.CharField(max_length=100, verbose_name='Pavadinimas')
	slug = models.SlugField()

	class Meta:
		verbose_name = 'Daikto Tipas'
		verbose_name_plural = 'Daiktų Tipai'

	def __str__(self):
		return self.name

class ItemCondition(models.Model):
	name = models.CharField(max_length=100, verbose_name='Pavadinimas')
	slug = models.SlugField()

	class Meta:
		verbose_name = 'Daikto Buklė'
		verbose_name_plural = 'Daiktų Buklė'

	def __str__(self):
		return self.name

class Item(models.Model):
	name = models.CharField(max_length=100, verbose_name='Pavadinimas', blank=True)
	category = models.ForeignKey(ItemType, on_delete=models.PROTECT, verbose_name='Tipas')
	color = models.CharField(max_length=100, verbose_name='Spalva')
	condition = models.ForeignKey(ItemCondition, on_delete=models.PROTECT, verbose_name='Būklė')
	description = models.TextField(verbose_name='Aprašymas')
	slug = models.SlugField(verbose_name='Nuorodos pavadinimas')

	class Meta:
		verbose_name = 'Daiktas'
		verbose_name_plural = 'Daiktai'

	def __str__(self):
		if self.name:
			return f'{self.category} „{self.name}“'
		else:
			return self.category

class ItemState(models.Model):
	user = models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True)
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	date = models.DateField(verbose_name='Data')
	state = models.BooleanField()

	class Meta:
		unique_together = ('user', 'item')