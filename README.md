# Hunter

## About Hunter
```
TBD
```

### Install & configure Hunter virtual environment.
```
$ virtualenv --/usr/bin/python hunter
$ source hunter/bin/activate
$ pip install -r requirements.txt
$ export HUNTER_SECRET_KEY=SOME-VERY-SECRET-KEY
```

### Run database migration
```
(hunter)$ python manage.py migrate
```

### Run Django app
```
(hunter)$ python manage.py runserver  
```

### Deactivate virtual environement
```
(hunter)$ deactivate
$
```
