from database import db_connection


def is_connected():
    return db_connection.is_connected()


def create(data: dict):
    try:
        if is_connected():
            db_cursor = db_connection.cursor()
            db_cursor.execute(
                "INSERT INTO student (id, first_name, last_name) VALUES ('" + data.get("id") + "', '" + data.get(
                    "first_name") + "', + '" + data.get("last_name") + "')")
            db_connection.commit()
            db_cursor.close()
        else:
            False, "".format("database connection failed")
    except Exception as e:
        False, str(e)
    return True, None


def update(data: dict):
    try:
        if is_connected():
            db_cursor = db_connection.cursor()
            q = "update student set "
            if data.get("first_name") is not None:
                q = q + "first_name = '" + data.get("first_name") + "',"
            if data.get("last_name") is not None:
                q = q + "last_name = '" + data.get("last_name") + "',"
            q = q.rstrip(',')
            q = q + " where id = '" + data.get("id") + "'"
            db_cursor.execute(q)
            db_connection.commit()
            db_cursor.close()
        else:
            False, "".format("database connection failed")
    except Exception as e:
        False, str(e)
    return True, None


def get(id: str):
    data = {}
    try:
        if is_connected():
            db_cursor = db_connection.cursor()
            db_cursor.execute("select * from student WHERE id='" + id + "';")
            result = db_cursor.fetchall()
            for x in result:
                if len(x) == 3:
                    data.update({"id": x[0], "first_name": x[1], "last_name": x[2]})
            db_cursor.close()
        else:
            False, "".format("database connection failed"), None
    except Exception as e:
        return False, str(e), None
    return True, None, data,


def list():
    data = [["id", "first_name", "last_name"]]
    try:
        if is_connected():
            db_cursor = db_connection.cursor()
            db_cursor.execute("select * from student;")
            result = db_cursor.fetchall()
            for x in result:
                if len(x) == 3:
                    data.append([x[0], x[1], x[2]])
            db_cursor.close()
        else:
            False, "".format("database connection failed"), None
    except Exception as e:
        return False, str(e), None
    return True, None, data,


def delete(id: str):
    try:
        if is_connected():
            db_cursor = db_connection.cursor()
            db_cursor.execute("delete from student WHERE id='" + id + "'")
            db_connection.commit()
            db_cursor.close()
        else:
            False, "".format("database connection failed")
    except Exception as e:
        return False, str(e)
    return True, None
