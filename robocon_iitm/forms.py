from django import forms
from models import Thread
class Blog(forms.ModelForm):
	class Meta:
		model = Thread
		fields=['title','subject','pic','description']