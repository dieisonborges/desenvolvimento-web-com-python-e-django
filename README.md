# desenvolvimento-web-com-python-e-django-
Desenvolvimento web com Python e Django - Do Zero ao Deploy

## To Deploy Heroku
pip install gunicorn
pip install django-heroku
pip freeze > requirements.txt
heroku login
heroku create dev-web-com-python-e-django

heroku addons:create heroku-postgresql:hobby-dev

- Creating heroku-postgresql:hobby-dev on ⬢ dev-web-com-python-e-django... free
- Database has been created and is available
- ! This database is empty. If upgrading, you can transfer
- ! data from another database with pg:copy
-Created postgresql-animate-81915 as DATABASE_URL

Create Procfile
web: gunicorn todoapp.wsgi --log-file -

git add .
git commit -m "First Deploy"
git push heroku master

heroku run python manage.py migrate --app dev-web-com-python-e-django
heroku run python manage.py createsuperuser --app dev-web-com-python-e-django


## COLLECTSTATIC Problem

This worked for me, run the following commands:

disable the collectstatic during a deploy

heroku config:set DISABLE_COLLECTSTATIC=1

deploy

git push heroku master

run migrations (django 1.10 added at least one)

heroku run python manage.py migrate

run collectstatic using bower

heroku run 'bower install --config.interactive=false;grunt prep;python manage.py collectstatic --noinput'

enable collecstatic for future deploys

heroku config:unset DISABLE_COLLECTSTATIC

try it on your own (optional)

heroku run python manage.py collectstatic

