from django import forms
from store.models import JoinForm


class Join(forms.ModelForm):
	# first = forms.CharField(max_length=60, blank=True, null=True)
	# last = forms.CharField(max_length=60, blank=True, null=True)
	# user_name = forms.CharField(max_length=20, blank=True, null=True)
	# pass_word = forms.CharField(min_length=6, max_length=10, blank=True, null=True)
	# email = forms.CharField(max_length=60, blank=True, null=True)


	class Meta:

		model = JoinForm
		fields = ('first', 'last', 'user_name', 'pass_word', 'email',)
		'''
		widgets = {
			'first': forms.fields.TextInput(attrs={
				'placeholder': 'Enter your first name',
				#'class': 'form-control',
				}),
			'last': forms.fields.TextInput(attrs={
				'placeholder': 'Enter your last name',
				#'class': 'form-control',
				}),
			'user_name': forms.fields.TextInput(attrs={
				'placeholder': 'Enter your desired username',
				#'class': 'form-control',
				}),
			'email': forms.EmailField(attrs={
				'placeholder': 'Enter your email address',
				#'class': 'form-control',
				})
			}
		'''