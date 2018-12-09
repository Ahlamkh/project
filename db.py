#!/usr/bin/env python3


import psycopg2


DBNAME = "news"


def q1():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    select = """ SELECT articles.title, COUNT(log.path) AS views FROM
    articles JOIN log ON log.path=concat('/article/',articles.slug)
    GROUP BY articles.title ORDER BY views DESC LIMIT 3"""
    c.execute(select)
    data = c.fetchall()
    print "What are the most popular three articles of all time?"
    for word in data:
        print ('"'+word[0]+'"'+' _ '+str(word[1])+' views')
    db.close()


def q2():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    select = """SELECT authors.name,COUNT(log.path) AS views FROM
    articles,authors,log WHERE articles.author=authors.id
    AND log.path=concat('/article/',articles.slug)
    GROUP BY authors.name ORDER BY views DESC """
    c.execute(select)
    data = c.fetchall()
    print "Who are the most popular article authors of all time?"
    for word in data:
        print (word[0]+' _ '+str(word[1])+' views')
    db.close()


def q3():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
	select = """SELECT to_char(day, 'mon dd, yyyy') ,
    CONCAT(error , ' % errors')
    FROM (SELECT total.day , ROUND(CAST((100*part.num)AS numeric )
    /CAST(total.num AS numeric), 1) AS error FROM (SELECT date(time)
    AS day , COUNT(status) AS num FROM log GROUP BY day) AS total
    JOIN (SELECT date(time) AS day , COUNT(status) AS num FROM log WHERE
    status='404 NOT FOUND' GROUP BY day) AS part ON total.day=part.day)
    AS result WHERE error>1.0 """
	c.execute(select)
    data = c.fetchall()
    print "On which days did more than 1% of requests lead to errors?"
    for word in data:
        print (word[0]+' _ '+word[1])
    db.close()


q1()

q2()

q3()
