from django.db import models
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
	author = models.CharField(max_length=200)
	title = models.CharField(max_length=200)
	text = models.TextField(blank=True)
	cover = models.ImageField(blank=True)
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)



	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post_detail', args=[str(self.id)])