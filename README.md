# Singheath_RMS Full Stack

## Environment
Setting up venv on windows

> python -m venv vevn

and activating the venv on windows

> venv\Scripts\activate.bat

Setting up venv on linux/unix

> python -m venv venv

and activating

> source venv/bin/activate

## Starting the app
Make sure you see (venv) infront of the user in the terminal
> python manage.py collectstatic

> python manage.py makemigrations

> python manage.py migrate

> python manage.py runserver

Go to localhost:8000 to see if the app is running
