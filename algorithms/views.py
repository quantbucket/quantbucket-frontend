from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
from services import Algorithm
from .forms import AlgorithmForm
import json

class AlgorithmListView(View):

	template_name = 'algorithms/list.html'

	def get(self,request):
		algorithm = Algorithm()
		algorithms = algorithm.list()
		return render(request, self.template_name,{'algorithms':algorithms})

class AlgorithmDetailView(View):

	template_name = 'algorithms/detail.html'

	def get(self,request,id):
		algorithm = Algorithm()
		algorithm = algorithm.detail(id)
		return render(request, self.template_name,{'algorithm':algorithm})

class AlgorithmCreateView(View):

	template_name = 'algorithms/create.html'

	def get(self,request):
		form = AlgorithmForm()
		return render(request, self.template_name, {'form': form})

	def post(self,request):
		form = AlgorithmForm(request.POST,request.FILES)
		files = request.FILES
		data = request.POST

		if form.is_valid():
			algorithm = Algorithm()
			new_algorithm = {
				'name' : data['name'],
				'developer' : 1,
				'version' : data['version'],
				'description' : data['description'],
				'repository' : data['repository']
			}
			image = {
				'image' : files['image']
			}
			new_algorithm = algorithm.create(new_algorithm,files=image)
			return HttpResponse('Algorithm was created')
		else:
			return HttpResponse('Some trouble with new algorithm')