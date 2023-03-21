from django.shortcuts import render
import requests


def home(request):
    if 'city' in request.POST:
        city = request.POST.get('city')
        
    else:
        city = 'Bahia'

        
    appid = '1d2b75c3768a5b8a6506e99e9069ab68'
    api_url = 'http://api.openweathermap.org/data/2.5/weather' 
    params = {'q':city, 'appid':appid,  'units':'metric'}
    r = requests.get(url=api_url, params=params)
    res =  r.json()

    data = {
        'city':city,
        'weather_description': res['weather'][0]['description'],
        'weather_temperature': res['main']['temp'],
        'weather_pressure': res['main']['pressure'],
        'weather_humidity': res['main']['temp'],
        'weather_icon': res['weather'][0]['icon']
    }

    
        
        

  
    
    return render(request, 'base/home.html', {'data':data})
