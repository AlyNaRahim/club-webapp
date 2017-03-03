from flask import render_template, flash, redirect, session, url_for, request, g
# from flask_login import login_user, logout_user, current_user, login_required
from app import app #, db, lm
# from .forms import LoginForm
# from .models import User


# @lm.user_loader
# def load_user(id):
#     return User.query.get(int(id))


# @app.before_request
# def before_request():
#     g.user = current_user


@app.route('/')
@app.route('/index')
# @login_required
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/documents')
def documents():
    return render_template("documents.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Wrong username or password. Please try again.'
        else:
            return redirect(url_for('index'))
    return render_template('login.html', error=error)
# def login():
#     if g.user is not None and g.user.is_authenticated:
#         return redirect(url_for('/index'))
#     form = LoginForm()
#     if form.validate_on_submit():
#         session['remember_me'] = form.remember_me.data
#         return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
#     return render_template('login.html')



# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('index'))
