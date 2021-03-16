from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
from .models import *
from django.contrib.auth import login,logout,authenticate
# Create your views here.
def home(request):
	products = Product.objects.all()
	return render(request,'user/dashboard.html',locals())
def profile(request):
	registrer_form = ProfileForm(request.POST or None)
	connexion_form = ConnexionForm(request.POST or None)
	if "enregistrer" in request.POST:
		if registrer_form.is_valid():
			username = registrer_form.cleaned_data['username']
			email = registrer_form.cleaned_data['email']
			phone_number = registrer_form.cleaned_data['phone_number']
			password = registrer_form.cleaned_data['password']
			try:
				user = User.objects.create_user(username=username,password=password)
				user.save()

				profile = Profile(user=user,phone_number=phone_number)
				profile.email = email
				profile.save()
				messages.success(request, "enregistre avec succes")
				return redirect(home)
			except Exception as e:
				messages.error(request,"NOM DEJA PRIS")
				registrer_form = ProfileForm()
		registrer_form = ProfileForm()
	if "connexion" in request.POST:
		if connexion_form.is_valid():
			username = connexion_form.cleaned_data['username']
			password = connexion_form.cleaned_data['password']
			try:
				user = authenticate(username = username,password=password)
				if user:
					login(request,user)
					messages.success(request,"vous etes connecte")
					return redirect(home)

			except Exception as e:
				messages.error(request,"vous n etes pas connecte")
			
	return render(request, 'user/account.html',locals())

def registrer(request):
	
	return(request,'user/account.html',locals())
def deconnexion(request):
	logout(request)
	return redirect(profile)

def productDetails(request,id):

	product = Product.objects.get(id=id)

	return render(request,"productdetails.html",locals())

def createProduct(request):
	product_form = ProductForms(request.POST or None,request.FILES)
	if(product_form.is_valid()):
		prod_object = product_form.save(commit = False)
		prod_object.owner=request.user
		prod_object.save()
		messages.success(request,"Produit ajoute avec success")
		return redirect(home)
	else:
		messages.error(request,"Erreur d'ajout")
		product_form = ProductForms()
	return render(request,"user/forms.html",locals())	

def productMark(request):

	mark_form = MarkForms(request.POST or None,request.FILES)
	if(request.method=='POST'):
		if(mark_form.is_valid()):
			mark_form.save()
	mark_form = MarkForms()
	return render(request,"user/forms.html",locals())

def products(request):

	productz=Product.objects.all()
	return render(request,"product.html",locals())








