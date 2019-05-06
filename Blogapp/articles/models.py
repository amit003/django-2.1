from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField()
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	thumb = models.ImageField(default='default.png', blank=True)
	author = models.ForeignKey(User, models.SET_NULL,blank=True,null=True)

	def __str__(self):
		return self.title

	@property
	def snippet(self):
		return self.body[:50] + '...'
