<h1 align="center"> Gota: An Service for recipes </h1>

 <p align="left">
   <img src="https://img.shields.io/badge/STATUS-%20DEV-green">
</p>

# Table of Contents
- [Introduction](#Introduction)
- [Motivation](#Motivation)
- [Requirements](#Requirements)
- [Installation](#Installation)
- [Run](#Run)
- [Data](#Data)
- [Examples](#Examples)

# Introduction
Project in which a REST API is created to manage cooking recipes in the [Elasticsearch](https://www.elastic.co/es/what-is/elasticsearch) database in order to be able to:

- Create a new recipe
- Retrieve a recipe
- Modify a recipe
- Search a recipe by its name

# Motivation
For this project I wanted to integrate the [Django](https://docs.djangoproject.com/en/4.1/) framework with Elasticsearch to develop Api Rest in which you could store the recipe data, make intelligent searches and modify the values of the data fields. 

The decision to choose Django was to know how powerful the framework is and how easy is the integration with Elasticsearch. 

For its integration it was necessary to read the [django_elasticsearch_dsl](https://django-elasticsearch-dsl.readthedocs.io/en/latest/quickstart.html) documentation.

# Requirements
- Pip == 22.2.2
- Python == 3.10.7
- Django == 4.1.1
- Django-elasticsearch-dsl == 7.2.2
- Django-elasticsearch-dsl-drf == 0.22.5

# Installation
- Install python==3.10.7

        sudo apt update

        sudo apt install python3.10

        python --version

- Clone the repository

        git clone https://github.com/MiguelBarriosAlvarez/Recipes-Api-Rest.git

- Install virtual enviroment: 

        sudo apt-get install python3-pip

        sudo pip3 install virtualenv

        virtualenv venv

        source venv/bin/activate

- Install requirements

        pip install -r requirements.txt

# Run
In order to be able to make the Request in Django, the Elasticsearch and Django service must be started.
In this case it will be done from local.

## Elasticsearch
The file is composed of a docker compose and two sh files to start or stop the service

- Start Elasticsearch

        sh start.sh


   - Elasticsearch: http://127.0.0.1:9200/

   - Kibana: http://127.0.0.1:560/

- Stop Elasticsearch

        sh stop.sh

## Django

    cd \Recipes-Api-Rest
    python .\manage.py runserver

# Data
I have decided to realize the following data model for Elasticsearch documents as follows in the example:

     {
        "name" : "French fries",
        "ingredients" : [
            {
            "quantity" : "500 grams",
            "ingredient" : "Potatoes"
            },
            {
            "quantity" : "100 milliliters",
            "ingredient" : "Oil"
            }
        ],
        "steps" : [
            {
            "description" : "Peel the potatoes",
            "step" : 1
            },
            {
            "description" : "Fry the potatoes",
            "step" : 2
            }
        ],
        "labels" : [
            "potatoes",
            "fried",
            "american",
            "food garnish"
        ],
        "timestamp" : "2022-09-15T15:42:44.694641Z"
    }

I have considered this model for the design as I consider it interesting to store all the information and be able to access it through elasticsearch queries.

# Examples
In this section I show some examples to be able to make requests to the API of recipes:
The JSON French fries is taken into account in the BODY.

### Create a new recipe

    curl --location --request GET 'http://127.0.0.1:8000/api/new/' \
    --header 'Content-Type: text/plain' \
    --data-raw '
        {BODY}'

### Retrieve a recipe
Simple search by recipe name. The API could be modified to search by register ID.

    curl --location --request GET 'http://127.0.0.1:8000/api/view/' \
    --header 'Content-Type: text/plain' \
    --data-raw '
        {
        "name" : "French fries"
        }'


### Modify a recipe
Through this request we can modify the value of a field of our choice, selecting the recipe by its name

    curl --location --request GET 'http://127.0.0.1:8000/api/update/' \
    --data-raw '{
        "field": "name",
        "value": "French Fries with Cheese"
        "query": "French fries"
    }'


- field: The field whose value is to be updated
- value: The value we want to update
- query: The name of the recipe we want to update

### Search a recipe
Through this request we can search for a recipe according to a related term in the recipes.
The search takes into account all the fields and thanks to the Elasticsearch parsers makes it more effective.

        curl --location --request GET 'http://127.0.0.1:8000/api/search/' \
        --data-raw '{
            "term": "garnish"
        }'


