from django.template.response import TemplateResponse

def home(request):
	response = TemplateResponse(request, 'home/template.html', {})
	return response