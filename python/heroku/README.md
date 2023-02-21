This readme is setup for all the tricks and setup I have learned for heroku. It should be noted that I have only used Heroku to set up a flask app deployment, so a lot of this cheat sheet will be from those learnings.


# Getting a simple flask app up on heroku

Following [this](https://www.youtube.com/watch?v=Li0Abz-KT78) tutorial

## Sign up to heroku

(As straight forward as it sounds)

## Install the Heroku CLI

For more information go to [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) webpage

1. Install heroku CLI
```
$ sudo snap refresh 
$ sudo snap install --classic heroku
```
2. Restart terminal


## Modify simple flask app

1. `>` git level directory of your flask app
2. Activate your virtual environment (please refer back to virtual env notes or some `virtualenv` tutorial)
3. `$ pip install`
4. (optional) Test server
```
$ gunicorn wsgi:app
```
5. Let heroku know we are using gunicorn
    1. `$ touch Procfile`
    1. `$ vim Procfile`
    1. Insert `web: gunicorn wsgi:app` (if your layout is identical to my simple flask tutorial layout)
6. Freeze current requirements
```
$ pip freeze > requirements.txt
```

## Commit changes and push to heroku

1. Commit changes

2. Login to heroku
```
$ heroku login
```

3. Create heroku app
```
$ heroku create
```

4. (optional) rename app
```
$ heroku rename some-name
```

5. Push code to heroku
```
$ git push heroku some-branch # the branch of our git we want to push, probably master

$ git push heroku master
```