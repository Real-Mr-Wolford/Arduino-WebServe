from flask import Blueprint, render_template, request, url_for, redirect
from .models import User
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    # Fetch all users from the database to show on the home page
    all_users = User.query.all() 
    return render_template('index.html', messages=all_users)

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        message = request.form.get('message')

        # Ensure the column names (name, message) match your models.py exactly
        new_user = User(name=name, message=message)
        db.session.add(new_user)
        db.session.commit()

        # Redirect to the index page after successful registration
        return redirect(url_for('main.index'))

    # If it's a GET request, just show the registration form
    return render_template('register.html')