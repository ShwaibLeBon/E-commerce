from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Profile(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	phone_number = models.CharField(max_length=24, default= "+257 000 000")
	# avatar = models.ImageField(null=True,blank=True, upload_to="profil/avatars/")
	is_valid = models.BooleanField(default=False)
	email = models.EmailField()
	def __str__(self):
		return f"{self.user.username}-{self.user.email}-{self.is_valid}"

class Product(models.Model):
	owner = models.ForeignKey(User , related_name='proprietaire',on_delete=models.CASCADE)
	name = models.CharField(max_length=500)
	mark = models.ForeignKey('Mark',on_delete=models.CASCADE)
	price = models.IntegerField()
	date = models.DateField(default=timezone.now, blank=True)
	image1 = models.ImageField(default='', upload_to='products/')
	image2 = models.ImageField(default='', upload_to='products/')
	image3 = models.ImageField(default='', upload_to='products/')
	image4 = models.ImageField(default='', upload_to='products/')
	description=models.CharField(max_length=100)

	def __str__(self):
		return f"name : {self.name} Marque : {self.mark.name}"

class Mark(models.Model):
	name = models.CharField(max_length=39)
	logo = models.ImageField(upload_to ="marks/logo/")

	def __str__(self):
	 	return f"{self.name}"

#class Contact(models.Model):
	#telephone = models.CharField(max_length=30)
	#email = models.EmailField()

	#def __str__(self):
		#return f"telephone : {self.telephone} email : {self.email}"

class Cart(models.Model):
	user = models.ForeignKey(User, related_name="acheteur", on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField()
	amount = models.FloatField()
	global_amount = models.FloatField(null=True, blank=True)
	paid = models.BooleanField(default=False)
	def __str__(self):
		return f"{self.user.username} a achete {self.product.name} {self.quantity} pour {self.amount}"
		


