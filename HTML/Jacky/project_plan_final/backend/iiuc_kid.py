from flask import Blueprint, render_template

# Create a Blueprint object for the "iiuc_kid" feature
iiuc_kid = Blueprint('iiuc_kid', __name__, template_folder='../frontend')

# Define a route for the "IIUC Kids" page
@iiuc_kid.route('/iiuc.kid', methods=['GET'])
def show_iiuc_kid():
    return render_template('iiuc_kid.html')
