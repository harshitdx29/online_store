import unittest
import database

class DatabaseTestCase(unittest.TestCase):
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
