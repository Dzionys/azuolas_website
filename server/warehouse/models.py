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

	class Meta:
		verbose_name = 'Daiktas'
		verbose_name_plural = 'Daiktai'

	def __str__(self):
		if self.name:
			return f'{self.category} „{self.name}“'
		else:
			return self.category

	def get_condition(self):
		return self.CONDITIONS[self.condition - 1][1]


class Rental(models.Model):
	STATES = (
		(1, 'Laisva'),
		(2, 'Rezervuota'),
		(3, 'Paimta')
	)

	reservation_date = models.DateTimeField(verbose_name='Rezervacijos data', null=True)
	pick_up_date = models.DateTimeField(verbose_name='Paėmimo data', null=True)
	return_date = models.DateTimeField(verbose_name='Gražinimo data', null=True)
	user = models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True)
	state = models.IntegerField(choices=STATES, default=1, verbose_name='Statusas')
	item = models.OneToOneField(Item, on_delete=models.CASCADE, related_name='obj', null=False)

	def __str__(self):
		return self.STATES[self.state - 1][1]

class Log(models.Model):
	STATES = (
		(1, 'Laisva'),
		(2, 'Rezervuota'),
		(3, 'Paimta')
	)

	state = models.IntegerField(choices=STATES, default=1, verbose_name='Statusas')
	prev_state = models.IntegerField(choices=STATES, default=1, verbose_name='Buves statusas')
	action = models.CharField(max_length=150, verbose_name='Veiksmas')
	rent = models.ForeignKey(Rental, on_delete=models.CASCADE, null=False)
	date = models.DateTimeField(verbose_name='Data', null=False)
	user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

	def __str__(self):
		return self.action

	def get_state(self):
		return self.STATES[self.state - 1][1]

	class Meta:
		verbose_name = 'Veiksmas'
		verbose_name_plural = 'Žurnalas'