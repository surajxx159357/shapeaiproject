
import requests
#import os
from datetime import datetime
x=open('apitest.py.txt','w')   # [ using this redirect storing we can store output into .txt file ]

api_key = '87d845b0b6cf29baa1a73cc34b067a95'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time),file=x)
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city),file=x)
print ("Current weather desc  :",weather_desc,file=x)
print ("Current Humidity      :",hmdt, '%',file=x)
print ("Current wind speed    :",wind_spd ,'kmph',file=x)


































































###[ leap year using for loop ]
# def leap_year(year):
#     if(year%4==0 and (year%100 or year%400)):
#         print("leap year")
#     else:
#         print("not a leap_year")
# {
#     leap_year(2020)
# }

###[ function with 2nd method ]
# def method(narsimha,villain):
#     return '{},god kills ,{}'.format(narsimha,villain)
# {
#     print(method("vishnu","rakshas"))
# }