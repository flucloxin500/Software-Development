from flask import Flask, redirect, url_for
from flask_login import LoginManager
from models import db, Users

# Import blueprints for each feature
from index import index
from login import login
from logout import logout
from register import register
from home import home
from dashboard import dashboard
from about import about
from checkout import checkout
from contact import contact
from iiuc import iiuc
from iiuc_kid import iiuc_kid
from iiuc_men import iiuc_men
from iiuc_women import iiuc_women
from reviews import reviews

app = Flask(__name__, static_folder='../backend/static')
app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database.db'

login_manager = LoginManager()
login_manager.init_app(app)
db.init_app(app)
app.app_context().push()

# Register blueprints for each feature
app.register_blueprint(index)
app.register_blueprint(login)
app.register_blueprint(logout)
app.register_blueprint(register)
app.register_blueprint(home)
app.register_blueprint(dashboard)
app.register_blueprint(about)
app.register_blueprint(checkout)
app.register_blueprint(contact)
app.register_blueprint(iiuc)
app.register_blueprint(iiuc_kid)
app.register_blueprint(iiuc_men)
app.register_blueprint(iiuc_women)
app.register_blueprint(reviews)

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

@app.route('/')
def root():
    return redirect(url_for('home.show'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
