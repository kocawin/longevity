# user-customized area for general recommendations

# usage

```bash
# activate python environment
pip install -r requirements.txt
python manage.py migrate
# crawl all articles since many articles do not have title and abstract
# python manage.py runscript get_articles
python manage.py runscript populate

# test recommendation
# More pregnancy related articles as input, less related articles are recommended
python manage.py test

# test recommendation with a specific user

export DJANGO_SUPERUSER_PASSWORD=admin;python manage.py createsuperuser --username admin --email admin@admin.com --no-input --skip-checks 
python manage.py runserver

# go to http://localhost:8000/articles/ to interactively test the recommendation
# After close some articles, refresh the page to see the new recommendations.
```