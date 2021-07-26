# Neighbourhood Watch

## Author
Josphine Ndanu

## Description
A website to kepp a user in theloop about everything happening within their neighbourhhod

## Set Up and Installations

### Prerequisites
1. Python version 3.8
2. Django 
3. Pip
4. Virtual Environment(venv)


### Clone the  project 
Run the following command on the terminal:
`git clone https://github.com/ndanu-josy/Neighbourhood.git`


###  Project Setup
1. Create virtual environment (python3 -m venv virtual)
2. Activate virtual environment (. virtual/bin/activate)
3. Install  all dependancies ( pip install -r requirements.txt)
4. Create database (CREATE DATABASE hood;)
5. Make migrations

    #### Database Migrations
    python3 manage.py makemigrations neighapp
    python3 manage.py migrate

6. Run the application
    ### Run 
    python3.8 manage.py runserver

7.  Testing the application
     python3 manage.py test neighapp

### Admin Dashboard
    (https://hoodwtch.herokuapp.com//admin)
    username: moringa
    password: moringa123




### Search functionality
    search by business name 

## Technologies used
    Python 3.8
    Bootstrap
    Django
   
## Live Sute

[View Live Site.](https://hoodwtch.herokuapp.com/)

## License

This project is under the [MIT](LICENSE) license.