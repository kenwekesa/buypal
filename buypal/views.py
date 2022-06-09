
#from accounts.models import Userlogin
#from django.views.generic import CreateView

from django.contrib.auth.decorators import login_required

from django.shortcuts import  render, redirect

from django.contrib import messages


from django.shortcuts import render

from accounts.models import Profile

from django.shortcuts import render
from django.contrib.auth import login, authenticate
from accounts.forms import SignUpForm

from django.contrib.auth.forms import AuthenticationForm #add this

from django.shortcuts import render, redirect

#for news 
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from accounts.models import News

from .serializers import NewsSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

from bs4 import BeautifulSoup as BSoup
from accounts.models import Headline
import requests

from random import randrange




#constants
ALPHA_VINTAGE_API_KEY =  'RRKMAMVFQD2U5T6Y'

CLOUD_FPM_API_KEY ='27fbd95a470a84bdbc9b4102a4818bd6'


# Create your views here.






class NewsApiView(APIView):

    def get(self, request):
        news_qs = News.objects.all()
        serializer = NewsSerializer(news_qs, many=True)
        return Response(serializer.data)


#@login_required
def home(request):
    #context = {'posts': Post.objects.all()}
    session = requests.Session()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.googlebot.com/bot.html)"} 
    url = "https://www.coingecko.com/en/crypto-gainers-losers"
    #url="https://coinmarketcap.com/gainers-losers/"
    headers = requests.utils.default_headers()
    headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
    })
    content = requests.get(url, verify=False).content
    soup = BSoup(content, "html.parser")

    data_table = soup.find_all('div', {"class":"coingecko-table"})

    tables_dic = {}

    for table in data_table:
        rows = table.find('table').find('tbody').find_all('tr')
        table_list = []
        for r in rows:
            rows_dic ={}
            td=r.find_all('td')
            rows_dic["coin"] = td[0].find('div').find_all('div')[1].find_all('span')[0].contents[0]
            rows_dic["volume"]  = td[1].find('a').find('span').contents[0]
            rows_dic["price"] = td[2].find('a').find('span').contents[0]
            rows_dic["percentage"]  = td[3].find('span').contents[0]

            table_list.append(rows_dic)

        tables_dic['table'+str(data_table.index(table))] = table_list
    print(tables_dic)

          
        
    url = ('https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=1ea40f94110644f493df2b9991d8ba39')

    news_json = requests.get(url) 
    

    context = {
        'articles': news_json.json()['articles'] ,
        'gainers_loosers': tables_dic,
    }
    
    
    
        
    return render(request, 'buypal/index.html',context)


def page_details_view(request):
    session = requests.Session()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.googlebot.com/bot.html)"} 
    url = "https://www.coingecko.com/en/crypto-gainers-losers"
    #url="https://coinmarketcap.com/gainers-losers/"
    headers = requests.utils.default_headers()
    headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
    })
    content = requests.get(url, verify=False).content
    soup = BSoup(content, "html.parser")

    data_table = soup.find_all('div', {"class":"coingecko-table"})

    tables_dic = {}

    for table in data_table:
        rows = table.find('table').find('tbody').find_all('tr')
        table_list = []
        for r in rows:
            rows_dic ={}
            td=r.find_all('td')
            rows_dic["coin"] = td[0].find('div').find_all('div')[1].find_all('span')[0].contents[0]
            rows_dic["volume"]  = td[1].find('a').find('span').contents[0]
            rows_dic["price"] = td[2].find('a').find('span').contents[0]
            rows_dic["percentage"]  = td[3].find('span').contents[0]

            table_list.append(rows_dic)

        tables_dic['table'+str(data_table.index(table))] = table_list
    print(tables_dic)

          
        
   

    news_json = requests.get(url) 
    

    context = {
        
        'gainers_loosers': tables_dic,
    }
    return render(request, 'buypal/page_details.html',context)

    
def news_view(request):
    #headlines = Headline.objects.all()[::-1]
    
    url = ('https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=1ea40f94110644f493df2b9991d8ba39')

    news_json = requests.get(url) 
    

    context = {
        'articles': news_json.json()['articles'] ,
    }

    return render(request, 'buypal/news.html',context)


def get_news_view(request):
    #headlines = Headline.objects.all()[::-1]
    
    url = ('https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=1ea40f94110644f493df2b9991d8ba39')

    news_json = requests.get(url) 
    
    
    context = {
        'article': news_json.json()['articles'][randrange(len(news_json.json()['articles']))] ,
    }

    return render(request, 'buypal/news_card.html',context)


