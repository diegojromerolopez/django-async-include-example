# django-async-include-example
A sample django site for the package [django-async-include](https://github.com/diegojromerolopez/django-async-include/).

# Instructions
* Clone repository and cd
* create virtual environment `python3 -m venv .venv`
* activate venv `source .venv/bin/activate`
* install dependencies `pip install -r requirements.txt`
* migrate db `python manage.py migrate`
* load data from fixtures `python manage.py loaddata shop_list/fixtures/shop_list.json`
* Start server `python manage.py runserver`
* Go to shoplist view `http://127.0.0.1:8000/shop_list/`

Update amount of items loaded in `shop_list.views.index` to your liking
