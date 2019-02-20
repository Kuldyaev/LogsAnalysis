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
        [ """SELECT articles.title as Article,
             COUNT(*) as hits
             FROM articles,log
             WHERE log.path = CONCAT('/article/',articles.slug)
             GROUP BY articles.title 
	     ORDER BY hits DESC 
	     LIMIT 3; """] , 'ans1'],
2 : ['Who are the most popular article authors of all time?', 
     ["""SELECT authors.name, COUNT(*) AS num
        FROM authors
        JOIN articles
        ON authors.id = articles.author
        JOIN log
        ON log.path LIKE CONCAT('/article/%', articles.slug)
        GROUP BY authors.name
        ORDER BY num DESC
        LIMIT 3;"""], 'ans2'],
3 : ['On which days did more than 1% of requests lead to errors?', 
        ["""
        SELECT total.day,
          ROUND(((errors.error_requests*1.0) / total.requests), 3) AS percent
        FROM (
          SELECT date_trunc('day', time) "day", count(*) AS error_requests
          FROM log
          WHERE status LIKE '404%'
          GROUP BY day
        ) AS errors
        JOIN (
          SELECT date_trunc('day', time) "day", count(*) AS requests
          FROM log
          GROUP BY day
          ) AS total
        ON total.day = errors.day
        WHERE (ROUND(((errors.error_requests*1.0) / total.requests), 3) > 0.01)
        ORDER BY percent DESC;
    """], 'ans3']
}        
        
        
def main():
    statment = "\n"
    for i in [1, 2, 3]:
        query = dict[i][1][0]    
        answer = work(query)
        statment += '\n Question ' + str(i) +': ' + str(dict[i][0]) + '\n Answer ' + str(i) + ': '
        print (answer)
        if i==1:
            for rec in answer:
                stat01 = ("\n \t" + rec[0] + " -- " + str(rec[1]) + " views")
                statment +=  stat01
        elif i==2:
            for rec in answer:
                stat02 =("\n \t" + rec[0] + " -- " + str(rec[1]) + " views")
                statment +=  stat02
        else:
            statment += str(answer)
        dict[i][2] = answer
    print (statment) 
 
if __name__ == '__main__':
    main()