def view_news_view(request):
    #headlines = Headline.objects.all()[::-1]
    
    url = ('https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=1ea40f94110644f493df2b9991d8ba39')

    news_json = requests.get(url) 
   
    

    context = {
        'article': news_json.json()['articles'][0] ,
    }

    return render(request, 'buypal/readnews.html',context)

def stockexchange_view(request):
    #context = {'posts': Post.objects.all()}
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=SBIN.BSE&outputsize=full&apikey="+ALPHA_VINTAGE_API_KEY
    #url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SBIN.BSE&interval=5min&apikey='+ALPHA_VINTAGE_API_KEY
    #url = 'https://fmpcloud.io/api/v3/historical-price-full/AAPL?serietype=line&apikey=27fbd95a470a84bdbc9b4102a4818bd6'

    r = requests.get(url)
    data = r.json()
    
    data_list = []
    
   
    for i in data['Time Series (Daily)']:
        if i >= '2022-01-01':
            myDict={}
            myDict["timeline"] = i
            myDict["data"] = data['Time Series (Daily)'][i]
            data_list.append(myDict)
        else:
            break
    
    context = { 
        "datas": data_list

     } 
        
    return render(request, 'buypal/stockexchange.html',context)


def login_view(request):
    #context = {'posts': Post.objects.all()}
  
    if request.method == "POST":
	    form = AuthenticationForm(request, data=request.POST)
	    if form.is_valid():
		    username = form.cleaned_data.get('username')
		    password = form.cleaned_data.get('password')
		    user = authenticate(username=username, password=password)
		    if user is not None:
			    login(request, user)
			    return redirect("user-home")
		    else:
			    messages.error(request,"Invalid username or password.")
	    else:
		    messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="forms/login.html", context={"login_form":form})



def signup_view(request):
    #context = {'posts': Post.objects.all()}
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            full_name = form.cleaned_data.get('full_name')
            email = form.cleaned_data.get('email')

            Profile.objects.create(user=user, full_name = full_name, email=email)

            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            

            messages.info(request, f"You are signed up successfully, login to proceed.")    
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'forms/signup.html', {'form': form})
    #return render(request, 'forms/signup.html')#,context)
    
@login_required
def userdashboard_view(request):
    return render(request, 'buypal/userdashboard.html')

@login_required
def edit_profile_view(request):
    #context = {'posts': Post.objects.all()}
    if request.method == 'POST':
        form = SignUpForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            full_name = form.cleaned_data.get('full_name')
            email = form.cleaned_data.get('email')

            Profile.objects.create(user=user, full_name = full_name, email=email)

            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            

            messages.info(request, f"You are signed up successfully, login to proceed.")    
            return redirect('login')
    else:
        form = SignUpForm(instance=request.user)
    return render(request, 'forms/signup.html', {'form': form})
    #return render(request, 'forms/signup.html')#,context)




def scrape(request):
  session = requests.Session()
  session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.googlebot.com/bot.html)"} 
  url = "https://nation.africa/kenya/news"
  headers = requests.utils.default_headers()
  headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
  })
  content = requests.get(url, verify=False).content
  soup = BSoup(content, "html.parser")

  News = soup.find_all('ol', {"class":"article-collection"})
  for artcile in News:
    main = artcile.find_all('li')
    for ar in main:
        af= ar.find('a')
        title = af.find('h3').contents
        print("\n\n-----------------------------------------------------------------------------")
        print(af['href'])
        print(title)
        print("\n\n-----------------------------------------------------------------------------")
    
        
        new_headline = Headline()
        new_headline.title = title
        new_headline.url = af['href']
        new_headline.image = "None"
        new_headline.save()
  print(News)
  return redirect("../")


def scrape_gainers_loosers(request):
  session = requests.Session()
  session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.googlebot.com/bot.html)"} 
  url = "https://www.coingecko.com/en/crypto-gainers-losers"
  headers = requests.utils.default_headers()
  headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
  })
  content = requests.get(url, verify=False).content
  soup = BSoup(content, "html.parser")

  News = soup.find_all('ol', {"class":"article-collection"})
  for artcile in News:
    main = artcile.find_all('li')
    for ar in main:
        af= ar.find('a')
        title = af.find('h3').contents
        print("\n\n-----------------------------------------------------------------------------")
        print(af['href'])
        print(title)
        print("\n\n-----------------------------------------------------------------------------")
    
        
        new_headline = Headline()
        new_headline.title = title
        new_headline.url = af['href']
        new_headline.image = "None"
        new_headline.save()
  print(News)
  return redirect("../")