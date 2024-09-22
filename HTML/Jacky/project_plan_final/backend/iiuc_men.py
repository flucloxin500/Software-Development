from flask import Blueprint, render_template

# Create a Blueprint object for the "iiuc_men" feature
iiuc_men = Blueprint('iiuc_men', __name__, template_folder='../frontend')

# Define a route for the "IIUC Men" page
@iiuc_men.route('/iiuc.men', methods=['GET'])
def show_iiuc_men():
    return render_template('iiuc_men.html')
