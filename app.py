from flask import Flask, render_template, request, jsonify
from flask_migrate import Migrate
from flask_cors import CORS
from models import db, User

app = Flask(__name__)

app.url_map.strict_slashes=False
app.config['DEBUG']=True
app.config['ENV']='development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///database.db'

db.init_app(app)
Migrate(app,db) #db init, db migrate, db upgrade
CORS(app)


@app.route("/", methods=['GET'])
def main():
    return render_template('index.html')


if __name__=='__main__':
    app.run() 