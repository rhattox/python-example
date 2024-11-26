import psycopg2
from psycopg2 import sql

# Define your database connection parameters
db_config = {
    "dbname": "test",
    "user": "root",
    "password": "root",
    "host": "localhost",  # Or the IP address of your database server
    "port": 5432  # Default PostgreSQL port
}

try:
    # Establish the connection
    connection = psycopg2.connect(**db_config)

    # Create a cursor object
    cursor = connection.cursor()

    # Execute a SQL query
    cursor.execute("SELECT version();")

    # Fetch and print the result
    db_version = cursor.fetchone()
    print(f"PostgreSQL version: {db_version}")

except (Exception, psycopg2.Error) as error:
    print(f"Error while connecting to PostgreSQL: {error}")
finally:
    # Close the connection
    if 'connection' in locals() and connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed.")

init