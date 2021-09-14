from database import db_connection


def is_connected():
    return db_connection.is_connected()


def create(data):
    try:
        if is_connected():
            db_cursor = db_connection.cursor()
            for d in data:
                db_cursor.execute(
                    "INSERT INTO student (id, first_name, last_name) VALUES ('" + d.get("id") + "', '" + d.get(
                        "first_name") + "', + '" + d.get("last_name") + "')")
                db_connection.commit()
            db_cursor.close()
    except Exception as e:
        return str(e)


def update(student: dict):
    if is_connected():
        pass


def get(id: str):
    try:
        if is_connected():
            data = {}
            db_cursor = db_connection.cursor()
            db_cursor.execute("select * from student WHERE id='" + id + "';")
            myresult = db_cursor.fetchall()
            for x in myresult:
                data.update({"id": x[0], "first_name": x[1], "last_name": x[2]})
            db_cursor.close()
            return data
    except Exception as e:
        return str(e)


def delete(id: str):
    try:
        if is_connected():
            db_cursor = db_connection.cursor()
            db_cursor.execute("delete from student WHERE id='" + id + "'")
            db_connection.commit()
            db_cursor.close()
    except Exception as e:
        return str(e)
