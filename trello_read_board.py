#!/usr/bin/env python

import sys
import os
import cgi
import cgitb; cgitb.enable()
import json
import MySQLdb

print "Content-Type: application/json"     
print                               	    # blank line, end of headers

arguments = cgi.FieldStorage()

# mysql DB schema:
# CREATE table tasks (id VARCHAR(255), url TEXT, project_id TEXT, project_url TEXT, project_name TEXT);

request_body = sys.stdin.read()
# {u'projectId': u'321', u'command': u'write', u'taskUrl': u'arst', u'taskId': u'wowitworks', u'projectName': u'testproject2'}

board_id = arguments['boardId'].value

db = MySQLdb.connect(host='localhost',
                     user='eyzhao_trello',
                     passwd='m6CVrMh3ylTc',
                     db='eyzhao_trello_projects')

curs = db.cursor()

query = """
    SELECT *
    FROM tasks
    WHERE (board_id = %s)
"""

curs.execute(query, (board_id))

results_table = curs.fetchall()

json_dictionary = [{
    'taskId': result[0],
    'taskUrl': result[5],
    'projectId': result[1],
    'projectUrl': result[2],
    'projectName': result[3],
    'boardId': result[4],
} for result in results_table]

db.close()

print(json.dumps(json_dictionary))

