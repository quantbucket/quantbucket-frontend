from apiclient.misc import Resource

class Dataset(Resource):

	def set_resource(self):
		self.resource = '/datasets/'