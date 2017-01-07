import unittest
import online_store
import flask

class OnlineStoreTestCase(unittest.TestCase):
  def test_check_auth(self):
    username = 'harshit'
    password = 'wingify'
    self.assertTrue(online_store.check_auth(username, password) == False)
    username = 'admin'
    password = 'secret'
    self.assertTrue(online_store.check_auth(username, password) == True)

  def test_authenticate(self):
    self.assertTrue(type(online_store.authenticate()) is flask.wrappers.Response)

if __name__ == '__main__':
    unittest.main()
