#!/usr/bin/env python

import sys
import os
import cgi
import cgitb; cgitb.enable()
import json
import MySQLdb

print "Content-Type: text/html"     # HTML is following
print                               	    # blank line, end of headers

# mysql DB schema:
# CREATE table tasks (id TEXT, url TEXT, project_id TEXT, project_url TEXT, project_name TEXT);

db = MySQLdb.connect(host='localhost',
                     user='eyzhao_trello',
                     passwd='m6CVrMh3ylTc',
                     db='eyzhao_trello_projects')

curs = db.cursor()

query = """
    DELETE FROM tasks
"""

curs.execute(query)

curs.execute('SELECT * FROM tasks')
for row in curs.fetchall():
    print(row)

db.close()
