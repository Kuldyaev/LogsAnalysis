# Logs Analysis

#### This is Project №3 in the Udacty Full Stack Nanodegree Program

This is a program that answers a few questions about the news database, such as who are the most popular authors and what are the most popular articles. It uses python to query a PostgreSQL database.

For this project, you will need:
* Python 3
* Vagrant
* VirtualBox

To run this program, the user needs to setup the news database.

Download the schema and data file here: 

https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

Create and setup the database with the command: 
```
psql -d news -f newsdata.sql
```
The database should include three tables:
* authors
* articles
* log

Download/Clone LogA.py file from  this repository.

The program must be run from within a VM environment such as vagrant.

In your python terminal, switch to the directory you have saved these files in and run LogA.py.

```
$ python LogA.py
```

This repositoryt also included is output.txt containing the output of the LogA.py code.
