# Django ORM Safe Delete

This project show how you can safely delete Django Objects. It also gives the ability to restore or undelete soft-deleted instances. By default, Django Admin lets us use `delete selected` action to remove objects, I have globally disabled this action, included an three custom actions `Restore deleted Objects` for restoring, `Delete temporary Objects`, for soft delete and `Delete permanently Objects` for permanent delete.
This app can be run using docker.

## Prerequisites

- Docker
- Docker-compose

## Getting Started

Steps to build, and run project:

1. `cd` to root of project
2. `docker-compose build`
3. `docker-compose up`
4. `docker-compose exec web python manage.py makemigrations`
5. `docker-compose exec web python manage.py migrate`
6. `docker-compose exec web python manage.py createsuperuser`

To test signup on browser, go to:

## Examples of usage

`http://localhost:8000/admin/`
for soft delete objects:

.. image:: https://github.com/hubert10/django-orm-safedelete/blob/master/soft-restore-actions.jpg
   :width: 908
   :height: 557
   
## Links

Check out official documentation to this project:
https://pypi.org/project/django-permanent/
