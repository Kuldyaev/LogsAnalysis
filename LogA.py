#!/usr/bin/env python
import psycopg2

def work(query):
    try:
        db = psycopg2.connect(database='news' , user='postgres' , password='postgres' , port=5432, host='localhost')
        print ("Connects to the database is completed")
        cursor=db.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        return results
        cursor.close()
        db.close()
    except:
	    print ('Connects to the database is failed')

dict = {
1 : ['What are the most popular three articles of all time?', 
        [ """SELECT a.title, a.slug, count(a.slug) as count 
            FROM log l JOIN articles a 
            ON l.path = concat('/article/', a.slug) 
            GROUP BY a.slug, a.title 
            ORDER BY count DESC 
            LIMIT 3;"""] , 'ans1'],
2 : ['Who are the most popular article authors of all time?', ["""SELECT count(l.id) as count, au.name 
                FROM articles a JOIN log l ON l.path = concat('/article/', a.slug) 
                JOIN authors au 
                ON au.id = a.author 
                GROUP BY au.name
                ORDER BY count DESC 
                LIMIT 3; """], 'ans2'],
3 : ['On which days did more than 1% of requests lead to errors?', ["""SELECT date
                FROM error_log_view
                WHERE "Percent Error" > 1"""], 'ans3']
}        
        
        
def main():
    statment = " "
    for i in [1, 2, 3]:
        query = dict[i][1][0]    
        answer = work(query)
        dict[i][2] = answer
        statment += '\n Question' + str(i) +': ' + str(dict[1][0]) + '\n Answer' + str(i) + ': '
        if i==1:
            for rec in dict[i][2]:
               stat01 = (rec[0] + " -- " + str(rec[2]) + " views")
            statment +=  stat01
        elif i==2:
            for rec in dict[i][2]:
                stat02 =(rec[1] + " -- " + str(rec[0]) + " views")
            statment +=  stat02
        else:
            statment += str(dict[i][2])
    print (statment) 
 
if __name__ == '__main__':
    main()
