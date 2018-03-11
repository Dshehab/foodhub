from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Restaurant(models.Model):
	name = models.CharField(max_length = 25)
	description = models.TextField()
	image = models.ImageField(null=True)
	opening_time = models.TimeField(null=True)
	closing_time = models.TimeField(null=True)
	publish_date = models.DateField()
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	def __str__(self):
		return self.name

class FavoriteRestaurant(models.Model):
	"""docstring for FavoriteRestaurat"""
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)


	
