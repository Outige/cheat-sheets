LAST UPDATED: 13 December 2020

This README will document the process of getting a "hello world" style fastapi rest api up and running. We will be using a psotges instance hosted on heroku (istead of the sqlite option).

# Heroku postgres:

### `Add postgres to a new project`:
* login to heroku online
* create a new project
* \> Resources \> Find more add-ons \> Heroku Postgres \> Install Heroku Postgres
```
Add-on plan:
Hobby Dev - Free

App to provision to:
Your new app
```
* Submit Order Form

You have now added postgres to a new heroku project.

-------------------------------------------------------

### `Interacting with your postgres instance from a linux command line`:
* Login to heroku CLI - heroku login
* Go to the new postgres addon (this is using the browser)
* Setting > Database credentials
* Copy the Heroku CLI text
* Past the Heroku CLI text in a terminal. This should log you into you heroku postgres
* Find the name of your database in your credentials, under Database
* Use the database and perform normal postgres functionality
* For some useful postgres CLI commands refere to this [this](https://github.com/Outige/cheat-sheats) repo
-------------------------------------------------------

# Fast api with psotgres:

I wanted to learn as much as I could from the fast api docs. So the majority of the base code for this tut comes directly from there. In particular I followed the [FastAPI SQL (Relational) Databases](https://fastapi.tiangolo.com/tutorial/sql-databases/) tut.

## Directory structure:
To get started copy the files as follows:
```
.
└── sql_app
    ├── crud.py
    ├── database.py
    ├── __init__.py
    ├── main.py
    ├── models.py
    ├── requirements.txt
    ├── schemas.py
    └── setup.sql
```
* `.`: This is the parent directory where you will be putting all of your folders.
* `sql_app`: The package of our fastapp api. The name isn't that important but if you change it you need to change all the references to sql_app to the new name
* `requirements.txt`: These are the dependancies needed to run the code
* `__init__.py`: This is an empty file. It's required to tell python that sql_app is a package
* `database.py`: This file sets up variables needed by other files. It is kind of run as a main because there is loose code and sets up global variables for the app.
* `models.py`: Sqlalchemy models. Not sure the real nature between models.py and schemas.py and crud.py. More research is required.
* `schemas.py`: Pydantic models. Again I'm not sure the real nature between models.py and schemas.py and crud.py. More research is required.
* `crud.py`: The code for the variuos crud operations required by the routes in main.py.
* `main.py`: The main modules where all the fapi stuff happens. All the routes provided by the rest api.
* `setup.sql`: This is a sql dump file used to set up the heroku database to create the tables required with the correct schemas for this api. Setup.py is also used by the test cases (discussed later) to reset the database.

## Requirements:
OK now cd to your `.` directory. Now that you've got all the files you need, install the requirements:
```
$ pip install -r sql_app/requirements.txt
```

## Running the api:
You are now ready to launch the app. From your `.` directory run:
```
$ uvicorn sql_app.main:app --reload
```

You can now go to `http://127.0.0.1:8000` or on postman and test all the routes.

## Fapi docs:

If you go to `http://127.0.0.1:8000/docs` you can see that autogen fapi docs.

## Changes required:

### Changes in `database.py`:

You will find a line like this:
```python
SQLALCHEMY_DATABASE_URL = "some postgres URI"
```

You will want to replace the URI with your own. To get your URI, view the credentials of your postgres DB on heroku. Then copy the `URI` into `databases.py`.

Also bring your attention to this line:
```python
    SQLALCHEMY_DATABASE_URL#, connect_args={"check_same_thread": False}
```

The comented out option is needed when using a sqlite database (this is explained in the fapi tut). So if you are using an sqlite db then uncomment.

# Unit tests
We will now add the unit tests to our tut. To get started copy the files as follows:
```
.
├── sql_app
│   ├── crud.py
│   ├── database.py
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── requirements.txt
│   ├── schemas.py
│   └── setup.sql
└── tests
    ├── requirements.txt
    └── test_api.py
```

If you're making a new project then you obviously need to copy all of the files over again (remember to make all the necessary changes). Else you can keep your old `sql_app/` and just copy of `tests/`.

## Requirements:
OK now cd to your `.` directory. Now that you've got all the files you need, install the requirements:
```
$ pip install -r tests/requirements.txt
```

## Running the tests
Change directory to `tests/`. Then run the unit test command:
```
$ python -m unittest discover -p 'test*.py'
```

# caviots
* Still need to add doc strings
* Would like unit tests to run with sqlite db. Can't get sqlite to work