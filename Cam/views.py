import requests
from django.shortcuts import render
from bs4 import BeautifulSoup

BASE_KRAIGSLIST_URL = 'https://kenya.craigslist.org/search/hhh?query={}'



def home(request):
    return render(request,template_name='base.html')

def new_search(request):
    search = request.POST.get('search')
    final_url = BASE_KRAIGSLIST_URL
    response = requests.get(final_url)
    data =  response.text
    print(data)

    return render(request,template_name='Cam/new_search.html')