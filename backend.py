import psycopg2
import pandas as pd
"""Module for managing database"""


def create_table():
    """
    Create table in database

    :return: table
    """
    conn = psycopg2.connect("dbname='Airplanes' user='postgres' password='passtosql12' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS airplanes("
                "ID SERIAL PRIMARY KEY,"
                "model TEXT,"
                "company TEXT,"
                "type TEXT,"
                "spread REAL,"
                "length REAL,"
                "height REAL,"
                "surface_area REAL,"
                "mass INTEGER,"
                "maximum_velocity INTEGER,"
                "flying_velocity INTEGER,"
                "mach_number REAL)")
    conn.commit()
    conn.close()


def insert_into_table(model, company, airplane_type, spread, length, height, surface_area, mass, maximum_velocity, flying_velocity, mach_number):
    """
    Insert data into database table

    :param model: string
    :param company: string
    :param airplane_type: string
    :param spread: float
    :param length: float
    :param height: float
    :param surface_area: float
    :param mass: integer
    :param maximum_velocity: integer
    :param flying_velocity: integer
    :param mach_number: float
    :return: new row
    """
    conn = psycopg2.connect("dbname='Airplanes' user='postgres' password='passtosql12' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO airplanes (model, company, type, spread, length, height, surface_area, mass, "
                "maximum_velocity, flying_velocity, mach_number)"
                " VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
                % (model, company, airplane_type, spread, length, height, surface_area, mass, maximum_velocity, flying_velocity, mach_number))
    conn.commit()
    conn.close()


def view_table():
    """
    Selecting all data from table

    :return: all rows from table
    """
    conn = psycopg2.connect("dbname='Airplanes' user='postgres' password='passtosql12' host='localhost' port='5432'")
    rows = pd.read_sql("SELECT * FROM airplanes", conn)
    print(rows.to_string(index=False))
    conn.close()


def delete_from_table(airplane_id):
    """
    Delete from table by id

    :param airplane_id: integer
    :return: deleted row
    """
    conn = psycopg2.connect("dbname='Airplanes' user='postgres' password='passtosql12' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM airplanes WHERE id=%s", (airplane_id,))
    conn.commit()
    conn.close()


def update_table(airplane_id, column, new_value):
    """
    Update value in row

    :param airplane_id: integer
    :param column: string
    :param new_value: string/float/integer
    :return: updated row
    """
    conn = psycopg2.connect("dbname='Airplanes' user='postgres' password='passtosql12' host='localhost' port='5432'")
    cur = conn.cursor()
    update_sql = "UPDATE airplanes SET {}='%s' WHERE id=%s".format(column) % (new_value, airplane_id)
    cur.execute(update_sql)
    conn.commit()
    conn.close()


def top_5(column):
    """
    Show top 5 rows by defined category

    :param column: string
    :return: 5 rows ordered by defined category
    """
    conn = psycopg2.connect("dbname='Airplanes' user='postgres' password='passtosql12' host='localhost' port='5432'")
    rows = pd.read_sql("SELECT * FROM airplanes ORDER BY {} DESC LIMIT 5".format(column), conn)
    print(rows.to_string(index=False))
    conn.close()


# view_table()
# insert_into_table("707", "Boeing", "Passenger", 44.42, 46.61, 12.93, 0, 66406, 0, 972, 0)
# insert_into_table("B-47E Statojet", "Boeing", "Military", 35.63, 33.48, 8.5, 132.7, 366300, 975, 0, 0.9)
# insert_into_table("787", "Boeing", "Passenger", 60, 63, 16.92, 325, 115000, 945, 903, 0.89)
# insert_into_table("General Dynamics F-16 Fighting Falcon", "Lockheed Martin", "Military", 9.8, 14.8, 4.8, 27.87, 8272,
#                  2300, 1000, 2.02)
# insert_into_table("X-15", "North American Aviation", "Military", 6.8, 15.45, 4.12, 18.6, 6620, 7274, 0, 6)
# insert_into_table("SR-71 Blackbird", "Lockheed", "Military", 16.94, 32.34, 5.64, 167.3, 27216, 3530, 3173, 3.56)
# delete_from_table(3)
# view_table()
# update_table(8, "company", "North American Aviation")
# view_table()
top_5("flying_velocity")
