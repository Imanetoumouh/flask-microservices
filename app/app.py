import os
# This is my first image
from flask import Flask, render_template, request
import mysql.connector

#SQLAlchemy pour les connexions à la base de données dans l'applications Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# la variable de configuration: définit l'URL de la base de données MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{os.environ['DATABASE_USER']}:{os.environ['DATABASE_PASSWORD']}@{os.environ['DATABASE_HOST']}/{os.environ['DATABASE_NAME']}"
# Initialisez SQLAlchemy : crée une instance de la classe SQLAlchemy et la lie à l'application Flask.
db = SQLAlchemy(app)

# Connectez-vous à la base de données à l'aide de mysql.connector
""" connection = mysql.connector.connect(
    host=os.environ['DATABASE_HOST'],
    port=int(os.environ['DATABASE_PORT']),
    database=os.environ['DATABASE_NAME'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD']
) """"

#cursor = connection.cursor()

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        age = request.form['age']
        module = request.form['module']

        # la classe Student
        student = Student(name=name, email=email, age=age, module=module)
        db.session.add(student)
        db.session.commit()
        #cursor.execute("INSERT INTO student (name, email, age, module) VALUES (%s, %s, %s, %s)", (name, email, age, module))
        #connection.commit()

    return render_template("index.html")

@app.route("/DevOps", methods=['GET', 'POST'])
def DevOps():
    students = Student.query.filter_by(module='DevOps').all()
    return render_template("registration.html", students=students, module='DevOps')
    #cursor.execute("SELECT * FROM student WHERE module = 'DevOps'")
    #data = cursor.fetchall()
    #return render_template("registration.html", data=data, module='DevOps')

@app.route("/BigData", methods=['GET', 'POST'])
def BigData():
    students = Student.query.filter_by(module='BigData').all()
    return render_template("registration.html", students=students, module='BigData')
    #cursor.execute("SELECT * FROM student WHERE module = 'BigData'")
    #data = cursor.fetchall()
    #return render_template("registration.html", data=data, module='BigData')

@app.route("/DataMining", methods=['GET', 'POST'])
def DataMining():
    students = Student.query.filter_by(module='DataMining').all()
    return render_template("registration.html", students=students, module='DataMining')
    #cursor.execute("SELECT * FROM student WHERE module = 'DataMining'")
    #data = cursor.fetchall()
    #return render_template("registration.html", data=data, module='DataMining')

if __name__ == "__main__":
    app.run(debug=True)
