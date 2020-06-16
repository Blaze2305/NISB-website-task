# NISB website task

This is a flask app for the nisb website task given as part of the core interview.

### How to run:
Create the following Database and Table in the mysql server
```sql
mysql> CREATE DATABASE nisb;
mysql> USE nisb;
mysql> CREATE TABLE users(
     _id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    ieee_num INTEGER NOT NULL,
    branch VARCHAR(20) NOT NULL,
    pass_hash VARCHAR(64) NOT NULL,
    pass_salt VARCHAR(6) NOT NULL,
    PRIMARY KEY (_id)
);
```
Set environment variables for the mysql server credentials
```sh
$ export mysql-user=<your username here>
$ export mysql-pass=<your password here>
```
This flask app requires [python 3.x](https://www.python.org/) to rub

Install the dependencies  and start the server.

```sh
$ pip install -m requirements.txt
$ python app.py
```

The flask app will be running on your localhost port 8080.
