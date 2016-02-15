import sys
import os
import groupmeme.config
import json 

CONFIG = groupmeme.config.ConfigClient()
cache_path = CONFIG["cache_path"]
caching_enabled = CONFIG["caching_enabled"]

def generate_key(fn, args):
	"""
	Generates a unique filename to store FN(*args) with.
	It is the function name followed by all of the input values separated by '_'
	"""
	key = str(fn.__name__)
	key += "_".join([str(arg) for arg in args])
	return key

def known(fn, args):
	"""
	Returns TRUE iff we've already cached FN(*ARGS)
	"""
	key = generate_key(fn, args)
	filepath = os.path.join(cache_path, key)
	return os.path.isfile(filepath)

def store_value(fn, args, value):
	"""
	Caches a known value for FN given ARGS as input
	This writes the value as a JSON file in a specified cache directory.
	"""
	key = generate_key(fn, args)
	filepath = os.path.join(cache_path, key) + ".json"
	to_store = {"VALUE" : value}
	with open(filepath, "w") as fp:
		json.dump(to_store, fp)

def get_value(fn, args):
	"""
	Assuming that we've cached the value of FN(*args), returns that known value
	"""
	key = generate_key(fn, args)
	filepath = os.path.join(cache_path, key)
	with open(filepath) as fp:
		return json.load(fp)["VALUE"]


def cache(fn):
	"""
	Decorate a function with this to cache that function's results

	This requires that a function's output depends only on its input
	and will always have the same output for the same input.

	This also requires function output to be convertible to/from JSON.
	Therefore, a function needs to return primative types, arrays, dicts, etc.
	"""
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

