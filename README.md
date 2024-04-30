# Django CRM
This is a simple django CRM to handle customer data, product records and the purchases they made.
The purpose of this project is to show how we can use python and implement web based CRM. I have used python for various use cases and this ended up as a demo project I implemented while learning backend development with django.

# Tech Stack:
django python, Html, Css, Bootstrap, Postgresql

# Setup:
* Create a virtual env
* Install dependencies:
  `python -m pip install -r requirements.txt`
* Install postgresql database: I used a postgresql docker container but you can also install it locally.
* Create a .env file and setup the credentials for your pgsql connection.
  ```
  DB = "db_name"
  USER = "username",
  PASSWORD = "password",
  HOST = "your_host",
  PORT = "your_port"
  ```
* From the django-crm directory run
`python setupdb.py`

  If all works well then your db is setup.
  Now you can make migrations for creation of your admin tables by running

  `python manage.py makemigrations`
* Once everything is set now run:
  `python manage.py runserver`

This will start the backend server and you will be able to access the site on localhost:8000/webapp
![image](https://github.com/Haris-Ali007/django-crm/assets/54216004/bf726e2a-f021-4714-9a7f-f476b8c6065b)

# Features:
* User authentication and registeration 
* Add, update and delete customer, product records.
* Add purchase records by selecting the customer and product and quantity from dropdown fields.
* Inventory update based on the purchased products.
* Cookies to keep track of session and print dynamic message based on the visit

