from django.db import models
from django.contrib import admin
from django.conf import settings

class FB(models.Model):
	email = models.CharField(verbose_name="Электронный адрес", max_length=50)
	text = models.TextField(verbose_name="Текст отзыва")
	class Meta:
		verbose_name = "Отзыв"
		verbose_name_plural = "Отзывы"

def __str__(self):
				return self.email