from apiclient.misc import Resource

class Analysis(Resource):

	def set_resource(self):
		self.resource = '/analysis/'

	def register_methods(self):
		self.add_method('do',self.resource)

	def do(self,dataset_id,algorithm_id,schema):
		payload = {
			'dataset' : dataset_id,
			'algorithm' : algorithm_id,
			'schema' : schema
		}
		self.post(self.get_method('do'),payload)