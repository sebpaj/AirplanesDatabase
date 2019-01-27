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
    update_sql = "UPDATE airplanes SET {}=%s WHERE id=%s".format(column) % (new_value, airplane_id)
    cur.execute(update_sql)
    conn.commit()
    conn.close()

# view_table()
# insert_into_table("707", "Boeing", "Passenger", 44.42, 46.61, 12.93, 0, 66406, 0, 972, 0)
# insert_into_table("B-47E Statojet", "Boeing", "Military", 35.63, 33.48, 8.5, 132.7, 366300, 975, 0, 0.9)
# delete_from_table(3)
# view_table()
# update_table(5, "mass", 36630)
view_table()
