# Ayomi app, NPI calculator

## How to deploy the app

To deploy the projet use the command : 
`docker-compose up -d`

The front-end can be seen in `http://localhost:3000/`\
The back-end can be seen in `http://localhost:8000/`

## API routes

Get all items `http://localhost:8000/api/calculator`\
Post one item `http://localhost:8000/api/calculator`\
Delete one item `http://localhost:8000/api/calculator/ + item's id`\
Get the csv `http://localhost:8000/api/calculator/csv`

## Use pytest

To use pytest you need to be in the api folder\
Create your python environnment with `source env/bin/activate`\
Use pytest `python -m pytest tests/` **warning during the test the main database is used, be sure to have your data base empty**

## Docs

You can get the fast api documentation in `http://localhost:8000/docs`