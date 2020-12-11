Written: 11 December 2020

This README will document the process of getting a "hello world" style fastapi rest api up and running. We will be using a psotges instance hosted on heroku (istead of the sqlite option).

# Heroku postgres

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

# Running the api
* intsall the requirements `sql_app/requirements.txt`
* cd to `heroku_rest_api`
* run the start command
```
$ uvicorn sql_app.main:app --reload
````