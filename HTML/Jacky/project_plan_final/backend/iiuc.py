from flask import Blueprint, render_template

# Create a Blueprint object for the "iiuc" feature
iiuc = Blueprint('iiuc', __name__, template_folder='../frontend')

# Define a route for the "IIUC" page
@iiuc.route('/iiuc', methods=['GET'])
def show_iiuc():
    return render_template('iiuc.html')
