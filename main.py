from flask import Flask, request, render_template
from services import create_student as cs, get_student as gs, delete_student as ds, update_student as us, \
    list_students as ls

app = Flask(__name__, static_folder='ui', template_folder="templates/")


# @app.route("/")
# def index():
#     return render_template("index.html")


@app.route('/createStudent', methods=['POST'])
def create_student():
    c = cs.CCreateStudent()
    done, err = c.create()
    return prepare_response(done, err, "createStudent")


@app.route('/getStudent', methods=['GET'])
def get_student():
    id = request.args.get('id')
    if id is None or len(id) == 0:
        return prepare_response(False, "Invalid Id", "getStudent")

    g = gs.CGetStudent(id=id)
    done, err, data = g.get_student()
    return prepare_response(done, err, "getStudent", data)


@app.route('/updateStudent', methods=['POST'])
def update_student():
    data = request.json
    if data is None or len(data) == 0:
        return prepare_response(False, "Invalid Json", "updateStudent")

    if data.get("id") is None or len(data.get("id")) == 0:
        return prepare_response(False, "Invalid ID", "updateStudent")

    if data.get("first_name") is not None and len(data.get("first_name")) == 0:
        return prepare_response(False, "Invalid first_name", "updateStudent")

    if data.get("last_name") is not None and len(data.get("last_name")) == 0:
        return prepare_response(False, "Invalid last_name", "updateStudent")

    u = us.CUpdateStudent(data=data)
    done, err = u.update_student()
    return prepare_response(done, err, "updateStudent")


@app.route('/deleteStudent', methods=['GET'])
def delete_student():
    id = request.args.get('id')
    if id is None or len(id) == 0:
        return prepare_response(False, "Invalid Id", "deleteStudent")

    d = ds.CDeleteStudent(id=id)
    done, err = d.delete_student()
    return prepare_response(done, err, "deleteStudent")


# @app.route('/listStudents', methods=['GET'])
# def list_students():
#     l = ls.CListStudents()
#     done, err, data = l.list_students()
#     return prepare_response(done, err, "listStudents", data)


def prepare_response(done, err, service, data=None):
    if done:
        if service.__eq__("createStudent"):
            return {"status": "success", "statusCode": 0, "message": "students created successfully"}
        elif service.__eq__("getStudent"):
            return {"status": "success", "statusCode": 0, "message": "student information sent successfully",
                    "data": data}
        elif service.__eq__("listStudents"):
            return {"status": "success", "statusCode": 0, "message": "students list sent successfully",
                    "data": data}
        elif service.__eq__("updateStudent"):
            return {"status": "success", "statusCode": 0, "message": "student information updated successfully"}
        elif service.__eq__("deleteStudent"):
            return {"status": "success", "statusCode": 0, "message": "student deleted successfully"}
    if err is not None:
        return {"status": "failed", "statusCode": 1, "message": err}


if __name__ == '__main__':
    app.run()
