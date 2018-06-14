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


print("Question 1:")
pop_article()
print("Question 2:")
pop_auth()
print("Question 3:")
error_day()




