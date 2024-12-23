import pyodbc

# Connection string with Windows Authentication
conn_string = r'Driver={ODBC Driver 17 for SQL Server};Server=Akanksha\SQLEXPRESS;Database=akanksha44;Trusted_Connection=yes;'

def readFromSql():
    try:
        # Establish the connection
        conn = pyodbc.connect(conn_string)
        cursor = conn.cursor()

        # Execute a sample query
        cursor.execute("SELECT * FROM ak1 where id=1")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    except pyodbc.Error as ex:
        print("Connection error:", ex)

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

readFromSql()