import unittest
import groupmeme.config

class ConfigTests(unittest.TestCase):
    
    def testCreation(self):
    	CONFIG = groupmeme.config.ConfigClient()

    def testSimpleFetch(self):
    	CONFIG = groupmeme.config.ConfigClient()

    	val = CONFIG["caching_enabled"]
    	self.assertTrue(val is not None, "A valid value should be returned")

    def testPaths(self):
    	CONFIG = groupmeme.config.ConfigClient()
    	val = CONFIG["cache_path"]
    	self.assertTrue(val is not None, "A valid value should be returned")


    
if __name__ == '__main__':
    unittest.main()