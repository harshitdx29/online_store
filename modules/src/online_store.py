#!/usr/bin/env python
import json
import sys
from functools import wraps
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from flask import Flask, jsonify, request, Response

import utils
from database import collection


app = Flask('Online_Store')

config = utils.get_config()

#Authentication Region
def check_auth(username, password):
    uname = config.get('authenticate').get('username')
    passwd = config.get('authenticate').get('password')
    return username == uname and password == passwd

def authenticate():
  """Sends a 401 response that enables basic auth"""
  return Response(
  'Could not verify your access level for that URL.\n'
  'You have to login with proper credentials', 401,
  {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
      return authenticate()
    return f(*args, **kwargs)
  return decorated

@app.route("/health", methods=['GET'])
@requires_auth
def health_status():
    return jsonify({"status":"ok"})

#Product_dict containing Product Id and Product Name
def project_online_store_api(prod_dict):
    prod_id = prod_dict.get('product_id')
    prod_name =prod_dict.get('product_name')
    return get_prod_dict(prod_id,prod_name)

#Returns a dictionary of Product Id and Product Name 
def get_prod_dict(prod_id,prod_name):
  if not prod_id:
    data = {
      'product_id': "Product Id missing"
    }
    return data
  insert_into_mongo(prod_id, prod_name)
  data = {
    'product_id': prod_id,
    'product_name': prod_name
  }
  return data

def insert_into_mongo(product_id, product_name):
  try:
    collection.insert_one({'product_id':product_id,'product_name':product_name})
    return
  except:
    logging.error('Error inserting in Database')
    return

@app.route('/', methods=['GET'])
def home_page():
  return jsonify({'Success':'Welcome to Online Store'})

#Post request for adding products to store
@app.route('/add_product', methods=['POST'])
@requires_auth
def add_product():
  id = request.get_json(force = True, cache = True)
  if id:
    if not collection.find_one({'product_id':id['product_id']}):
      product = project_online_store_api(id)
      return json.dumps(product)
    else:
      return jsonify({'error':'Product already exists.'})
  else:
    return jsonify({'error':'Product Id Missing'})

#Post request for deleting products from store
@app.route('/delete_product', methods=['POST'])
@requires_auth
def deleted_product():
  id = request.get_json(force = True, cache = True) 
  if id:
    result = collection.delete_many({'product_id':id['product_id']})
    if result.deleted_count>0:        
      return jsonify({'success':'Product removed from store'})
    else:
      return jsonify({'error':"Product does not exist"})
  else:
    return jsonify({'error':'Product Id Missing'})

#Post request for editting product in store
@app.route('/edit_product', methods=['POST'])
@requires_auth
def edit_product():
  id = request.get_json(force = True, cache = True)    
  if id:
    result = collection.update_one(
      {'product_id':id['product_id']},
        {
          "$set": {
            'product_name': id['product_name']
          }
        })
    if result.matched_count>0:
      if result.modified_count>0:
        return jsonify({'success':'Product details updated'})
      else: 
        return jsonify({'error':'Nothing Changed'})  
    return jsonify({'error':"Product does not exist"})    
  else:
    return jsonify({'error':'Enter Data'})

#Get request to retreive information about product based on product id
@app.route('/product/<prodid>', methods=['GET'])
@requires_auth
def get_prod_info(prodid):
  try:
    result = json.dumps(collection.find_one({'product_id':prodid},{'_id':0}))
    if result == 'null':
      return jsonify({'error':'Please enter proper Id'})      
    else:
      return result
  except Exception as e:
    logging.error(str(e))
    abort(404)

#Get Request to retreive information of all the products in the store
@app.route('/products', methods=['GET'])
@requires_auth
def get_all_prod_info():
  product_list=[]
  try:
    cursor = collection.find({},{'_id':0})
    for doc in cursor:
      product_list.append(doc)
    return json.dumps(product_list) 
  except Exception as e:
    logging.error(str(e))
    abort(404)

@app.errorhandler(500)
def internal_error(error):
  return "500 Internal Server Error"

@app.errorhandler(404)
def not_found(error):
  return "404 Page Not Found Error"

@app.errorhandler(405)
def method_not_allowed(error):
  return "405 Method Not Allowed Error"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port = 80, debug=True)

