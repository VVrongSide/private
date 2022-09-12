###################################################################################
# This database template was created by Anders Holm (DK).                        #
#                                                                                 #  
# The template is based on the database already created before running the       #
# program.                                                                        #
# Read the README.md to get this settled. It will guide you through the           #
# installation and setup.                                                         #
#                                                                                 #
###################################################################################


# Libraries to import
import mysql.connector              
from mysql.connector import errorcode
import datetime


# Database object
class Database(object):

    # Basic instans of the 'Database class'. 
    # Contains the needed attributes for to establish a connection to the database and create a cursor object.  
    
    def __init__(self, host, user, password, database):
        self.host        = host
        self.user        = user
        self.password    = password
        self.database    = database
        self.connection  = self.connect_db()
        self.cursor      = self.get_cursor()
        
        
    # Establish or open a connection to the database.
    def connect_db(self):
        conn = mysql.connector.connect(host=self.host, 
                                       user=self.user, 
                                       password=self.password, 
                                       database=self.database)
        return conn

    # Create cursor to commands to the database can be given.
    def get_cursor(self):
        return self.connection.cursor()

    # Close connection and cursor to the database.
    def disconnect_db(self):
        if self.connection.is_connected():
                self.cursor.close()
                self.connection.close()

"""

# Dummy program to show it works with a few examples.
if __name__ == '__main__':
    
    # Create a database object with the credential in the parenthesis.
    db = Database('localhost','root','new_password','new_database')
    

    #Creates a 'movies' table with a few attributes.
    db.cursor.execute("CREATE TABLE movie(id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(30),release_year YEAR(4),genre VARCHAR(30))")


    # First insert into the database.
    query = "INSERT INTO movie (title, release_year, genre) VALUES (%s,%s,%s)"
    data = ("Deadpool", 2016, "Action")
    db.cursor.execute(query,data)
    
    # Second insert into the database.
    db.cursor.execute("INSERT INTO movie (title, release_year, genre) VALUES ('The Batman',2022,'Action/Adventure')")
    
    # Commit first and second insert in the database 'movie'.
    db.connection.commit()
    

    # Select element in the row where id = 1 and prints it. 
    db.cursor.execute("SELECT * FROM movie WHERE id = 1")
    result = db.cursor.fetchall()
    for x in result:
        print(x)

    # Change a specific element in 'genre' column.
    db.cursor.execute("UPDATE movie SET genre = 'Action/Fantasy' WHERE title = 'Deadpool'")
    # Verify the change has been made to the database.
    db.cursor.execute("SELECT * FROM movie WHERE id = 1")
    result = db.cursor.fetchall()
    for x in result:
        print(x)

"""