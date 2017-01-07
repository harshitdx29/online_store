import unittest
import database

class DatabaseTestCase(unittest.TestCase):

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

  def test_dbConfig(self):
    self.assertTrue(database.dbConfig == 'heroku_n940r2hr')
    self.assertFalse(database.dbConfig == 'Random_String') 

  def test_collectionConfig(self):
    self.assertTrue(database.collectionConfig =='dataCollection')
    self.assertFalse(database.collectionConfig == 'Random_String')

  def test_user(self):
    self.assertTrue(database.user == 'harshit')
    self.assertFalse(database.user == 'Random_String')

  def test_password(self):
    self.assertTrue(database.password == 'mongo')
    self.assertFalse(database.password == 'Random_String')

if __name__ == '__main__':
    unittest.main()
