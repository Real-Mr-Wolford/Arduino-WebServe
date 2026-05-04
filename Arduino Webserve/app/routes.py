from flask import Blueprint, render_template, request, url_for, redirect
from .models import User
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
   
    all_users = User.query.all() 
    return render_template('index.html', messages=all_users)

@main.route('/game')
def game():
    return render_template('game.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        message = request.form.get('message')

       
        new_user = User(name=name, message=message)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('main.index'))

   
    return render_template('index.html')
