import pyodbc


# Database connection function
def get_db_connection():
    connection_string = (
        "DRIVER={ODBC Driver 17 for SQL Server}; "
        "SERVER=localhost,1433; "
        "DATABASE=AdventureWorks2012; "
        "UID=RobotTestUser1; "
        "PWD=testPass;"
    )
    try:
        conn = pyodbc.connect(connection_string)
        print("Connection successful!")
        return conn
    except pyodbc.Error as e:
        raise Exception(f"Error connecting to the database: {str(e)}")
