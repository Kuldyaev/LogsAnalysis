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
        ["""SELECT to_char(time, 'DD FMMonth YYYY') AS date,
        (count(status) filter (where status like '404%'))
        * 100.0 / (count(status)) as errors
        FROM log group BY date
        having errors (status) > 1.0;"""], 'ans3']
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
