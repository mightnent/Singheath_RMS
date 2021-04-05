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

## Working with AWS
Use the video resource in the group on how to access the AWS instance via winSCP, a SFTP program. 
Then use it to open the terminal (or you can use putty directly. Having winscp just gives a better idea visually)

In the terminal, go to pyapps (you can see it when you ls)
You can activate the venv along the way

Go to Singhealth_RMS folder

Do your standard git fetch, checkout, pull etc. 

Then open up my screen program. 
> screen -r main

This is where the django is running. You can ctrl+c to stop it and do your typical django python manage.py stuff. 

When you are ready, you can run it using 
> python manage.py runserver 0.0.0.0:8000
(or you can just use the up arrow to find this command)

Exit the screen by Crtl + A, then press D
### Side note on the AWS
You can just use the aws instance like any linux ssh. So you can execute anything in it normally. 

## Accessing admin panel
Go to http://localhost:8000/admin/login/?next=/admin/
You can login with tester:password1.1

## Changelog for 02 March 2021
1. Refined permission for side bar such that only auditors who are logged in can access it
2. Created 2 permission groups : "tenant" and "auditor". 
3. Removed registration page. Only super_user can add users now
4. created a decorator file in authentication app to simplify permission assigning and checking for auth for individual views
5. Refactored urls.py and view.py for app app. Split each urls and views out for refined control

## Changelog for 13 March 2021
1. Did up HTML,CSS (frontend) skeleton template for fnb-checklist

## Changelog for 22 March 2021
1. Created a checklist app so that master admin can do up a new checklist. In other words, the each checklist is dynamic, you can create different checklist, different sections, different subsections and different questions
2. Integrated front and backend to dynamically displaying checklist questions on the fnb-checklist

## Changelog for 23 March 2021
1. Created an audit app, including database models, so to receive new audit checklist instances as categorised by tenant location, institution
2. Created institution security group for future use, so can limit what a normal auditor can see based on institution he is from

## Changelog for 25 March 2021
1. Merged various branch
    1. Admin css
    2. Templates for audit
    3. Templates for new audits
    4. Templates for manage tenant
    5. Template for performance graph
2. Reroute admin login to backend dashboard
3. Integrate backend to manage tenant page, ability to create a tenant from front end. 
4. When tenant created, auto create user and assign tenant user group to the user
5. Fixed scroll issue on physical mobile device
6. Created model for tenant, checklistinstance
7. Migrated to psql
8. Hosted on AWS