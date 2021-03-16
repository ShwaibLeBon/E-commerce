from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

<<<<<<< HEAD

class Profile(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	phone_number = models.CharField(max_length=24, default= "+257 000 000")
	# avatar = models.ImageField(null=True,blank=True, upload_to="profil/avatars/")
	is_valid = models.BooleanField(default=False)
	email = models.EmailField()
	def __str__(self):
		return f"{self.user.username}-{self.user.email}-{self.is_valid}"

class Product(models.Model):
	owner = models.ForeignKey(User, related_name='proprietaire', on_delete=models.CASCADE)
	name = models.CharField(max_length=500)
	mark=models.ForeignKey('Mark',on_delete=models.CASCADE)
	price = models.IntegerField()
	date = models.DateField(default=timezone.now, blank=True)
	image1 = models.ImageField(default='', upload_to='products/')
	image2 = models.ImageField(default='', upload_to='products/')
	image3 = models.ImageField(default='', upload_to='products/')
	image4 = models.ImageField(default='', upload_to='products/')
	description = models.CharField(max_length=100)

	def __str__(self):
		return f"Nom : {self.name} Marque : {self.mark.name}"

class Mark(models.Model):
	name = models.CharField(max_length=200)
	logo = models.ImageField(upload_to="marks/logo")

	def __str__(self):
		return self.name



#class Panier(models.Model):
	#user=models.ForeignKey(User,on_delete = models.CASCADE)
	#item=models.CharField(max_length=30)
	#delivery=models.BooleanField(default = False)
	#maison=models.BooleanField(default = False)

	#def __str__(self):
		#return f"Items: {self.Item}"
    
=======
>>>>>>> origin/master

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
	nom = models.CharField(max_length=500)
	marque=models.CharField(max_length=50)
	prix = models.IntegerField()
	posted_date = models.DateField(default=timezone.now)
	photo1 = models.ImageField(default='', upload_to='products/')
	photo2 = models.ImageField(default='', upload_to='products/')
	photo3 = models.ImageField(default='', upload_to='products/')
	photo4 = models.ImageField(default='', upload_to='products/')
	description=models.CharField(max_length=100)

	def __str__(self):
		return f"Nom : {self.nom} Marque : {self.marque}"
