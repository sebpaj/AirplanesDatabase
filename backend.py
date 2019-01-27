import psycopg2
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


def insert_into_table():
    """
    Insert data into database table

    :return: row in table
    """
