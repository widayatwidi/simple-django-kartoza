from django.db import models
from django.contrib.auth.models import User
# from geoposition.fields import GeopositionField

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='profile.png', upload_to='profile_pics')
	phone = models.CharField(max_length=30, blank=True)
	location = models.CharField(max_length=30, blank=True)
	homeAddress = models.TextField(max_length=500, blank=True)
	# position = GeopositionField(blank=True)

	def __str__(self):
		return f'{self.user.username} Profile'