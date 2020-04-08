# desenvolvimento-web-com-python-e-django-
Desenvolvimento web com Python e Django - Do Zero ao Deploy

## To Deploy Heroku
pip install gunicorn
pip install django-heroku
pip freeze > requirements.txt
heroku login
heroku create dev-web-com-python-e-django

heroku addons:create heroku-postgresql:hobby-dev

> Creating heroku-postgresql:hobby-dev on ⬢ dev-web-com-python-e-django... free
> Database has been created and is available
> ! This database is empty. If upgrading, you can transfer
> ! data from another database with pg:copy
>Created postgresql-pointy-86006 as DATABASE_URL

Create Procfile
web: gunicorn todoapp.wsgi

git add .
git commit -m "First Deploy"
git push heroku master

heroku run python manage.py migrate --app dev-web-com-python-e-django
heroku run python manage.py createsuperuser --app dev-web-com-python-e-django

