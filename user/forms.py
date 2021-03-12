from django import forms


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
