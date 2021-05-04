from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
from .models import *
from django.contrib.auth import login,logout,authenticate
# Create your views here.
def home(request):
	try:
		cart = Cart.objects.filter(user=request.user,paid=False).count()
	except Exception as e:
		print

	products = 	Product.objects.all()
	return render(request,'product.html',locals())
def account(request):
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

				user = authenticate(username = username,password=password)
				if user:
					login(request,user)
					messages.success(request,"vous etes connecte")
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
	return render(request,"login_logout.html",locals())

def deconnexion(request):
	logout(request)
	return redirect(home)
def productDetail(request,id):
	product = Product.objects.get(id=id)
	add_to_cart = Add_cartForm(request.POST or None)
	if add_to_cart.is_valid():
		quantity = add_to_cart.cleaned_data['quantity']
		amount = float(product.price)*float(quantity)
		Cart(user=request.user,product=product,quantity=quantity,amount=amount).save()
	
	return render(request,"productdetails.html",locals())
def createProduct(request):
	product_form = ProductForm (request.POST or None ,request.FILES)
	if product_form.is_valid():
		product_obj = product_form.save(commit = False)
		product_obj.owner = request.user
		product_obj.save()
		messages.success(request,"produit ajoute avec success")
		return redirect(home)
	else :
		messages.error(request,"erreur d'ajout")
		product_form = ProductForm()
	return render(request,"user/forms.html",locals())


def createMark(request):
	mark_form = MarkForm(request.POST ,request.FILES)
	if mark_form.is_valid():
		mark_form.save()
		messages.success(request, "mark ajoute avec success")
		return redirect(home)
	mark_form = MarkForm()
	return render(request,"user/forms.html",locals())

def products(request):
	all_product = Product.objects.all()
	return render(request,"product.html",locals())

def cart(request):
	carts = Cart.objects.filter(user=request.user,paid=False)
	return render(request,"cart.html",locals())

