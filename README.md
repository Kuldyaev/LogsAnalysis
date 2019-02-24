# Logs Analysis

#### This is Project №3 in the Udacty Full Stack Nanodegree Program

This is a program that answers a few questions about the news database, such as who are the most popular authors and what are the most popular articles. It uses python to query a PostgreSQL database.

For this project, you will need:
* Python 3
* Vagrant
* VirtualBox

To run this program, the user needs to setup the news database.

To use the same virtual machine to run this SQL database, you will first need to download VirtualBox, this will run the virtual machine. You do not need the extension pack, SDK or to launch the virtualbox, vagrant will do that. This is the link to download virtual box:

https://www.virtualbox.org/wiki/Download_Old_Builds_5_1

Download vagrant, install the version for your operating system. This is the link:

https://www.vagrantup.com/downloads.html

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
