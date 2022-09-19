# Database template


This database template is made for a Linux distro and so is the rest of the guide. 
It was last tested on a laptop with 20.04.1-Ubuntu on 25-03-2022, where it is confirmed that everything worked.

In order to follow this guide, the reader is expected to have a basic understanding of SQL syntax and Linux usage.

## Table of Contents

1. Install and setup of MariaDB.
2. Login to MariaDB and create a database.
3. database_template.py



# 1. Install and setup of MariaDB

Open a terminal on the laptop you which to run your database.

### Update and upgrade your computer.
```
$ sudo apt update && sudo apt upgrade -y
```

### Install MariaDB (make sure to get the latest version)
```
$ sudo apt install mariadb-server
```

Find the latest version: https://mariadb.org/download/
Make sure to get a stable version which will have the longest support from the vendor.

To verify your MariaDB server version use the following command:
```
$ dpkg -l | grep mariadb-server
```
This will list the installed mariadb server packages with its specific version.

### Configure MariaDB and setup root user and password
```
$ sudo mysql_secure_installation
``` 

Guide to help you through the secure setup:
https://mariadb.com/kb/en/mysql_secure_installation/

#NOTE: Your root user will get you access to the MariaDB on your laptop. It can be used to create/delete database as well as users. 

### Install the Python SQL library "mysql.connector"
```
$ sudo python3 -m pip install mysql-connector-python
```
Verify your installation with the following command:
```
$ python3 -m pip check mysql-connector-python
```
or use:
```
$ dpkg -l | grep mariadb-server
```
This will display all packages installed containing the name 'mariadb-server'.

# 2. Login to MariaDB and create a database.

If everything in step 1 'Install and setup of MariaDB' continue with this section.

Open a terminal on the laptop you installed MariaDB and type the following:
```
$ mysql -u root -p
```
Type in the password for the root user you made during the configuration of MariaDB.
#NOTE: Replace your root password with the 'new_password' string in the database_template.py file. The program needs this password to access MariaDB on your laptop.

The terminal should now display: 
MariaDB [(none)]> 
This indicate you have successfully accessed the MariaDB.

Now we want to create our database by typing:
```
CREATE DATABASE <database_name>;
```
SQL syntax requires all commands end with a ';'
#NOTE Replace the 'new_database' string in the database_template.py file with the name of your database. MariaDB needs to know which specific database it accesses since you could have several.

To verify your database has been created type:
```
SHOW DATABASES;
```
Your new database should appear in the terminal.

To enter the database type:
```
USE <database_name>;
```
Notice how MariaDB [(none)]> changes to MariaDB [database_name]> 

From here on your new database is set and ready to go.
Try run the database_template.py file. If any errors occurs, go back and check you did every step as described in this README file. 


# 3. database_template.py

The file 'database_template.py' contains the basic setup for initializing a database object.
This object can then be used to perform basic SQL operations.

The main program:
Create a 'movie' table with four attributes:   

|id        | title         | release_year  	| genre   |
| -------- | ------------- | -------------- | ------- |
| INT AUTO INCREMENT | VARCHAR | YEAR       | VARCHAR |

Next up two movies are inserted which will make the database contain the following: 

|  id   | title  | release_year  	| genre  |
| -------- | ------------- | -------- | --- |
|  1  | Deadpool     |   2016   |   Action         |
|  2  | The Batman   |   2022   |  Action/Adventure|

Then the genre attribute for 'Deadpool' is updated:
'Action' -> 'Action/Adventure'

Before and after this update a print statement display the first row to show the update. 

If the program terminate without any errors you should see the following statement in the terminal:
```
(1, 'Deadpool', 2016, 'Action')
(1, 'Deadpool', 2016, 'Action/Fantasy')  
```

Hope this was helpful and enjoy!


