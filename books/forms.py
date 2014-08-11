from django import forms

class ContactForm(forms.Form):
	subject=forms.CharField()
	email=forms.EmailField(required=False)
	message=forms.CharField()
class TestForm(forms.Form):
	name=forms.CharField(max_length=100)
	gender=forms.CharField()
class TestnextForm(forms.Form):
	email=forms.CharField(max_length=100)
class UploadFileForm(forms.Form):
	#title=forms.CharField(max_length=50)
	file=forms.FileField()
