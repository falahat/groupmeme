import json
import os 

class ConfigClient(object):

	def __init__(self):
		self.BASE_PATH = os.path.dirname(os.path.abspath(__file__))

		with open(os.path.join(self.BASE_PATH, "config.json")) as fp:
			self.config_dict = json.load(fp)

	def __getitem__(self, key):
		if key not in self.config_dict:
			return None
		val = self.config_dict[key]
		if "path" in key:
			val = os.path.join(self.BASE_PATH, val)
		return val
