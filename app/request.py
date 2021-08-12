import urllib.request,json
from .models import  News, Articles

# Getting api key
api_key = None
# Getting the news base url
base_url = None
# Getting the articles_url base url
articles_url = None

def configure_request(app):
    global api_key,base_url,articles_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_SOURCE_URL']
    articles_url = app.config['ARTICLES_BASE_URL ']
    

def get_news(cake):
    '''function that gets the json response to the url request
    '''
    get_news_url = base_url.format(cake, api_key)
    print(get_news_url)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)

    return news_results

def process_results(news_list):

    news_results = []
    for news_item in news_list:
        name = news_item.get('name')
        url = news_item.get('url')
        country = news_item.get('country')
        description = news_item.get('description')
        category = news_item.get('category')
        id = news_item.get('id')

        news_object = News(name, url, description, country, category, id)
        news_results.append(news_object)

    return news_results