from django import forms

class DatasetForm(forms.Form):
    name = forms.CharField(label='Name', max_length=255)
    data =  forms.FileField(label='Data')