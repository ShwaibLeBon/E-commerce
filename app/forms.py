from django import forms
from .models import* 


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

class ProductForm(forms.ModelForm):

	nom = forms.CharField(
		label='',
		widget=forms.TextInput(
			attrs={
				'placeholder':'nom',
				'class':'form-control'
			


				}

			))

	marque = forms.CharField(
		label='',
		widget=forms.TextInput(
			attrs={
				'placeholder':'marque',
				'class':'form-control'
			


				}

			))

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


	description = forms.CharField(
		label='',
		widget=forms.TextInput(
			attrs={
				'placeholder':'description',
				'class':'form-control'
			


				}

			))

	class Meta:
		model = Product
		exclude = ['owner']