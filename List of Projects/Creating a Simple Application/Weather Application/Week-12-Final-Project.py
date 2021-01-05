# Week 12 programming assignment; Final Project
# Programming Assignment 12.1 by Kevin Angotti.
import requests
import json
api_key = '452a847163430917be8f26435eebce04'
city_url = 'http://api.openweathermap.org/data/2.5/weather?q='                                                          # weather url's from open weather map
zip_url = 'http://api.openweathermap.org/data/2.5/weather?q='                                                           # weather url's from open weather map

def cityName_search():
    cityName = input('Provide a valid {city name}, {state}, {country code}. ')
    inputList = cityName.split(',')
    try:
        cityName = requests.get(
            city_url + inputList[0] + ',' + inputList[1] + ',' + inputList[2] + '&units=imperial' + '&appid=' + api_key)
        if cityName.status_code == 200:                                                                                 # status of the connection
            print('Your connection was successful!', cityName.status_code)
            data = json.loads(cityName.text)                                                                            # pulls data from the API
            print('In ' + data['name'] + ' it will be ' + str(data['main']['temp']) + ' degrees and have ' +
                  data['weather'][0]['description'])                                                                    # prints returned data
            print('The low for today is ' + str(data['main']['temp_min']))                                              # prints returned data
            print('The high for today is ' + str(data['main']['temp_max']))                                             # prints returned data
        else:
            print('Search value error, check city name, state, or country. ', cityName.status_code)
    except requests.exceptions.RequestException as e:                                                                   # prints connection error
        print('An error was thrown here is the error. ')
        print(e)                                                                                                        # prints error code
        exit()

def zipCode_search():                                                                                                   # function to run the search by zip code or city name
    zipCode = input('Provide a valid US zip code. ')
    try:
        zipCode = requests.get(zip_url + '&zip=' + zipCode + '&units=imperial&appid=' + api_key)
        if zipCode.status_code == 200:                                                                                  # status of the connection
            print('Your connection was successful!', zipCode.status_code)
            data = json.loads(zipCode.text)                                                                             # pulls data from the API
            # print(data)
            print('In ' + data['name'] + ' it will be ' + str(data['main']['temp']) + ' degrees and have ' +
                  data['weather'][0]['description'])                                                                    # prints returned data
            print('The low for today is ' + str(data['main']['temp_min']))                                              # prints returned data
            print('The high for today is ' + str(data['main']['temp_max']))                                             # prints returned data
        else:
            print('Search value error, check zip code and try again. ', zipCode.status_code)                            # prints connection error
    except requests.exceptions.RequestException as e:
        print('An error was thrown here is the error. ')
        print(e)                                                                                                        # prints error code
        exit()


def main():
    while True:
        print('Welcome to the weather app, to see a forecast follow the prompts!')
        weather_forecast = input(
            'Please enter 0 to search weather by zip code or 1 to search by city name. Enter q to quit. ')              # tells the program search criteria
        if weather_forecast.lower() == 'q':
            print('Thanks for using the Weather app!')                                                                  # exits the weather app
            exit()
        else:
            if weather_forecast == '0':                                                                                 # tells program to search by zip code
                print('Please follow the prompts.')
                zipCode_search()                                                                                        # calls zip code search function
            elif weather_forecast == '1':                                                                               # tells program to search by city
                print('Please follow the prompts.')
                cityName_search()                                                                                       # calls city search function
            else:
                print('Please enter a valid entry. ')


main()
if __name__ == '__main__':
    main()                                                                                                              # runs main program
