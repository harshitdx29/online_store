import unittest
import online_store
import flask
import utils
from flask import request
from online_store import app
from functools import wraps

class OnlineStoreTestCase(unittest.TestCase):

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

  def test_check_auth(self):
    username = 'harshit'
    password = 'wingify'
    self.assertTrue(online_store.check_auth(username, password) == False)
    username = 'admin'
    password = 'secret'
    self.assertTrue(online_store.check_auth(username, password) == True)

  def test_authenticate(self):
    self.assertTrue(type(online_store.authenticate()) is flask.wrappers.Response)

  def test_project_online_store_api(self):
    dict = {}
    data1 = {
      'product_id': "Product Id missing"
    }
    self.assertTrue(online_store.project_online_store_api(dict) == data1)
    dict = {'product_id': '1', 'product_name': 'Test Product'}
    data2 = {
      'product_id': '1',
      'product_name': 'Test Product'
    }
    self.assertTrue(online_store.project_online_store_api(dict) == data2)
    self.assertFalse(online_store.project_online_store_api(dict) == data1)

  def test_get_prod_dict(self):
    prod_id = ""
    prod_name = "Test Product"
    data = {
      'product_id': "Product Id missing"
    }
    self.assertTrue(online_store.get_prod_dict(prod_id, prod_name) == data)
    prod_id = 1
    data = {
      'product_id': prod_id,
      'product_name': prod_name
    }
    self.assertTrue(online_store.get_prod_dict(prod_id, prod_name) == data)

  def test_health(self):
    with app.test_request_context():
      response = self.tester.get('/health')
      self.assertTrue(response.status_code == 401)

if __name__ == '__main__':
    unittest.main()
