import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        connection  = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "Thukubrian1@2024",
)
    
        if connection.is_connected():
            cursor = connection.cursor()

            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            print("Database 'alx_book_store' has successfully been created")

    
    except mysql.connector.Error:
        print("Error while connecting to MYSQL {e}")


    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
        
        print("MYSQL connection was closed")

if __name__ == "__main__":
    create_database()