# Techproj - django app created for technical task

## Setup

First setup .env file located in techproj_django directory
Then type this commands
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```
Usage:
This is implementation of integrated django admin panel with connection to PostgresDB

Admin panel is located by the adress /admin

The credentials will be ones that You have been written in createsuperuser command
There will be field test models which you can edit.
To add new fields head to main/models and create needed models.
Then add them to main/admin file and type following commands
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver # This command is not necessary if you don't want to run server after this
```

Then you will be able to access added fields in admin panel
