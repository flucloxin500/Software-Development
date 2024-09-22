from flask import Blueprint, render_template

# Create a Blueprint object for the "about" feature
about = Blueprint('about', __name__, template_folder='../frontend')

# Define a route for the "About" page
@about.route('/about', methods=['GET'])
def show_about():
    return render_template('about.html')
