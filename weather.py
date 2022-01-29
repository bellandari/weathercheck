import requests
from uszipcode import SearchEngine
import os
import sys
import key

# Clears the console due to an lack-of-library error I don't feel like installing
os.system('cls||clear')

# Main Function
def weathercheck():
    
    # Pulls API Key from hidden file
    password = key.keycode
    
    # Asks user for Zipcode of US Location
    zipcode = input("\nWeathercheck - Enter the Zipcode: ")
    
    # Response from API
    response = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?zip={zipcode}&units=imperial&appid={password}")

    # Dictionary for responses
    temp = round(response.json()['list'][0]['main']['temp'])
    feelslike = round(response.json()['list'][0]['main']['feels_like'])
    humidity = response.json()['list'][0]['main']['humidity']
    weather = response.json()['list'][0]['weather'][0]['main']
    description = response.json()['list'][0]['weather'][0]['description']
    degree_sign = u"\N{DEGREE SIGN}"

    # Zipcode Search Engine
    engine = SearchEngine()
    
    # Searches by Zipcode
    zipsearch = engine.by_zipcode(zipcode)

    # Output formatting
    print (f"\n     City: {zipsearch.major_city} \
        \n     Temperature: {temp}{degree_sign}F \
        \n     Feels Like: {feelslike}{degree_sign}F \
        \n     Humidity: {humidity}% \
        \n     Weather: {weather} \
        \n     Info: {description}\n")
    
    # Acts as a "While True" loop to prevent program from shutting down before results are read.
    choice = input("Check again? Y/N: ")
                   
    if choice == 'y':
        os.system('cls||clear')
        weathercheck()
        
    else:
        sys.exit()

weathercheck()