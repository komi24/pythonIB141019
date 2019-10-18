from . import db

class Voiture(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  marque = db.Column(db.String(100))
  photo = db.Column(db.String(100))
