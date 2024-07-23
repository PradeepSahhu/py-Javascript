
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///TODO.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'  # Corrected path
db = SQLAlchemy(app)



class ToDo(db.Model):
    sno = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(200),nullable=False)
    desc = db.Column(db.String(500),nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self)->str:
        return f"{self.sno} - {self.title}"


@app.route("/",methods=["GET","POST"])
def hello_world():
    if request.method == "POST":
        print("POST")
    todo = ToDo(title="First todo",desc="Start it for now and see it")
    db.session.add(todo)
    db.session.commit()
    return "<p>Hello, World!</p>"


@app.route("/pradeep")
def products():
    return render_template("index.html")


# if __name__ == "__main__":
#     app.run(debug=True,port=8000)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Ensure tables are created
    app.run(debug=True, port=8000)

# in templates - html file is stored
# in static - static data is stored like text file like images like videos