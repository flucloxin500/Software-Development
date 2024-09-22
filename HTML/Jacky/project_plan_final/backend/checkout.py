from flask import Blueprint, render_template

# Create a Blueprint object for the "checkout" feature
checkout = Blueprint('checkout', __name__, template_folder='../frontend')

# Define a route for the "Checkout" page
@checkout.route('/checkout', methods=['GET'])
def show_checkout():
    return render_template('checkout.html')
