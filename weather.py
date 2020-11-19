import requests, json
# base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
CITY = input("Please Enter the city name:")
print("Locating city:",CITY,"....\n\n")
#api key
API_KEY = "05cc201d696d928ab9b1aa615fbab3cf"
# upadting the URL
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
# HTTP request
response = requests.get(URL)
# checking the status code of the request
if response.status_code == 200:
   # getting data in the json format
   data = response.json()
   # getting the main dict block
   main = data['main']
   temperature = main['temp']
   humidity = main['humidity']
   pressure = main['pressure']
   # weather report
   report = data['weather']
#python version 3.6 or above is required for these below statements.
   print(f"{CITY:-^30}")
   print(f"Temperature: {temperature}")
   print(f"Humidity: {humidity}")
   print(f"Pressure: {pressure}")
   print(f"Weather Report: {report[0]['description']}")
else:
   # showing the error message
   print("Error in the HTTP request or invalid city name:",CITY)
