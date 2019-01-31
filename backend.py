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


def create_table_details():
    """
    Create table contain details about airplane

    :return: table
    """
    conn = psycopg2.connect("dbname='Airplanes' user='postgres' password='passtosql12' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS airplanes_details("
                "ID INTEGER,"
                "model TEXT,"
                "company TEXT,"
                "production_year INTEGER,"
                "number_of_airplanes INTEGER)")
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


def insert_into_table_details(airplane_id, model, company, production_year, number_of_airplanes):
    """
    Insert data into table airplanes_details

    :param airplane_id: integer
    :param model: string
    :param company: string
    :param production_year: integer
    :param number_of_airplanes: integer
    :return: new row in the table
    """
    conn = psycopg2.connect("dbname='Airplanes' user='postgres' password='passtosql12' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO airplanes_details (ID, model, company, production_year, number_of_airplanes)"
                " VALUES('%s', '%s', '%s', '%s', '%s')" % (airplane_id, model, company, production_year, number_of_airplanes))
    conn.commit()
    conn.close()


def view_table(table_name):
    """
    Selecting all data from table

    :param table_name: string
    :return: all rows from table
    """
    conn = psycopg2.connect("dbname='Airplanes' user='postgres' password='passtosql12' host='localhost' port='5432'")
    rows = pd.read_sql("SELECT * FROM {}".format(table_name), conn)
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


def update_table(table_name, airplane_id, column, new_value):
    """
    Update value in row

    :param table_name: string
    :param airplane_id: integer
    :param column: string
    :param new_value: string/float/integer
    :return: updated row
    """
    conn = psycopg2.connect("dbname='Airplanes' user='postgres' password='passtosql12' host='localhost' port='5432'")
    cur = conn.cursor()
    update_sql = "UPDATE {} SET {}='%s' WHERE id=%s".format(table_name, column) % (new_value, airplane_id)
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


def print_company_models(company_name):
    """
    Print all models for defined company

    :param company_name: string
    :return: all rows with defined company
    """
    conn = psycopg2.connect("dbname='Airplanes' user='postgres' password='passtosql12' host='localhost' port='5432'")
    rows = pd.read_sql("SELECT * FROM airplanes WHERE company='%s'" % company_name, conn)
    print(rows.to_string(index=False))
    conn.close()


def join_two_tables():
    """
    Join two tables as inner join

    :return:
    """
    conn = psycopg2.connect("dbname='Airplanes' user='postgres' password='passtosql12' host='localhost' port='5432'")
    rows = pd.read_sql("SELECT * FROM airplanes INNER JOIN airplanes_details ON (airplanes.id = airplanes_details.id)", conn)
    print(rows.to_string(index=False))
    conn.close()


def show_tables():
    """
    Show all available tables in database

    :return:
    """
    conn = psycopg2.connect("dbname='Airplanes' user='postgres' password='passtosql12' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public' ORDER BY table_schema,"
                "table_name")
    tables = cur.fetchall()
    for table in tables:
        print(table[0])
    conn.close()


show_tables()
