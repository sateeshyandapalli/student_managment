import mysql.connector
import config

db_connection = mysql.connector.connect(host=config.credentials.get('host'),
                                        user=config.credentials.get("user"),
                                        passwd=config.credentials.get("password"),
                                        port=config.credentials.get("port"),
                                        db=config.credentials.get("database"))
db_cursor = db_connection.cursor()
db_cursor.execute(
    "CREATE TABLE IF NOT EXISTS student (id VARCHAR(255) PRIMARY KEY, first_name VARCHAR(255), last_name varchar(255))")
db_cursor.close()