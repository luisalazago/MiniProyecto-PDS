"""
https://pynative.com/python-postgresql-insert-update-delete-table-data-to-perform-crud-operations/
"""

import psycopg2

def insert(postgres_insert_query, record_to_insert="", table=""):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="PolloFrito1*",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres")
        cursor = connection.cursor()
        cursor.execute(postgres_insert_query, record_to_insert)
        record = cursor.fetchall()
        print(record)
        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into {} table".format(table))
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)


def select(postgres_insert_query, record_to_select="", table=""):
    ans = []
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="PolloFrito1*",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres")
        cursor = connection.cursor()
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
