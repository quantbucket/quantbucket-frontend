from django import forms

class AlgorithmForm(forms.Form):
    name = forms.CharField(label='Name', max_length=255)
    version = forms.DecimalField(label='Version')
    description = forms.CharField( widget=forms.Textarea)
    image =  forms.ImageField(label='Image')
    repository = forms.CharField(label='Repository', max_length=255)