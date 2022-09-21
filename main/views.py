from django.shortcuts import render
from bs4 import BeautifulSoup as bs
import requests

# Create your views here.
def Home(request):
      return render(request,"index.html")

def Search(request):
      if request.method=="POST":
            search=request.POST.get("search")
            search.replace(" ","")
            url='https://www.ask.com/web?q='+search
            response=requests.get(url)
            soup=bs(response.text,"lxml")
            result_listing=soup.find_all('div',{'class':'PartialSearchResults-item'})
            final_result=[]
            for result in result_listing:
                  result_title = result.find(class_='PartialSearchResults-item-title').text
                  result_url = result.find('a').get('href')
                  result_desc = result.find(class_='PartialSearchResults-item-abstract').text
                  final_result.append((result_title, result_url, result_desc))
            context = {
            'final_result': final_result
            }

            return render(request,"search.html",context)

      return render(request, 'search.html')


            
