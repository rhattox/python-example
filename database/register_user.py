import psycopg2
from database.database_configs import db_config


def register_user(user):
    try:
        # Establish the connection
        connection = psycopg2.connect(**db_config)

        # Create a cursor object
        cursor = connection.cursor()

        # Execute a SQL query
        cursor.execute(
            "INSERT INTO users_table (name, email, password) VALUES (%s, %s, %s);",
            (user.name, user.email, user.password)
        )
        connection.commit()
        print("User successfully registered!")
    except (Exception, psycopg2.Error) as error:
        print(f"Error while connecting to PostgreSQL: {error}")
    finally:
        # Close the connection
        if 'connection' in locals() and connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed.")
