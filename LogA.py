#!/usr/bin/env python
import psycopg2


def work(query):
    try:
        db = psycopg2.connect(database='news', user='postgres',
                              password='postgres', port=5432, host='localhost')
        cursor = db.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        db.close()
        return results
    except Exception:
        print('Connects to the database is failed')
        raise


dict = {
 1: ['What are the most popular three articles of all time?',
     ["""SELECT articles.title as Article,
        COUNT(*) as hits
        FROM articles,log
        WHERE log.path = CONCAT('/article/',articles.slug)
        GROUP BY articles.title
        ORDER BY hits DESC
        LIMIT 3; """], 'ans1'],
 2: ['Who are the most popular article authors of all time?',
     ["""SELECT authors.name, COUNT(*) AS num
        FROM authors
        JOIN articles
        ON authors.id = articles.author
        JOIN log
        WHERE log.path = CONCAT('/article/%',articles.slug)
        GROUP BY authors.name
        ORDER BY num DESC
        LIMIT 3;"""], 'ans2'],
 3: ['On which days did more than 1% of requests lead to errors?',
     ["""SELECT day, per FROM (
              SELECT day, round((sum(requests)/(
            SELECT count(*) FROM log
            WHERE substring(cast(log.time as text), 0, 11) = day) * 100), 2)
        AS per FROM (
          SELECT substring(cast(log.time as text), 0, 11) as day,
                  count(*) as requests FROM log
                  WHERE status like '%404%' GROUP BY day)
                   as log_percentage group by day order by per DESC)
                   as final_query
                   where per >= 1
            """], 'ans3']
}


def main():
    statment = "\n"
    for i in [1, 2, 3]:
        query = dict[i][1][0]
        answer = work(query)
        print(answer)
        statment += ('\n Question ' + str(i) + ': ' + str(dict[i][0]) +
                     '\n Answer ' + str(i) + ': ')
        if i == 1:
            for (art, view) in answer:
                stat01 = ('\n \t - "{}" -- {} views'.format(art, view))
                statment += stat01
        elif i == 2:
            for (autor, view) in answer:
                stat02 = ("\n \t - {} -- {} views".format(autor, view))
                statment += stat02
        else:
            statment += ("\n \t" + str(answer[0][0]) + "  " +
                         str(answer[0][1]) + '%' +
                         ' of requests lead to errors')
        dict[i][2] = answer
    print(statment)


if __name__ == '__main__':
    main()
