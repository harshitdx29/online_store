Setup instructions:
1) pip install virtualenv
2) virtualenv venv
3) source venv/bin/activate
4) pip install -r requirements.txt
5) python modules/src/online_store_api.py

------------------------------------------------------------------------------------------------------------------------------------------
Request:GET curl -i -H "Content-Type: application/json" -u admin:secret 0.0.0.0:80/ - Welcome Page for the online store
Response:
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 43
Server: Werkzeug/0.11.15 Python/2.7.10
Date: Sat, 07 Jan 2017 09:20:48 GMT

{
  "Success": "Welcome to Online Store"
}

------------------------------------------------------------------------------------------------------------------------------------------
Request:GET curl -i -H "Content-Type: application/json" -u admin:secret 0.0.0.0:80/products - Fetching Information for all the products
Response:
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 94
Server: Werkzeug/0.11.15 Python/2.7.10
Date: Sat, 07 Jan 2017 09:18:30 GMT

[{"product_id": "25", "product_name": "Key"}, {"product_id": "30", "product_name": "Product"}]

------------------------------------------------------------------------------------------------------------------------------------------
Request:GET curl -i -H "Content-Type: application/json" -u admin:secret 0.0.0.0:80/product/<prodid> - Fetching Information for product with the given product id
Response:
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 43
Server: Werkzeug/0.11.15 Python/2.7.10
Date: Sat, 07 Jan 2017 09:19:44 GMT

{"product_id": "25", "product_name": "Key"}

------------------------------------------------------------------------------------------------------------------------------------------
Request:POST curl -i -H "Content-Type: application/json" -u admin:secret -X POST -d '{"product_id":"30","product_name":"Product"}' 
https://api-online-shop.herokuapp.com/add_product
Response:
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 47
Server: Werkzeug/0.11.15 Python/2.7.10
Date: Sat, 07 Jan 2017 09:06:57 GMT


