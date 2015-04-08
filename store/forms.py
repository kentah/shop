from django import forms
from store.models import JoinForm


class Join(forms.models.ModelForm):
	# first = forms.CharField(max_length=60, blank=True, null=True)
	# last = forms.CharField(max_length=60, blank=True, null=True)
	# user_name = forms.CharField(max_length=20, blank=True, null=True)
	# pass_word = forms.CharField(min_length=6, max_length=10, blank=True, null=True)
	# email = forms.CharField(max_length=60, blank=True, null=True)


	class Meta:

		model = JoinForm
		fields = ('first_name','last_name', 'username', 'password', 'email')
		widgets = {
			'first_name': forms.fields.TextInput(attrs={
				'placeholder': 'Enter your first name',
				'class': 'form-control form-group',
				}),
			'last_name': forms.fields.TextInput(attrs={
				'placeholder': 'Enter your last name',
				'class': 'form-control form-group',
				}),
			'username': forms.fields.TextInput(attrs={
				'placeholder': 'Enter your desired username',
				'class': 'form-control form-group',
				}),
			'password': forms.PasswordInput(attrs={
				'placeholder': 'Enter your desired password',
				'class': 'form-control form-group',
				}),
			'password1': forms.PasswordInput(attrs={
				'placeholder': 'Verify Password',
				'class': 'form-control form-group'}),
			'email': forms.fields.TextInput(attrs={
				'placeholder': 'Enter your email address',
				'class': 'form-control form-group',
				})
			}

class Login(forms.models.ModelForm):
	pass
	