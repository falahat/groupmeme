import api

CLIENT = api.GroupmeClient()

class Group(object):
	"""docstring for Group"""
	def __init__(self, group_id):
		self.group_id = group_id
		self.messages = None

	def collect_messages(self):
		self.messages = api.CLIENT.get_all_group_messages(self.group_id)

	def create_like_network(self):
		pass;
		