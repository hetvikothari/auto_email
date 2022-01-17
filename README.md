# auto_email

_____________________________________________________________________________________________

### Tech Stack Used
#### Backend - Django
#### Database - SQLite
#### Deployment - Heroku
#### API - https://openweathermap.org/api

_____________________________________________________________________________________________

### Features
## A Django server built for sending automatic emails.
## Users can send email with the temperature of the receiver's city at the time of sending mail.
## Weather Data fetched using API.
## Weather API Used: https://openweathermap.org/api

________________________________________________________________________________________________

### Steps to install
#### Clone the repository
`git clone https://github.com/hetvikothari/auto_email/`
#### Create a virtual environment 
`python3 -m venv <name of the environment>`
#### Activate the virtual environment 
`<name of the environment>/Scripts/activate`
#### Install the requirements.
`pip install -r 'requirements.txt'`
#### Create a .env file and add your email password and API_KEY for "hps://openweathermap.org/api" API
#### Make migrations
`python manage.py makemigrations`
`python manage.py migrate`
#### Run the following command to start the server
`python manage.py runserver`
#### Go to http://localhost:8000/admin/
