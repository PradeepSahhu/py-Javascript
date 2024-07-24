
from flask import Flask,render_template,request,redirect
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

@app.route("/")
def home():
    return "<p>Hello home page</p>"

@app.route("/pradeep",methods=["GET","POST"])
def submitingToDB():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        print(title,description)
        todo = ToDo(title=title,desc=description)
        db.session.add(todo)
        db.session.commit()

    all_tasks = ToDo.query.order_by(ToDo.date_created).all()
    print(all_tasks)

    return render_template("index.html", all_tasks=all_tasks)

@app.route("/delete/<int:id>")
def delete(id):
    task_delete = ToDo.query.get_or_404(id)

    try:
        db.session.delete(task_delete)
        db.session.commit()
        return redirect("/pradeep")
    
    except:
        return "Their is some problem in deletion"

@app.route("/update/<int:id>",methods=["GET","POST"])
def updation(id):
    task_update = ToDo.query.get_or_404(id)
    try:
        if(request.method == "POST"):
            task_update.title = request.form["title"]

            try:
                db.session.commit()
                return redirect("/pradeep")
            except:
                return "their is some problem in updation in inner"
        else:
            return render_template("updation.html", task_update=task_update)
    except:
        return "their is some problem in updation in outer"


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