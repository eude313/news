from flask import render_template, request, url_for, redirect
from . import main
from ..request import get_sources, get_articles
# from ..models import Source

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/sources')
def index():
    general = get_sources()
    return render_template('index.html', message = general)

@main.route('/about/<source_id>')
def about(source_id):   
    # get_id = get_sources()
    articles = get_articles(source_id)
    return render_template('about.html', articles = articles)