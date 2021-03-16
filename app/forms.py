from django import forms
<<<<<<< HEAD
from .models import*
=======
from .models import* 
>>>>>>> origin/master


class ProfileForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(
		attrs={
		'type':'text', 
		'placeholder':'Username', 

		}))
	email = forms.CharField(widget=forms.EmailInput(
		attrs={
		'type':'email', 
		'placeholder':'email', 

		}))
	phone_number = forms.CharField(widget=forms.TextInput(
		attrs={
		'type':'tel', 
		'placeholder':'Telephone', 

		}))
	password = forms.CharField(widget=forms.PasswordInput(
		attrs={
		'type':'password', 
		'placeholder':'password', 

		}))
class ConnexionForm(forms.Form):
	"""docstring for ConnexionForm"""
	username = forms.CharField(widget=forms.TextInput(
		attrs={
		'type':'text',
		'placeholder':'Username',
		}))
	password = forms.CharField(widget=forms.TextInput(
		attrs={
		'type':'password',
		'placeholder':'password',
		}))

<<<<<<< HEAD
class ProductForms(forms.ModelForm):

	name = forms.CharField(
		label='',
		widget=forms.TextInput(
			attrs={
				'placeholder':'Nom',
=======
class ProductForm(forms.ModelForm):

	nom = forms.CharField(
		label='',
		widget=forms.TextInput(
			attrs={
				'placeholder':'nom',
>>>>>>> origin/master
				'class':'form-control'
			


				}

			))

<<<<<<< HEAD
	mark = forms.ModelChoiceField(
		label = '',
		queryset = Mark.objects.all(),
		widget = forms.Select(
			attrs={
				
				'class' : 'form-control',
				'placeholder':''
=======
	marque = forms.CharField(
		label='',
		widget=forms.TextInput(
			attrs={
				'placeholder':'marque',
				'class':'form-control'
			

>>>>>>> origin/master

				}

			))

<<<<<<< HEAD
	price = forms.IntegerField(
 		label='Prix',
 		widget=forms.NumberInput(
 			attrs={
 				'placeholder':'',
 				'class':'form-control'
				


 				}

 			))

	date = forms.DateField(
 		label='',
 		widget=forms.DateInput(
 			attrs={
 				'placeholder':'Date',
 				'class':'form-control',
 				'type':'date'
				


 				}

 			))

	image1=forms.FileField(
         label='',
         widget = forms.FileInput(
             attrs={
             'class':'form-control-file',
             'placeholder':''
             }
         ))


	image2=forms.FileField(
         label='',
         widget = forms.FileInput(
             attrs={
             'class':'form-control-file',
             'placeholder':''
             }
         ))


	image3=forms.FileField(
         label='',
         widget = forms.FileInput(
             attrs={
             'class':'form-control-file',
             'placeholder':''
             }
         ))

	image4=forms.FileField(
         label='',
         widget = forms.FileInput(
             attrs={
             'class':'form-control-file',
             'placeholder':''
             }
         ))
=======
	prix = forms.IntegerField(
		label='',
		widget=forms.NumberInput(
			attrs={
				'placeholder':'prix',
				'class':'form-control'
			


				}

			))

	posted_date = forms.DateField(
		label='',
		widget=forms.DateInput(
			attrs={
				'placeholder':'date',
				'class':'form-control',
				'type':'date'
			


				}

			))

	photo1=forms.FileField(
     label='',
     widget = forms.FileInput(
         attrs={
         'class':'form-control-file',
         'placeholder':'photo1'
         }
     ))


	photo2=forms.FileField(
     label='',
     widget = forms.FileInput(
         attrs={
         'class':'form-control-file',
         'placeholder':'photo2'
         }
     ))


	photo3=forms.FileField(
     label='',
     widget = forms.FileInput(
         attrs={
         'class':'form-control-file',
         'placeholder':'photo3'
         }
     ))

	photo4=forms.FileField(
     label='',
     widget = forms.FileInput(
         attrs={
         'class':'form-control-file',
         'placeholder':'photo4'
         }
     ))
>>>>>>> origin/master


	description = forms.CharField(
		label='',
		widget=forms.TextInput(
			attrs={
<<<<<<< HEAD
				'placeholder':'',
=======
				'placeholder':'description',
>>>>>>> origin/master
				'class':'form-control'
			


				}

			))

	class Meta:
		model = Product
<<<<<<< HEAD
		exclude = ['owner']

class MarkForms(forms.ModelForm):

	name = forms.CharField(
 		label='',
 		widget=forms.TextInput(
 			attrs={
 				'placeholder':'',
 				'class':'form-control'
				


 				}

 			)) 
	logo=forms.FileField(
		label='',
		widget = forms.FileInput(
			attrs={
             'class':'form-control-file',
             'placeholder':''
             }
         ))

	class Meta:
 		model = Mark
 		fields = '__all__'

#class PanierForms(forms.ModelForm):
 	#item = forms.IntegerField(
 		#label='',
 		#widget=forms.NumberInput(
 			#attrs={
 				#'placeholder':'',
 				#'class':'form-control'
				


 				#}

 			#))

 	#class Meta:
 		#model = Product
 		#exclude = ['livraison','maison','user']










=======
		exclude = ['owner']
>>>>>>> origin/master
