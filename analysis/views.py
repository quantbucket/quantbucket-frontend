from django.shortcuts import render
from django.http import HttpResponse
from formtools.wizard.views import SessionWizardView
from django.views.generic.base import View
from services import Analysis
from .forms import AnalysisAlgorithmForm,AnalysisDatasetForm,AnalysisSchemaForm
import json

FORMS = [('0', AnalysisAlgorithmForm),
         ('1', AnalysisDatasetForm),
         ('2', AnalysisSchemaForm)]

TEMPLATES = {'0': 'analysis/algorithm.html',
             '1': 'analysis/dataset.html',
             '2': 'analysis/schema.html'}

class AnalysisListView(View):

	template_name = 'analysis/list.html'

	def get(self,request):
		analysis = Analysis()
		analysis = analysis.list()
		return render(request, self.template_name,{'analysis':analysis})

class AnalysisDetailView(View):

	template_name = 'analysis/detail.html'

	def get(self,request,id):
		analysis = Analysis()
		analysis = analysis.detail(id)
		return render(request, self.template_name,{'analysis':analysis})

class AnalysisWizard(SessionWizardView):
	form_list = [AnalysisAlgorithmForm, AnalysisDatasetForm, AnalysisSchemaForm]
	
	def get_template_names(self):
    		return [TEMPLATES[self.steps.current]]

    	def done(self, form_list, **kwargs):
    		return HttpResponseRedirect('/page-to-redirect-to-when-done/')