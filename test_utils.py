import unittest
import utils

class UtilsTestCase(unittest.TestCase):
  def test_get_config(self):
    self.assertTrue(type(utils.get_config()) is dict)
    self.assertFalse(utils.get_config() == None)

if __name__ == '__main__':
    unittest.main()
