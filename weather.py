import requests
import os
import sys
import key
import click

#os.system('cls || clear')

#class weathercheck:
        
@click.command()
@click.option("--city", "-c", prompt = True)

def weather(city):
    
    # Pulls API Key from hidden file
    password = key.keycode
    
    # Asks user for name of city 
    
    # Response from API
    response = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?q={city}&units=imperial&appid={password}")
    
    # Handles error if typo in city
    if response.json()['cod'] == "404":
        
        click.echo ("Was there a typo? Try again!")
        
        weather()
        
    else: 
        
        # Dictionary for responses
        temp = round(response.json()['list'][0]['main']['temp'])
        feelslike = round(response.json()['list'][0]['main']['feels_like'])
        humidity = response.json()['list'][0]['main']['humidity']
        weather = response.json()['list'][0]['weather'][0]['main']
        info = response.json()['list'][0]['weather'][0]['description']
        degree_sign = u"\N{DEGREE SIGN}"

        click.echo (f"\nIt is currently {temp}{degree_sign}F in {city} with {info}. It feels like {feelslike}{degree_sign}F, with a humidity of {humidity}%. \n")

weather()