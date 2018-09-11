#!/usr/bin/env python

import sys
import os
import cgi
import cgitb; cgitb.enable()
import json
import MySQLdb

print "Content-Type: text/html"     # HTML is following
print                               	    # blank line, end of headers

request_body = sys.stdin.read()
request = json.loads(request_body)

task_id = request['taskId']
task_url = request['taskUrl']
project_name = request['projectName']
project_id = request['projectId']
project_url = 'https://trello.com/c/' + request['projectId']
board_id = request['boardId']

db = MySQLdb.connect(host='localhost',
                     user='eyzhao_trello',
                     passwd='m6CVrMh3ylTc',
                     db='eyzhao_trello_projects')

curs = db.cursor()

query = """
    INSERT INTO tasks 
        (id, task_url, project_id, project_url, project_name, board_id)
    VALUES (%s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
        task_url        = VALUES(task_url),
        project_id      = VALUES(project_id),
        project_url     = VALUES(project_url),
        project_name    = VALUES(project_name),
        board_id        = VALUES(board_id);
"""

curs.execute(query, (task_id, task_url, project_id, project_url, project_name, board_id))

curs.execute('SELECT * FROM tasks')

db.close()
