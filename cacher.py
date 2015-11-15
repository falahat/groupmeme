import sys
import os
import groupmeme.config
import json 

CONFIG = groupmeme.config.ConfigClient()
cache_path = CONFIG["cache_path"]
caching_enabled = CONFIG["caching_enabled"]

def generate_key(fn, args):
	key = str(fn.__name__)
	key += "_".join([str(arg) for arg in args])
	return key

def known(fn, args):
	key = generate_key(fn, args)
	filepath = os.path.join(cache_path, key)
	return os.path.isfile(filepath)

def store_value(fn, args, value):
	key = generate_key(fn, args)
	filepath = os.path.join(cache_path, key)
	to_store = {"VALUE" : value}
	with open(filepath, "w") as fp:
		json.dump(to_store, fp)

def get_value(fn, args):
	key = generate_key(fn, args)
	filepath = os.path.join(cache_path, key)
	with open(filepath) as fp:
		return json.load(fp)["VALUE"]


def cache(fn):

	def inner(*args):
		if not known(fn, args):
			value = fn(*args)
			store_value(fn, args, value)
		else:
			value = get_value(fn, args)

		return value

	if caching_enabled:
		return inner
	else:
		return fn

