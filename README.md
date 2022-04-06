# InventoryAssignment

this project was created to skill assignment 

database have two models connected with FK

CRUD for these models  available from django admin panel (endpoint '/admin/')

to start this project your need provide next actions:

to install libriaries, use requirements

```
pip install -r requirements.txt
```
or
```
pip3 install -r requirements.txt
```

create database in Mysql
of switch to sqlite

```
python manage.py makemigrations 
python manage.py migrate
python manage.py createsuperuser
```

after this you can start project:

```
python manage.py runserver
```

or run test to check:

```
python manage.py test
```