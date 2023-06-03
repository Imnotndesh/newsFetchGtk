import json,requests
## Api key from website
appKey = 'ab1a600bcfe741fdadad464a7698e0bf'

def apiFetch(usrTopic):
    apiResponse = requests.get(f'https://newsapi.org/v2/everything?q={usrTopic}&apiKey={appKey}').text
    global newsCollection
    newsCollection = json.loads(apiResponse)
    return newsCollection
