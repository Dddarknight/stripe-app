# Stripe App
Provides oppotunity to use Stripe tools for making purchases of individual items or orders, containing several items of different quantity.


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
To get keys fot Stripe, you have to create an account. Follow the [link](https://dashboard.stripe.com/login).
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

## Description and usage
| Endpoints | Description |
|----------|---------|
| /item/{item_id}/ |  The page for buying the item.  |
| /order/{order_id}/ | The page for buying the order. Here you can see the list of items, their quantity, taxes and discounts. |


## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)