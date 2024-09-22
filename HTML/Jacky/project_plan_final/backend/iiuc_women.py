from flask import Blueprint, render_template

# Create a Blueprint object for the "iiuc_women" feature
iiuc_women = Blueprint('iiuc_women', __name__, template_folder='../frontend')

# Define a route for the "IIUC Women" page
@iiuc_women.route('/iiuc.women', methods=['GET'])
def show_iiuc_women():
    return render_template('iiuc_women.html')
