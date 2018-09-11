#!/usr/bin/env python

import sys
import os
import cgi
import cgitb; cgitb.enable()
import json

print "Content-Type: text/html"     # HTML is following
print                               	    # blank line, end of headers

TRELLO_PROJECTS_JSON = '/home2/eyzhao/data/trello/projects.json'

arguments = cgi.FieldStorage()

if not os.path.isfile(TRELLO_PROJECTS_JSON):
    f = open(TRELLO_PROJECTS_JSON, 'w')
    f.write('{}')
    f.close()


print(arguments)
if 'command' in arguments:
    command = arguments['command'].value

    if command == 'write':

        #project_id = arguments['projectId'].value
        #project_name = arguments['projectName'].value
        #task_id = arguments['taskId'].value
        #task_url = arguments['taskUrl'].value

        request_body = sys.stdin.read()

        #trello_projects = json.loads(open(TRELLO_PROJECTS_JSON).read())
        #trello_projects[task_id] = {
        #    'taskId': task_id,
        #    'taskUrl': task_url,
        #    'projectId': project_id,
        #    'projectName': project_name
        #}

        #f = open(TRELLO_PROJECTS_JSON, 'w')
        #f.write(json.dumps(trello_projects))
        #f.close()

        print(request_body)
    elif command == 'read':
        trello_projects = json.loads(open(TRELLO_PROJECTS_JSON).read())
        print(trello_projects)
    elif command == 'clear':
        f = open(TRELLO_PROJECTS_JSON, 'w')
        f.write('{}')
        f.close()

else:
    print('Please issue a command via GET or POST')
