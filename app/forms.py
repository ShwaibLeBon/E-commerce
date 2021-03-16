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

	name = forms.CharField(
		label='',
		widget=forms.TextInput(
			attrs={
				'placeholder':'name',
				'class':'form-control'
			


				}

			))

	mark = forms.ModelChoiceField(
		label='',
		queryset = Mark.objects.all(),
		widget=forms.Select(
			attrs={
				'placeholder':'mark',
				'class':'form-control'
			


				}

			))

	price = forms.IntegerField(
		label='',
		widget=forms.NumberInput(
			attrs={
				'placeholder':'price',
				'class':'form-control'
			


				}

			))

	image1=forms.FileField(
     label='',
     widget = forms.FileInput(
         attrs={
         'class':'form-control-file',
         'placeholder':'image1'
         }
     ))


	image2=forms.FileField(
     label='',
     widget = forms.FileInput(
         attrs={
         'class':'form-control-file',
         'placeholder':'image2'
         }
     ))


	image3=forms.FileField(
     label='',
     widget = forms.FileInput(
         attrs={
         'class':'form-control-file',
         'placeholder':'image3'
         }
     ))

	image4=forms.FileField(
     label='',
     widget = forms.FileInput(
         attrs={
         'class':'form-control-file',
         'placeholder':'image4'
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
		exclude = ['owner','date']


class MarkForm(forms.ModelForm):
	name = forms.CharField(
			label='name',
			widget=forms.TextInput(
				attrs={
					'placeholder':'name'
				}

			)

		)

	logo = forms.ImageField(
			label='logo',
			widget=forms.FileInput(
				attrs={
					'placeholder':'logo'
				}

			)

		)

	class Meta:
		model = Mark
		fields ='__all__'


