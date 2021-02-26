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
