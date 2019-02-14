#!/usr/bin/env python

import psycopg2

def main():
    try: 
	    db = psycopg2.connect(database='news' , user='postgres' , password='postgres' , port=5432, host='localhost')
	    print ("OK")
	    cursor=db.cursor()
	    cursor.execute('SELECT * FROM log LIMIT 5')
	    for row in cursor:
		    print (row)
	    cursor.close()
	    cursor.execute()
        results = cursor.fetchall('SELECT * FROM authors LIMIT 2')
		for article in results:
            title = article[0]
            views = article[1]
            print("\"%s\" - %s views." % (title, views))
        cursor.close()
	    db.close()
    except:
	    print ('FAIL')




if __name__ == '__main__':
    main()
