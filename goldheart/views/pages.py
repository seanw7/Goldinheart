from flask import Blueprint, render_template

page = Blueprint('page', __name__, template_folder='templates')


@page.route('/')
def home():
    return render_template('home.html')

@page.route('/terms')
def terms():
    return render_template('terms.html')

@page.route('/songs')
def songs():
    return render_template('songs.html')

@page.route('/about')
def about():
    return render_template('about.html')

@page.route('/contact')
def contact():
    return render_template('contact.html')

@page.route('/media')
def media():
    return render_template('media.html')

@page.route('/calendar')
def calendar():
    return render_template('calendar.html')
