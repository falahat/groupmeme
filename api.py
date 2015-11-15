import requests
import json

BASE_PATH = "https://api.groupme.com/v3/"

def get_auth_token():
	with open("/home/aryan/code/groupmeme/auth.key") as fp:
		return fp.read()

class GroupmeClient(object):
	"""docstring for GroupmeClient"""
	def __init__(self, auth_token = None):
		if auth_token:
			self.auth_token = auth_token
		else:
			self.auth_token = get_auth_token()

	def get_groups(self):
		url = BASE_PATH + "groups"
		params = {"token":self.auth_token}
		r = requests.get(url, params=params)
		return r.json()

	def get_group_message_chunk(self, group_id, max_messages=100, before_id=None, since_id=None):
		url = BASE_PATH + "groups/{}/messages".format(group_id)

		params = {"token" : self.auth_token, "limit" : 100}
		if before_id:
			params["before_id"] = before_id
		if since_id:
			params["since_id"] = since_id

		r = requests.get(url, params=params)
		if r and r.status_code == 200:
			ans = r.json()
			if ans and ans["response"]:
				ans = ans["response"]["messages"]
				# print ans
				return ans

	def group_message_generator(self, group_id, before_id=None):
		curr_messages = True

		while curr_messages:
			curr_messages = self.get_group_message_chunk(group_id, before_id=before_id)	
			if curr_messages:
				before_id = curr_messages[-1]["id"]
				yield curr_messages

	def get_all_group_messages(self, group_id, before_id=None, max_messages=None):
		all_messages = list()
		for chunk in self.group_message_generator(group_id, before_id):
			all_messages += chunk
			if max_messages and len(all_messages) > max_messages:
				break;
		return all_messages
