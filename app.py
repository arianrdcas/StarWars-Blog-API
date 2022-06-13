from flask import Flask, render_template, request, jsonify
from flask_migrate import Migrate
from flask_cors import CORS
from models import db, User, Favorite, Personaje, Planeta, Nave

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


"""----RUTAS DE USUARIOS-----"""

@app.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    users = list(map(lambda user: user.serialize(), users))

    return jsonify(users), 200

@app.route('/api/users/<int:iduser>', methods=['GET'])
def get_user(iduser):
    users = User.query.filter_by(iduser = iduser)
    users = list(map(lambda user: user.serialize_whit_favorite(), users))

    if not iduser: return jsonify ({ "status": False, "msg": "El usuario no existe"}), 404 

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


"""----RUTAS DE PERSONAJES-----"""

@app.route('/api/personajes', methods=['GET'])
def get_personajes():
    personajes = Personaje.query.all()
    personajes = list(map(lambda personaje: personaje.serialize(), personajes))

    return jsonify(personajes), 200


@app.route('/api/personajes/<int:idpersonaje>', methods=['GET'])
def get_personaje(idpersonaje):
    personajes = Personaje.query.filter_by(idpersonaje = idpersonaje)
    personajes = list(map(lambda personaje: personaje.serialize(), personajes))

    if not idpersonaje: return jsonify ({ "status": False, "msg": "El usuario no existe"}), 404 

    return jsonify(personajes), 200


@app.route('/api/personajes/', methods=['POST'])
def post_personajes():

    name = request.json.get('name')
    height = request.json.get('height')
    mass = request.json.get('mass')
    hair_color = request.json.get('hair_color')
    skin_color = request.json.get('skin_color')
    eye_color = request.json.get('eye_color')
    birth_year = request.json.get('birth_year')
    gender = request.json.get('gender')

    personaje = Personaje()
    personaje.name = name
    personaje.height = height
    personaje.mass = mass
    personaje.hair_color = hair_color
    personaje.skin_color = skin_color
    personaje.eye_color = eye_color
    personaje.birth_year = birth_year
    personaje.gender = gender
    
    personaje.save()
 
    return jsonify(personaje.serialize()), 201


@app.route('/api/personajes/<int:idpersonaje>', methods=['PUT'])
def put_personaje(idpersonaje):

    name = request.json.get('name')
    height = request.json.get('height')
    mass = request.json.get('mass')
    hair_color = request.json.get('hair_color')
    skin_color = request.json.get('skin_color')
    eye_color = request.json.get('eye_color')
    birth_year = request.json.get('birth_year')
    gender = request.json.get('gender')

    personaje = Personaje.query.get(idpersonaje)
    personaje.name = name
    personaje.height = height
    personaje.mass = mass
    personaje.hair_color = hair_color
    personaje.skin_color = skin_color
    personaje.eye_color = eye_color
    personaje.birth_year = birth_year
    personaje.gender = gender
    
    personaje.update()
 
    return jsonify(personaje.serialize()), 201

@app.route('/api/personajes/<int:idpersonaje>', methods=['DELETE'])
def delete_personajes(idpersonaje):

    personaje = Personaje.query.get(idpersonaje)
    personaje.delete()
    
    return jsonify({ "status": True, "msg": "Personaje elminado"}), 200



"""----RUTAS DE PLANETAS-----"""

@app.route('/api/planetas', methods=['GET'])
def get_planetasall():
    planetas = Planeta.query.all()
    planetas = list(map(lambda planeta: planeta.serialize(), planetas))

    return jsonify(planetas), 200


@app.route('/api/planetas/<int:idplaneta>', methods=['GET'])
def get_planetas(idplaneta):
    planetas = Planeta.query.filter_by(idplaneta = idplaneta)
    planetas = list(map(lambda planeta: planeta.serialize(), planetas))

    return jsonify(planetas), 200


@app.route('/api/planetas', methods=['POST'])
def post_planetas():

    name = request.json.get('name')
    diameter = request.json.get('diameter')
    rotation_period = request.json.get('rotation_period')
    orbital_period = request.json.get('orbital_period')
    gravity = request.json.get('gravity')
    population = request.json.get('population')
    climate = request.json.get('climate')

    planeta = Planeta()
    planeta.name = name
    planeta.diameter = diameter
    planeta.rotation_period = rotation_period
    planeta.orbital_period = orbital_period
    planeta.gravity = gravity
    planeta.population = population
    planeta.climate = climate
    
    planeta.save()
 
    return jsonify(planeta.serialize()), 201


@app.route('/api/planetas/<int:idplaneta>', methods=['PUT'])
def put_planeta(idplaneta):

    name = request.json.get('name')
    diameter = request.json.get('diameter')
    rotation_period = request.json.get('rotation_period')
    orbital_period = request.json.get('orbital_period')
    gravity = request.json.get('gravity')
    population = request.json.get('population')
    climate = request.json.get('climate')
    
    planeta = Planeta.query.get(idplaneta)
    planeta.name = name
    planeta.diameter = diameter
    planeta.rotation_period = rotation_period
    planeta.orbital_period = orbital_period
    planeta.gravity = gravity
    planeta.population = population
    planeta.climate = climate
    
    planeta.update()
 
    return jsonify(planeta.serialize()), 201



@app.route('/api/planetas/<int:idplaneta>', methods=['DELETE'])
def delete_planetas(idplaneta):

    planeta = Planeta.query.get(idplaneta)
    planeta.delete()
    
    return jsonify({ "status": True, "msg": "Planeta elminado"}), 200


"""----RUTAS DE NAVES-----"""

@app.route('/api/naves', methods=['GET'])
def get_naves():
    naves = Nave.query.all()
    naves = list(map(lambda nave: nave.serialize(), naves))

    return jsonify(naves), 200


@app.route('/api/naves/<int:idnave>', methods=['GET'])
def get_nave(idnave):
    naves = Nave.query.filter_by(idnave = idnave)
    naves = list(map(lambda nave: nave.serialize(), naves))

    return jsonify(naves), 200


@app.route('/api/naves', methods=['POST'])
def post_naves():

    name = request.json.get('name')
    model = request.json.get('model')
    vehicle_class = request.json.get('vehicle_class')
    cargo_capacity = request.json.get('cargo_capacity')
    passenger = request.json.get('passenger')
    

    nave = Nave()
    nave.name = name
    nave.model = model
    nave.vehicle_class = vehicle_class
    nave.cargo_capacity = cargo_capacity
    nave.passenger = passenger
    
    nave.save()
 
    return jsonify(nave.serialize()), 201


@app.route('/api/naves/<int:idnave>', methods=['PUT'])
def put_nave(idnave):

    name = request.json.get('name')
    model = request.json.get('model')
    vehicle_class = request.json.get('vehicle_class')
    cargo_capacity = request.json.get('cargo_capacity')
    passenger = request.json.get('passenger')
    
    
    nave = Nave.query.get(idnave)
    nave.name = name
    nave.model = model
    nave.vehicle_class = vehicle_class
    nave.cargo_capacity = cargo_capacity
    nave.passenger = passenger
    
    nave.update()
 
    return jsonify(nave.serialize()), 201

@app.route('/api/naves/<int:idnave>', methods=['DELETE'])
def delete_naves(idnave):

    nave = Nave.query.get(idnave)
    nave.delete()
    
    return jsonify({ "status": True, "msg": "Nave elminado"}), 200

if __name__=='__main__':
    app.run()  