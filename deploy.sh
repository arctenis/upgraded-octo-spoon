#!/bin/bash

set -o errexit

pip install -U pip
pip install -r requirements.txt
python manage.py collectstatic --noinput --settings=core.settings.prod
python manage.py createsuperuser --noinput --settings=core.settings.prod --username=jack --email=contact@nicolaschartier.fr
