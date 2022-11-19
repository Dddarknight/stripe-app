# Stripe App
Provides an oppotunity to use Stripe tools for making purchases of individual items or orders, containing several items of different quantity.


## Links and tools
This project was built using these tools:
| Tool | Description |
|----------|---------|
| [Django](https://www.djangoproject.com/) |  "A high-level Python web framework" |
| [Stripe](https://stripe.com/docs) |  "Stripe’s software and APIs are used to accept payments, send payouts, and manage businesses online" |
| [poetry](https://python-poetry.org/) |  "Python dependency management and packaging made easy" |


## Installation
**Copy a project**
```
$ git clone git@github.com:Dddarknight/stripe-app.git
$ cd stripe-app
```

**Set up the environment**
```
$ pip install poetry
$ make install
```

**Set up environment variables**
```
$ touch .env
```
You have to write into .env file secret keys for Django and also publishable and private keys for Stripe. See .env.example.
To get SECRET_KEY for Django app:
```
$ python manage.py shell
>>> from django.core.management.utils import get_random_secret_key
>>> get_random_secret_key()
```
To get keys for Stripe, you have to create an account (this app provides the oppotunity to work with 2 pairs of keys for USD and for another currency). Follow the [link](https://dashboard.stripe.com/login).
Then add secret keys to .env file.

While development you can put your localhost to HOST variable.

**Dealing with migrations**
```
$ make migrate
```
**Launch**
```
$ make run
```
## Using app with Docker
You have to fill PostgreSQL credentials in .env file.
Then:
```
$ docker-compose up -d --build
$ docker exec -it stripe_app bash
# python manage.py migrate
# python manage.py createsuperuser
```
Then provide admin username/password for managing objects (items, orders).

## Description and usage
| Endpoints | Description |
|----------|---------|
| /item/{item_id}/ |  The page for buying the item.  |
| /item-intent/{item_id}/ |  The page for pre-buying the item.  |
| /order/{order_id}/ | The page for buying the order. Here you can see the list of items, their quantity, taxes and discounts. |
| /items/ |  The list of availible items.  |
| /orders/ |  The list of orders.  |
| /admin/ |  Can be used for creating items / orders.  |


## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)