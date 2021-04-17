#!/bin/bash
cd /home/ubuntu/pyapps
source venv/bin/activate
cd Singheath_RMS
python manage.py notify_service
deactivate