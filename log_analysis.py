#!/usr/bin/env python3

import psycopg2

try:
    db = psycopg2.connect("dbname=news user=postgres")
except:
    print("Please check the database setup correctly."
          " Refer to readme.md for more information.")

cursor = db.cursor()

# This query gets the most popular articles of all times
cursor.execute(" SELECT articles.title, count(log.path)"
               " FROM articles"
               " JOIN log ON "
               " log.path=textcat(CAST('/article/' as text), articles.slug)"
               " WHERE status = '200 OK' GROUP BY articles.title"
               " ORDER BY count(log.path) DESC"
               " LIMIT 3;")

rows = cursor.fetchall()

print("The most viewed articles of all times were: ")
for row in rows:
    print("\"" + row[0] + "\"" + " - " + str(row[1]) + " views")

# This query gets the most popular authors of all times
cursor.execute(" SELECT auth.name, count(l.path)"
               " FROM log l INNER JOIN articles "
               " art ON l.path=textcat(CAST('/article/' as text), art.slug)"
               " INNER JOIN authors auth ON art.author = auth.id"
               " WHERE l.status = '200 OK'"
               " GROUP BY auth.name"
               " ORDER BY count(l.path) DESC "
               " LIMIT 3;")

rows = cursor.fetchall()

print("\nThe most viewed authors of all times were: ")
for row in rows:
    print("\"" + row[0] + "\"" + " - " + str(row[1]) + " views")

# This query returns on which days, more than 1% of requests led to errors
cursor.execute(" SELECT fail_count_data.time::DATE,"
               " fail_count_data.no_of_failures,"
               " fail_count_data.no_of_failures + successful.ok_call_counts"
               " as total"
               " FROM(SELECT TIME::DATE , count(*) as no_of_failures"
               " FROM log"
               " WHERE status != '200 OK'"
               " GROUP BY TIME::DATE) as fail_count_data,"
               " (SELECT TIME::DATE, count(*) as ok_call_counts"
               " FROM log"
               " WHERE status = '200 OK'"
               " GROUP BY TIME::DATE) as successful"
               " WHERE (fail_count_data.time = successful.time"
               " AND (fail_count_data.no_of_failures * 100) > "
               "(fail_count_data.no_of_failures + "
               " successful.ok_call_counts));")

rows = cursor.fetchall()

print("\nDays when more than 1% of requests led to errors: ")
for row in rows:
    percentage = (row[1]/row[2] * 100)
    print(str(row[0]) + " - " + "{0:.2f}".format(percentage) + "% errors")

db.close()
