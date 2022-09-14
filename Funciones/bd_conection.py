"""
https://pynative.com/python-postgresql-insert-update-delete-table-data-to-perform-crud-operations/
"""

import psycopg2

contrasenia = "begueta124"

def connection_bd(password_, user_="postgres", host_="127.0.0.1", port_="5432", database_="postgres"):
    connection = psycopg2.connect(user=user_,
                                  password=password_,
                                  host=host_,
                                  port=port_,
                                  database=database_)
    cursor = connection.cursor()
    return cursor, connection
    
def insert(postgres_insert_query, record_to_insert="", table=""):
    ans = -1
    try:
        cursor, connection = connection_bd(contrasenia)
        print(record_to_insert)
        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()
        count = ans = cursor.rowcount
        print(count, "Record inserted successfully into {} table".format(table))
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
    except (Exception, psycopg2.Error) as error:
        print("Error in insert operation", error)
    return ans


def insertMany(postgres_insert_query, record_to_insert="", table=""):
    ans = -1
    try:
        cursor, connection = connection_bd(contrasenia)
        cursor.executemany(postgres_insert_query, record_to_insert)

        connection.commit()
        count = ans = cursor.rowcount
        print(count, "Record inserted successfully into {} table".format(table))
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
    except (Exception, psycopg2.Error) as error:
        print("Error in insertMany operation", error)
    return ans


def select(postgres_insert_query, record_to_select="", table=""):
    ans = []
    try:
        cursor, connection = connection_bd(contrasenia)
        cursor.execute(postgres_insert_query, record_to_select)
        ans = cursor.fetchall()

        connection.commit()
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)
    return ans
