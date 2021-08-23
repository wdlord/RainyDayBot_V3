# RainyDayBot_V3
An even newer implementation of my script that notifies me if it will rain tomorrow.

This project communicates with the National Weather Service's API.

This version is super simple for others to use, but if you do not use T-Mobile as your phone carrier you may have to figure out how to alter the Send_SMS.py file for your phone number. Just add your coordinates the the Locations dictionary in NWS_API.py, pass that location to get_forecast_url(location) in check_rain(), and set the program running.
