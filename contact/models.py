from django.db import models
from django.urls import reverse

class Contact(models.Model):
	name = models.CharField(max_length=32)
	email = models.EmailField()
	message = models.TextField()

	def __str__(self):
		return self.email

	def get_absolute_url(self):
		return reverse('success')