# django-async-include-example
A sample django site for the package [django-async-include](https://github.com/diegojromerolopez/django-async-include/).

# Instructions
* Clone repository and cd to repository directory.
* Create virtual environment `python3 -m venv .venv`
* Activate venv `source .venv/bin/activate`
* Install dependencies `pip install -r requirements.txt`
* Migrate db `python manage.py migrate`
* Load data from fixtures `python manage.py loaddata shop_list/fixtures/shop_list.json`
* Start server `python manage.py runserver`
* Go to shoplist view `http://127.0.0.1:8000/shop_list/`
* Modify URL GET "size" parameter to get more shop list items, e.g. `http://127.0.0.1:8000/shop_list/?size=20`
