# Introduction 
This is Django project that includes an API for managing restaurant information with the functionality described. We'll use Django's built-in ORM for interacting with the SQLite database and Django REST Framework (DRF) for creating the REST API endpoints.

# Prerequisites
1.	Python 3.6 or higher installed on system.
2.	Familiarity with virtual environments in Python.
3.  Basic knowledge of Django and the Django REST Framework.

# Build and Test
1.   Set Up Your Django Project:
    #   Install Django and DRF.
            pip install django djangorestframework
    #   Start a new Django project
            django-admin startproject restaurantproject
    #   Navigate to your project directory
            cd restaurantproject
    #   Start a new Django app
            python manage.py startapp restaurants
2.  Define Your Models:
    #   In restaurants/models.py, define your Restaurant model
    #   Make migrations and migrate to create the database schema
3.  Create Serializers:
    #   In restaurants/serializers.py, create a RestaurantSerializer class
4.  Create Views:
    #   In restaurants/views.py, create the necessary views using DRF's viewsets or APIViews
5.  Configure URLs:
    #   In 'restaurants/urls.py', set up your URL routes
    #   Include these in your project's urls in 'restaurantproject/urls.py'
6.  Set Up the DRF:
        Add 'rest_framework' and app, 'restaurants', to INSTALLED_APPS in 'settings.py'
7.  Testing API:
    #   To apply the changes made in models
            python manage.py makemigrations
            python manage.py migrate
    #   Run the development server
            python manage.py runserver

8. To install dependencies
    pip install -r requirements.txt

9.  API Endpoints
    #    By this endpoint we can retireve and create new restaurants
            http://127.0.0.1:8000/restaurants/


