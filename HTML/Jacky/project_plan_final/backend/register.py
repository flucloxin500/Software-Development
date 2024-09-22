from flask import Blueprint, url_for, render_template, redirect, request, flash
from flask_login import LoginManager
from werkzeug.security import generate_password_hash
from sqlalchemy.exc import IntegrityError  

from models import db, Users

register = Blueprint('register', __name__, template_folder='../frontend')
login_manager = LoginManager()
login_manager.init_app(register)

@register.route('/register', methods=['GET', 'POST'])
def show():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        fname = request.form['first_name']
        lname = request.form['last_name']

        if username and email and password and confirm_password:
            if password == confirm_password:
                hashed_password = generate_password_hash(
                    password, method='sha256')
                try:
                    new_user = Users(
                        username=username,
                        email=email,
                        fname=fname,
                        lname=lname,
                        password=hashed_password,
                    )

                    db.session.add(new_user)
                    db.session.commit()
                    flash('Account created successfully!', 'success')
                    return redirect(url_for('login.show'))
                except IntegrityError:  
                    db.session.rollback()  
                    flash('User with this email already exists!', 'error')
                    return redirect(url_for('register.show'))
            else:
                flash('Passwords do not match!', 'error')
                return redirect(url_for('register.show'))
        else:
            flash('Missing fields!', 'error')
            return redirect(url_for('register.show'))
    else:
        return render_template('register.html')
