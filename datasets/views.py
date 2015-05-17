from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
from services import Dataset
from .forms import DatasetForm
import json

class DatasetListView(View):

	template_name = 'datasets/list.html'

	def get(self,request):
		dataset = Dataset()
		datasets = dataset.list()
		return render(request, self.template_name,{'datasets':datasets})

class DatasetDetailView(View):

	template_name = 'datasets/detail.html'

	def get(self,request,id):
		dataset = Dataset()
		dataset = dataset.detail(id)
		return render(request, self.template_name,{'dataset':dataset})

class DatasetCreateView(View):

	template_name = 'datasets/create.html'

	def get(self,request):
		form = DatasetForm()
		return render(request, self.template_name, {'form': form})

	def post(self,request):
		form = DatasetForm(request.POST,request.FILES)
		files = request.FILES
		data = request.POST

		if form.is_valid():
			dataset = Dataset()
			new_dataset = {
				'name' : data['name'],
				'user' : 1
			}
			data = {
				'data' : files['data']
			}
			
			new_dataset = dataset.create(new_dataset,files=data)
			return HttpResponse('Dataset was created')
		else:
			return HttpResponse('Some trouble with new dataset')