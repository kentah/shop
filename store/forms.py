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
		fields = ['first', 'last', 'user_name', 'pass_word', 'email']