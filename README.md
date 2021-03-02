# Singheath_RMS Full Stack

## Environment
Setting up venv on windows

> python -m venv venv

and activating the venv on windows

> venv\Scripts\activate.bat

Setting up venv on linux/unix

> python3 -m venv venv

Note: You might need to install the python3-venv package. Just follow the command in the terminal

And activating

> source venv/bin/activate

Installing dependencies
> pip install -r requirements.txt

## Starting the app
Make sure you see (venv) infront of the user in the terminal
> python manage.py collectstatic

> python manage.py makemigrations

> python manage.py migrate

> python manage.py runserver

Go to localhost:8000 to see if the app is running

## Accessing admin panel
Go to http://localhost:8000/admin/login/?next=/admin/
You can login with tester:password1.1

## Changelog for 02 March 2021
1. Refined permission for side bar such that only auditors who are logged in can access it
2. Created 2 permission groups : "tenant" and "auditor". 
3. Removed registration page. Only super_user can add users now
4. created a decorator file in authentication app to simplify permission assigning and checking for auth for individual views
5. Refactored urls.py and view.py for app app. Split each urls and views out for refined control

