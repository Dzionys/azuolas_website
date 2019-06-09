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

class Item(models.Model):
	STATES = (
		(1, 'Laisva'),
		(2, 'Rezervuota'),
		(3, 'Paimta')
	)

	CONDITIONS = (
		(1, 'Puiki'),
		(2, 'Labai gera'),
		(3, 'Gera'),
		(4, 'Prasta'),
		(5, 'Labai prasta'),
		(6, 'Netinkama naudoti'),
		(7, 'Nėra')
	)

	name = models.CharField(max_length=100, verbose_name='Pavadinimas', blank=True)
	category = models.ForeignKey(ItemType, on_delete=models.PROTECT, verbose_name='Tipas')
	color = models.CharField(max_length=100, verbose_name='Spalva')
	condition = models.IntegerField(choices=CONDITIONS, verbose_name='Būklė', default=7)
	description = models.TextField(verbose_name='Aprašymas')
	slug = models.SlugField(verbose_name='Nuorodos pavadinimas')
	user = models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True)
	state = models.IntegerField(choices=STATES, default=1, verbose_name='Statusas')
	date = models.DateTimeField(verbose_name='Data')

	class Meta:
		verbose_name = 'Daiktas'
		verbose_name_plural = 'Daiktai'

	def __str__(self):
		if self.name:
			return f'{self.category} „{self.name}“'
		else:
			return self.category

	def get_state(self):
		return self.STATES[self.state - 1][1]

	def get_condition(self):
		return self.CONDITIONS[self.condition - 1][1]

class Log(models.Model):

	action = models.CharField(max_length=150, verbose_name='Veiksmas')
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	date = models.DateTimeField(verbose_name='Data')
	user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.action

	class Meta:
		verbose_name = 'Veiksmas'
		verbose_name_plural = 'Žurnalas'