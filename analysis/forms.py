from django import forms

class AnalysisAlgorithmForm(forms.Form):
	algorithm = forms.CharField(max_length=100)

class AnalysisDatasetForm(forms.Form):
	dataset = forms.CharField(max_length=100)

class AnalysisSchemaForm(forms.Form):
	schema = forms.CharField(max_length=100)