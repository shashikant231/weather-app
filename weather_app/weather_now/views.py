from django.shortcuts import render
import requests
from .models import City 


# Create your views here.
def index(request):
  

    
    cities = City.objects.all()
    weather_data = []

    for city in cities:
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=476c5d7313941b7b56b3cb5655fa2341'
        r = requests.get(url.format(city)).json()
        city_weather = {
        'city' : city.name ,
        'temperature' : r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon' : r['weather'][0]['icon'],
        }
        
        weather_data.append(city_weather)
    
    context = {'weather_data' : weather_data}
        
    return render(request,'weather_now/home.html', context)
