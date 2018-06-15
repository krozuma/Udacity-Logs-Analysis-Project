#!/usr/bin/env python
import psycopg2


def pop_article():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    query = "select * from newsHits;"
    c.execute(query)
    rows = c.fetchall()
    for d in rows:
        print('{} {} {} {} '.format(d[0], '-', d[1], 'views'))
    db.close()


def pop_auth():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    query = "select * from authorHits;"
    c.execute(query)
    rows = c.fetchall()
    for d in rows:
        print('{} {} {} {} '.format(d[0], '-', d[1], 'views'))
    db.close()


def error_day():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    query = "select to_char(errorHits.date, 'FMMonth DD, YYYY')," \
            "cast(errorHits.errors as float) / cast(totalHits.results as " \
            " float) * 100 from totalHits, errorHits where totalHits.date" \
            "= errorHits.date AND errorHits.date = '2016-07-17';"
    c.execute(query)
    row = c.fetchall()
    for d in row:
        print('{} {} {}{} {}'.format(d[0], '-', round(d[1], 1), '%', 'errors'))
    row = c.fetchall()


print("What are the most popular three articles of all time?")
pop_article()
print("Who are the most popular article authors of all time?")
pop_auth()
print("On which days did more than 1% of requests lead to errors?")
error_day()
