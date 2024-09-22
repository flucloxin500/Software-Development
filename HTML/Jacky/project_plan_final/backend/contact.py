from flask import Blueprint, render_template

# Create a Blueprint object for the "contact" feature
contact = Blueprint('contact', __name__, template_folder='../frontend')

# Define a route for the "Contact" page
@contact.route('/contact', methods=['GET'])
def show_contact():
    return render_template('contact.html')
