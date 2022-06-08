from flask import Flask, render_template, request, jsonify
from flask_migrate import Migrate
from flask_cors import CORS
from models import db, User, Personaje, Planeta, Nave

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

@app.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    users = list(map(lambda user: user.serialize(), users))

    return jsonify(users), 200

@app.route('/api/users/<int:id>', methods=['GET'])
def get_user(id):
    users = User.query.filter_by(id = iduser)
    users = list(map(lambda user: user.serialize(), users))

    return jsonify(users), 200

@app.route('/api/users', methods=['POST'])
def post_users():

    name = request.json.get('name')
    last_name = request.json.get('last_name')
    nameuser = request.json.get('nameuser')
    password = request.json.get('password')
    emailuser = request.json.get('emailuser')

    user = User()
    user.name = name
    user.last_name = last_name
    user.nameuser = nameuser
    user.password = password
    user.emailuser = emailuser
    user.save()

    return jsonify(user.serialize()), 201


@app.route('/api/users/<int:id>', methods=['PUT'])
def put_users(id):

    name = request.json.get('name')
    last_name = request.json.get('last_name')
    nameuser = request.json.get('nameuser')
    password = request.json.get('password')
    emailuser = request.json.get('emailuser')

    user = User.query.get(id)
    user.name = name
    user.last_name = last_name
    user.nameuser = nameuser
    user.password = password
    user.emailuser = emailuser
    user.update()
    
    return jsonify(user.serialize()), 200


@app.route('/api/users/<int:id>', methods=['DELETE'])
def delete_users(id):

    user = User.query.get(id)
    user.delete()
    
    return jsonify({ "status": True, "msg": "Usuario elminado"}), 200

if __name__=='__main__':
    app.run()  