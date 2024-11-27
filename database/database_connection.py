import psycopg2
from database_configs import db_config

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
