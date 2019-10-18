from flask import Flask, render_template, request, redirect
from uuid import uuid4
from models import db
from models.Voiture import Voiture


app = Flask(__name__, static_folder="public", static_url_path="/public")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///voiture.sqlite3"

with app.app_context():
  db.init_app(app)
  db.create_all()


@app.route("/")
def home():
    liste_voitures = Voiture.query.all()
    return render_template("index.html", liste=liste_voitures)

@app.route("/form", methods=["POST"])
def form():
    photo = request.files["photo"]
    filename = str(uuid4()) + photo.filename
    print(photo)
    photo.save('./public/images/'+filename)
    
    voiture = Voiture(
      marque=request.form.get("marque"),
      photo=filename)
    db.session.add(voiture)
    db.session.commit()

    return redirect("/")


app.run(port=5000, debug=True)
