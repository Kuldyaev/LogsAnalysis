# Logs Analysis

#### This is Project №3 in the Udacty Full Stack Nanodegree Program


To run this program, the user needs to setup the news database.
For this project, you will need:
* Python 3
* Vagrant
* VirtualBox

Download the schema and data file here: 

https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

Create and setup the database with the command: psql -d news -f newsdata.sql

The database should include three tables:
* authors
* articles
* log


This Python program runs from the command line without any input from the user. It connects to the database, then uses SQL queries to analyze the data and print out answers. Each question is answered using a single SQL query in a single function. Python is used for minimal "post-processing" (specifically formatting the output and calculating a more accurate % failure rate.)

The program must be run from within a VM environment such as vagrant. To execute the program, type into the command line: python3 newsdata.py

Also included is output.txt containing the output of the LogA.py code.
