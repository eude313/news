from flask import render_template
from app.request import get_articles, get_news
from . import main


@main.route('/')
def home():
    return render_template('home.html')

# @main.route('/sources', methods = ['GET'])
# def index():
#     '''
#     view root page that returns the index page and its data
#     '''
#     title = "Home|newsrun"
#     all_news = get_news('sports')
#     general_news = get_news('general')
#     tech_news = get_news('technology')
#     bus_news = get_news('business')
#     ent_news = get_news('entertainment')

#     # print(all_news)

#     return render_template('index.html', title=title, sports=all_news, general=general_news, technology=tech_news,
#     business=bus_news, entertainment=ent_news)


# @main.route('/about/<source_id>', methods = ['GET'])
# def about(source_id):   
#     # get_id = get_sources()
#     articles = get_articles(source_id)
#     return render_template('about.html', articles = articles)
