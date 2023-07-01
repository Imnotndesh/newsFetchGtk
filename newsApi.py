import json,requests
import time
## Api key from website
appKey = 'ab1a600bcfe741fdadad464a7698e0bf'

# def headlineFetch():
#     headResponse = requests.get(f'https://newsapi.org/v2/top-headlines?country=us&apiKey={appKey}').text
#     global headCollection
#     headCollection = json.loads(headResponse)
#     print(headCollection)
#     return headCollection

def searchFetch(usrTopic):
    searchResponse = requests.get(f'https://newsapi.org/v2/everything?q={usrTopic}&apiKey={appKey}').text
    global newsCollection
    newsCollection = json.loads(searchResponse)
    return newsCollection
    time.sleep(20)
