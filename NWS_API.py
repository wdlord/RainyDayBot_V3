import requests
import datetime

base_url = 'https://api.weather.gov/'

Locations = {
    'Escondido': (33.1192, -117.0864),
    'Tempe': (33.4255, -111.9400),
}

Weekdays = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday',
}


# returns the URL to query based on location coordinates
def get_forecast_url(coordinates):
    GET = f'points/{coordinates[0]},{coordinates[1]}'
    json_response = requests.get(base_url + GET).json()
    return json_response['properties']['forecast']


# gets the name of the weekday for tomorrow's date
def get_tomorrow():
    key = (datetime.date.today() + datetime.timedelta(days=1)).weekday()    # returns 0 - 6 (monday - sunday)
    return Weekdays[key]


# gets the forecast for tomorrow
def get_forecast(URL):
    json_response = requests.get(URL).json()
    periods = json_response['properties']['periods']

    for p in periods:
        if p['name'] == get_tomorrow():
            return p


# returns True if the Detailed Forecast predicts rain, else False
def will_rain(forecast):
    rain_keywords = ['rain', 'shower']
    return any([word in forecast for word in rain_keywords])


# the main call of this module
def check_rain():
    url = get_forecast_url(Locations['Tempe'])
    forecast = get_forecast(url)

    return forecast['detailedForecast']
