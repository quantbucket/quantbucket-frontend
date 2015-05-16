from django.shortcuts import render
from django.views.generic.base import View,TemplateView
from services import Algorithm

class AlgorithmListView(View):

	template_name = 'algorithms/list.html'

	def get(self,request):
		algorithm = Algorithm()
		algorithms = algorithm.list()
		return render(request, self.template_name,{'algorithms':algorithms})

class AlgorithmDetailView(TemplateView):

	template_name = 'algorithms/detail.html'

	def get(self,request,id):
		algorithm = Algorithm()
		algorithm = algorithm.detail(id)
		return render(request, self.template_name,{'algorithm':algorithm})