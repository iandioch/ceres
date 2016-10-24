import json

class Card(object):
	def __init__(self, name, template_location, data_location):
		self.name = name
		self.template_location = template_location
		self.data_location = data_location
		self.template = self._read_file(template_location)
		self.data = self.get_data()
	
	def _read_file(self, loc):
		"""Return the contents of the given file"""
		with open(loc, 'r') as filereader:
			return filereader.read()

	def get_data(self):
		"""Return the raw json string from file"""
		file_data = self._read_file(self.data_location)
		return file_data
		
