#!/usr/bin/env python

import psycopg2

def main():
    try:
	    db = psycopg2.connect(database = 'news', 
		                      user = 'postgres',
							  password = 'postgres',
							  post = 5432,
							  host = 'localhost')
		print ('The connection is established')
	except:
	    print ('The connection is failed')

	cursor = db.cursor()
	cursor.execute("SELECT * FROM log LIMIT 5")
	for row in cursor:
		print (row)
	cursor.close()
	db.close()

if __name__ == '__main__':
    main()