# Django Template

This repo is just empty template. It helps to create new django project faster.

## Installation

### Copy all directories to your project folder
```
app_name
├── app
├── config
│   ├── api
│   │   └── v1
│   └── settings
├── manage.py
├── Pipfile
└── readme.md
```
### Install dependencies 
```
pipenv shell
pipenv install
```
### Set project secret key
  
1. Generate secret key
```bash
from django.core.management.utils import get_random_secret_key

secret_key = get_random_secret_key()
```
2. Copy this value to config.settings.base
```
SECRET_KEY = '<secret_key>'
```

### Set database in config.settings.dev

```
DATABASES = {
    'default': {
        'NAME': '<database_name>',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': 'dev',
        'PASSWORD': 'dev',
        'HOST': '127.0.0.1',
        'PORT': 5432,
        'CONN_MAX_AGE': 300
    }
}
```
### Create log directory
```
app_name
├── app
├── config
└── log  ← ← ←
```
