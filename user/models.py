from django.db import models

from django.contrib.auth.models import User


class Profile(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	phone_number = models.CharField(max_length=24, default= "+257 000 000")
	# avatar = models.ImageField(null=True,blank=True, upload_to="profil/avatars/")
	is_valid = models.BooleanField(default=False)
	email = models.EmailField()
	def __str__(self):
		return f"{self.user.username}-{self.user.email}-{self.is_valid}"
		