from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import requests
import smtplib
from smtplib import SMTPException
from django.core.mail import EmailMessage
import json
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()

# Create your models here.
city_options = (
    ('Mumbai', 'Mumbai'),
    ('Delhi', 'Delhi'),
    ('Chennai', 'Chennai'),
    ('Banglore', 'Banglore'),
    ('Kolkata', 'Kolkata'),
)


class Mail(models.Model):
    email = models.CharField(max_length=100, blank=False, null=False, help_text=(
        "Enter reciever's email address"))
    name = models.CharField(max_length=100, blank=False, null=False, help_text=(
        "Enter reciever's name"))
    city = models.CharField(max_length=20, blank=False,
                            null=False, choices=city_options, help_text=(
                                "Enter reciever's city"))
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    time = models.TimeField(null=True, blank=True, default=current_time)

    def __str__(self):
        return f'{self.name} - {self.city}'


city_id = {"Mumbai": 1275339, "Delhi": 1261481,
           "Chennai": 1264527, "Banglore": 1267701, "Kolkata": 1275004}


@receiver(post_save, sender=Mail)
def send_email(sender, instance, **kwargs):
    name = instance.name
    email = instance.email
    city = instance.city
    api_key = os.getenv('api_key')
    print(api_key)
    cityId = city_id[city]
    url = f"https://api.openweathermap.org/data/2.5/weather?id={cityId}&appid={api_key}"
    response = requests.get(url).text
    response_info = json.loads(response)
    print(response)
    answer = response_info["main"]['temp'] - 273.15
    answer = str(round(answer, 2)) + '°C'
    icon_id = response_info["weather"][0]['icon']
    icon_url = f"http://openweathermap.org/img/w/{icon_id}.png"
    subject = f'Hi {name}, interested in our services'
    html_content = '<b>Temperature of %s : %s </b> <br/> <img src="%s"/>'
    message = EmailMessage(subject=subject, body=html_content % (city,
                                                                 answer, icon_url), to=[email])
    message.content_subtype = 'html'
    message.send()
