import os

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.ora import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
  flights = db.excute("SELECT * FROM flights").fetchall()
  return render_template("index.html", flights=flights)

@app.route("/book", methods=["POST"])
def book():
  """Book a flight."""
  #GET form information
  name = request.form.get("name")
  try:
    light_id = int(request.form.get("flight_id"))
  except ValueError:
    return render_template("error.html", message="Invalid flight number.")
  # Make sure the flight exists
  if db.excute("SELECT * FROM flights WHERE id = :id, {"id":light_id}).rowcount == 0:
    return render_template("error.html", message="No such flight with that id.")
  db.execute("INSERT INTO passengers (name, flight_id) VALUES (:name, :flight_id)", {"name":name, "flight_id":flight_id} )
  db.commit()
  return render_template("success.html")
