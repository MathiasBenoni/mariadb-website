# A website using mariaDB

## A website that displays the most common adjective describing the website

This website uses python as backend. `app.py` is connected to the HTML. `app.py` then sends this info to `mariadb_python.py`, this script then takes the adjective and stores it in the database. The database is to be updated.

Also planned to do a wordcloud for all the adjectives, instead of just a word

# The installation

## Create an environment

Create a project folder and a .venv folder within with this command:

```
mkdir myproject
cd myproject
python3 -m venv .venv
```

## Install Flask

- Open a terminal or use the one in Visual Studio Code
- Navigate to your project folder
- Run the command bellow to install Flask

```
pip install Flask
```

## Install mariaDB for Mac

If you are on mac, run this command to install mariaDB and update to latest version

```
brew install mariadb
brew upgrade mariadb
```

If you are using Windows, go to [mariaDB](https://mariadb.com/docs/server/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-msi-packages-on-windows)'s website and follow the guide there

## Setup mariaDB for Mac

Navigate to your local `terminal`.

Start mariaDB

```
brew services start mariadb
```

If you later want to stop the database you can run

```
brew services stop mariadb
```

If it is your first time using mariaDB you need to login without a password to setup a password

```
sudo mariadb -u root
```

This now puts you inside mariaDB, if you want to exit mariaDB, just type `EXIT;` or `QUIT;`or just `Ctrl + D`

### Setup your user

```
CREATE USER 'username'@'localhost' IDENTIFIED BY 'secure_password';
```

`username`is what you will use for logging in, as well as your `secure_password`

#### The pythonscript uses `pythonuser` as username and `pythonpass`as password

```
CREATE USER 'pythonuser'@'localhost' IDENTIFIED BY 'pythonpass';
```

You should now be logged in as root user, even though you just created a new one. The root user has all the privileges, if you want your user that you just created to also have all privileges, you can run

```
GRANT ALL PRIVILEGES ON *.* TO 'username'@'localhost';
```

#### Example

```
GRANT ALL PRIVILEGES ON *.* TO 'pythonuser'@'localhost';
```

#### Give privileges specific to a specific database (Recommended)

```
GRANT SELECT, INSERT, UPDATE ON database_name.* TO 'username'@'localhost';
```

#### For my script

```
GRANT SELECT, INSERT, UPDATE ON adjectives.* TO 'pythonuser'@'localhost';
```
