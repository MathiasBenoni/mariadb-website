# A website using mariaDB

## A website that displays the most common adjective describing the website

This website uses python as backend. `app.py` is connected to the HTML. `app.py` then sends this info to `mariadb_python.py`, this script then takes the adjective and stores it in the database. The database is to be updated.

Also planned to do a wordcloud for all the adjectives, instead of just a word

# The installation

## Create an environment

Create a project folder and a `.venv` folder within with this command:

```
mkdir myproject
cd myproject
python3 -m venv .venv
```

## Install Flask

- Open a `terminal` or use the one in Visual Studio Code
- Navigate to your project folder
- Run the command bellow to install Flask

```
pip install Flask
```

## Install mariaDB for Mac

[If you are using Windows, go to mariaDB's website and follow the guide there](https://mariadb.com/docs/server/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-msi-packages-on-windows)

Run this command to install mariaDB and update to latest version

```
brew install mariadb
brew upgrade mariadb
```

## Start mariaDB for Mac

Navigate to your local `terminal`.

Start mariaDB

```
brew services start mariadb
```

If you later want to stop the database you can run

```
brew services stop mariadb
```

## Windows

.....

## Setup mariaDB

If it is your first time using mariaDB, you need to login without a password to setup a password

```
sudo mariadb -u root
```

This now puts you inside mariaDB, if you want to exit mariaDB, just type `EXIT;`, `QUIT;` or just `Ctrl + D`

### Setup your user

```
CREATE USER 'username'@'localhost' IDENTIFIED BY 'secure_password';
```

#### The pythonscript uses `pythonuser` as username and `pythonpass`as password

```
CREATE USER 'pythonuser'@'localhost' IDENTIFIED BY 'pythonpass';
```

You should now be logged in as root user, even though you just created a new one. The root user has all the privileges, if you want your user that you just created to also have all privileges, you can run

```
GRANT ALL PRIVILEGES ON *.* TO 'username'@'localhost';
```

#### Give privileges to a specific database (Recommended)

```
GRANT SELECT, INSERT, UPDATE ON database_name.* TO 'username'@'localhost';
```

#### For my script

```
GRANT SELECT, INSERT, UPDATE ON adjectives.* TO 'pythonuser'@'localhost';
```

#### After you have done that, you need to save the changes

```
FLUSH PRIVILEGES;
```

#### If you are unsure that you have done it correctly you can run

```
SHOW GRANTS FOR 'pythonuser'@'localhost';
```

And you should see something like

```
+------------------------------------------------------------------+
| Grants for pythonuser@localhost
+------------------------------------------------------------------+
| GRANT USAGE ON *.* TO `pythonuser`@`localhost` IDENTIFIED BY PASSWORD
|'*C85F42CED428CAE393E47738770729D0657BB541'
| GRANT SELECT, INSERT, UPDATE ON `adjectives`.* TO `pythonuser`@`localhost`
+-------------------------------------------------------------------+
```

### Complete user-generation

```
CREATE USER 'pythonuser'@'localhost' IDENTIFIED BY 'pythonpass';
GRANT SELECT, INSERT UPDATE ON ON adjectives.* TO 'pythonuser'@'localhost';
FLUSH PRIVILEGES;
```

# Making the database

### Run this command to create the database used in this project

```
CREATE DATABASE adjectives;
```

#### Use the database

```
USE adjectives;
```

#### The code bellow will create all the neccesary information to get started

```
CREATE TABLE adjectives (
    id INT AUTO_INCREMENT PRIMARY KEY,
    adjective VARCHAR(50) NOT NULL
);
```

#### To be extra sure, run this command

```
DESCRIBE adjectives;
```

#### If it looks like this you are done, you can now `QUIT;`, `EXIT;` or `Ctrl + D` to get out of the terminal, and close it

```
+-----------+-------------+------+-----+---------+----------------+
| Field     | Type        | Null | Key | Default | Extra          |
+-----------+-------------+------+-----+---------+----------------+
| id        | int(11)     | NO   | PRI | NULL    | auto_increment |
| adjective | varchar(50) | NO   |     | NULL    |                |
+-----------+-------------+------+-----+---------+----------------+
```
