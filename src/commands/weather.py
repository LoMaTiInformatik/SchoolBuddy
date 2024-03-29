# Import used libraries
from utils.definitions import weatherapicodes as codelist
import requests

# Set the keyword
keywords = ['weather']


def cmdfunction(spktext: str):
    # Defining the API url and using the private API key
    weather_url = 'http://api.weatherapi.com/v1/current.json'
    api_key = 'c88d5fcfad014b909ae94202231506'
    
    try:
        params = {
            'key': api_key,
            'q': 'auto:ip',
            'lang': 'de'
        }

        # Getting the data from the API and reading the .json file recieved
        response = requests.get(weather_url, params=params)
        response.raise_for_status()
        
        weather_data = response.json()
        
        location = weather_data['location']['name']
        country = weather_data['location']['country']
        temp_c = weather_data['current']['temp_c']
        condition_code = weather_data['current']['condition']['code']
        is_day = weather_data['current']['is_day']


        condition = codelist[str(condition_code)]['day']

        if (is_day == 0):
            condition = codelist[str(condition_code)]['night']


        temphc = 'warm'

        if (temp_c < 10):
            temphc = 'kalt'
        
        if (str(temp_c).index(".")):
            temp_c = str(temp_c).replace("."," komma ")


        output = "Hier ist das aktuelle Wetter in " + str(location) + ", " + str(country) + ". " + "Es ist " + str(temp_c) + " Grad Celsius " + str(temphc) + " und " + str(condition) + "."
        #print(output)

        return {
            "error": "",
            "value": output
        }
    
    except:
        return {
            "error": "weather-1",
            "value": ""
        }
        
    #except (requests.RequestException, KeyError) as e:
        #print('Error:', str(e))

#cmdfunction()