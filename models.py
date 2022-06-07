from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    iduser = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    nameuser = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    emailuser = db.Column(db.String(250), nullable=False, unique=True)

    def serialize(self):
        return{
            "id": self.iduser,
            "name": self.name,
            "last_name": self.last_name,
            "nameuser": self.nameuser,
            "emailuser": self.emailuser
        }


    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()