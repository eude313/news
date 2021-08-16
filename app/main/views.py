from flask import render_template
from app.request import get_articles, get_news
from . import main

# /sources
@main.route('/')
def home():
    return render_template('home.html')
 
@main.route('/sources')
def index():
    
    title = "Home|newsrun"
    all_news = get_news()
    general_news = get_news()
    tech_news = get_news()
    bis_news = get_news()
    ent_news = get_news()

    # print("get_news")

    return render_template('index.html', title=title, sports=all_news, general=general_news, technology=tech_news, business=bis_news, entertainment=ent_news)

# @main.route('/source/<int:id>')
# def news(id):
    
#     news = get_news(id)

#     return render_template('index.html', news=news)

# @main.route('/about/<source_id>', methods = ['GET'])
# def about(source_id):   
#     # get_id = get_sources()
#     articles = get_articles(source_id)
#     return render_template('about.html', articles = articles)
