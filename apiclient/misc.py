import requests
import json

class Client():

	def __init__(self):
		self.methods = {}
		self.set_endpoint()
		self.set_resource()
		self.register_base_methods()
		self.register_methods()
		self.response = None

	def get(self,resource):
		response = requests.get(self.endpoint+resource)
		self.response = response.json()

	def post(self,resource,payload,files=None):
		response = requests.post(self.endpoint+resource, data=payload, files=files)
		self.response = json.loads(response.text)

	def add_method(self,name,path):
		self.methods[name] = path

	def get_method(self,name):
		return self.methods[name]

	def register_methods(self):
		return None

	def set_resource():
		return None

class Resource(Client):

	def set_endpoint(self):
		self.endpoint = 'http://localhost:8081'	

	def register_base_methods(self):
		self.add_method('list',self.resource)
		self.add_method('detail',self.resource+'{id}/')
		self.add_method('create',self.resource)

	def detail(self,id):
		self.get(self.get_method('detail').format(id=id))
		return self.response

	def list(self):
		self.get(self.get_method('list'))
		return self.response

	def create(self,payload,files=None):
		self.post(self.get_method('create'),payload,files)
		return self.response