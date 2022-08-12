from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
            {
                'author': {'username': 'Jhon'},
                'body': 'Beautiful day in Portland!'
                },
            {
                'author': {'username': 'Susan'},
                'body': 'The Avengers movie is so cool!'
                }
            ]
    return render_template('index.html', title='Home', user=user, posts=posts)

