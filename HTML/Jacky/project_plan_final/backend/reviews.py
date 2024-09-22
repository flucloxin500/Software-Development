from flask import Blueprint, render_template

# Create a Blueprint object for the "reviews" feature
reviews = Blueprint('reviews', __name__, template_folder='../frontend')

# Define a route for the "Reviews" page
@reviews.route('/reviews', methods=['GET'])
def show_reviews():
    return render_template('reviews.html')
