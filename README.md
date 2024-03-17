# This is Tour agency project

To use this set enviorment using following command

> **Step 1** - Install dependencies using a `virtual environment`

```bash
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ pip install -r requirements.txt
```

<br />

> **Step 2** - Setup the database 

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> **Step 4** - Start Project

```bash
$ python manage.py runserver 
```