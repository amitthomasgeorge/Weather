from django.shortcuts import render
import json
import urllib.request
import math
# Create your views here.

def index(request):
    if(request.method=='POST'):
        city=request.POST['city']
        res=urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=26f1fad232eaf2df094a2c55857df48d').read()
        jsondata=json.loads(res)
        data={
            'country_code':str(jsondata['sys']['country']),
            'coordinate':str(jsondata['coord']['lon'])+' '+str(jsondata['coord']['lat']),
            'temp':str(round(float(jsondata['main']['temp'])-273.15,2)),
            'pressure':str(jsondata['main']['pressure']),
            'humidity':str(jsondata['main']['humidity']),
        }
    else:
        city=''
        data={}
    return render(request,'index.html',{'city':city,'data':data})