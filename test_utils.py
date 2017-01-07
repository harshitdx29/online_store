import unittest
import utils

class UtilsTestCase(unittest.TestCase):
  @classmethod
  def setup_class(klass):
    """This method is run once for each class before any tests are run"""

  @classmethod
  def teardown_class(klass):
    """This method is run once for each class _after_ all tests are run"""

  def setUp(self):
    self.tester = app.test_client(self)
    self.config = utils.get_config()

  def teardown(self):
    print "TEAR DOWN!"

  def test_get_config(self):
    self.assertTrue(type(utils.get_config()) is dict)
    self.assertFalse(utils.get_config() == None)

if __name__ == '__main__':
    unittest.main()
