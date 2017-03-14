from flask import render_template, flash, redirect, session, url_for, request, g
# from flask_login import login_user, logout_user, current_user, login_required
from app import app #, db, lm
from functools import wraps

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out.')
    return redirect(url_for('index'))

@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html')

@app.route('/about')
@login_required
def about():
    return render_template("about.html")

@app.route('/documents')
@login_required
def documents():
    return render_template("documents.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'uca' or request.form['password'] != 'uca':
            error = 'Wrong username or password. Please try again.'
        else:
            session['logged_in'] = True
            flash('You were logged in.')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)
