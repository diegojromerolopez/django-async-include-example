#!/bin/bash

python manage.py collectstatic --noinput
python manage.py migrate
python manage.py loaddata /app/shop_list/fixtures/shop_list.json
python manage.py runserver 0.0.0.0:8000