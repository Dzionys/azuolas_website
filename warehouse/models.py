from django.db import models

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