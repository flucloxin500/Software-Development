from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

dashboard = Blueprint('dashboard', __name__, template_folder='../frontend')

@dashboard.route('/dashboard', methods=['GET'])
@login_required
def show():
    return render_template('dashboard.html')

@dashboard.route('/dashboard/redirect', methods=['GET'])  # Change the URL to avoid conflicts
def redirect_to_dashboard():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.show'))
    else:
        return redirect(url_for('login.show'))
