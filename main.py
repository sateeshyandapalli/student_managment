from flask import Flask, request, render_template
from database import db

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/createStudent', methods=['POST'])
def createStudent():
    db.create([{"id": "32362", "first_name": "hdfhjdfh", "last_name": "jsdhdkshdsd"}])
    return {"status": "success"}


@app.route('/getStudent', methods=['GET'])
def getStudent():
    d = db.get("32362")
    return {"status": "success", "data": d}


@app.route('/updateStudent', methods=['POST'])
def updateStudent():
    pass


@app.route('/deleteStudent', methods=['GET'])
def deleteStudent():
    db.delete("32362")
    return {"status": "success"}


if __name__ == '__main__':
    app.run()
