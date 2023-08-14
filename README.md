# RainAlertNotifier
RainAlertNotifier is a Python script that utilizes the OpenWeatherMap API and the Twilio API to provide SMS notifications about impending rain in a specific location.
## Overview
RainAlertNotifier is a simple and practical tool designed to help you stay informed about potential rain in your vicinity. By interfacing with the OpenWeatherMap API, the script retrieves hourly weather data, and through the Twilio API, it sends SMS notifications when rain is anticipated. This allows you to adjust your plans and take appropriate precautions based on upcoming weather conditions.
## Features
* Fetches up-to-date weather data using the OpenWeatherMap API.
* Sends SMS notifications via the Twilio API when rain is predicted.
* Customizable location settings using latitude and longitude coordinates.
## How It Works
1. OpenWeatherMap API Integration: RainAlertNotifier interacts with the OpenWeatherMap API to collect detailed weather forecasts for a specified location. The API provides hourly weather data, which the script analyzes to determine if rain is expected.

2. Twilio SMS Notifications: When the script detects potential rain in the forecast, it leverages the Twilio API to send an SMS notification to a designated phone number. This notification serves as a timely reminder to prepare for rainy weather.

3. Deploy and Schedule: To ensure you receive rain alerts consistently, you can deploy and schedule the RainAlertNotifier script to run automatically on a server. Services like pythonanywhere provide an excellent platform for this purpose. By configuring a scheduled task on pythonanywhere, the script will run at specified intervals (e.g., every few hours), continuously keeping you updated on weather conditions.
## Configuration
* OpenWeatherMap API: Obtain an API key by signing up at OpenWeatherMap, and replace API_KEY in main.py.

* Twilio API: Sign up at Twilio to acquire your ACCOUNT_SID, AUTH_TOKEN and MY_NUM. Replace these values in main.py.

* Location: Determine the latitude and longitude coordinates of your desired location using resources like 'latlong.net'. Update the my_lat and my_lon values in main.py.
## Credits
RainAlertNotifier was developed by Shahaf Yagoda
