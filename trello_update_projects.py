#!/usr/bin/env python

import sys
import os
import cgi
#import cgitb; cgitb.enable()
import MySQLdb
import urllib3; urllib3.disable_warnings()
from trello import TrelloApi
from pprint import pprint
import json
import requests

print "Content-Type: text/html"     
print                               	    # blank line, end of headers

KEY = '88c2820ebbda50ae62ae526528372897'
TOKEN = 'd6dc0a0ae335155c03b7281fe69faa6925ab1d22c4e214ffe22959293749ce08'
PROJECT_CHECKLIST_NAME = 'Next Actions (automated)'

trello_params = {
    'token': TOKEN,
    'key': KEY
}

trello = TrelloApi(KEY)
trello.set_token(TOKEN)

board = trello.boards.get('57f98b2ec2956233649b0873')

db = MySQLdb.connect(host='localhost',
                     user='eyzhao_trello',
                     passwd='m6CVrMh3ylTc',
                     db='eyzhao_trello_projects')

curs = db.cursor()

#(id, project_id, project_url, project_name, board_id)
query = """
    SELECT * FROM tasks
"""
curs.execute(query)

trello.checklists.get('5772ebcfc0432dff14d70b55')

keys = ['task_id', 'project_id', 'project_url', 'project_name', 'board_id', 'task_url']
data_raw = [dict(zip(keys, row)) for row in curs.fetchall()]

print('Checking to ensure existence of all task-project pairs...')
data = []
for task in data_raw:
    try:
        trello.cards.get(task['task_id'])
        trello.cards.get(task['project_id'])
        data.append(task)
    except:
        print('Error processing task: {0} --- project {1}. One of them may not exist.'.format(task['task_url'], task['project_url']))

project_ids = set(task['project_id'] for task in data)
project_checklist_dict = {}

for project_id in project_ids:
    current_checklists = trello.cards.get_checklist(project_id)
    current_checklist_names = [checklist['name'] for checklist in current_checklists]
    if PROJECT_CHECKLIST_NAME in current_checklist_names:
        current_checklist_ids = [checklist['id'] for checklist in current_checklists]
        checklist_id = current_checklist_ids[current_checklist_names.index(PROJECT_CHECKLIST_NAME)]

        print('Deleting checklist for {0}'.format(project_id))
        requests.delete(
            'https://trello.com/1/checklists/{0}'.format(checklist_id),
            params = trello_params
        )

    print('Creating card for project: {0}'.format(project_id))
    checklist = requests.post(
        'https://trello.com/1/cards/{0}/checklists'.format(project_id),
        params = trello_params, 
        data = {
            'name': PROJECT_CHECKLIST_NAME
    }).json()

    project_checklist_dict[project_id] = checklist['id']

# Order cards by creation date
card_creation_dates = [trello.cards.get(task['task_id']).get('dateLastActivity') for task in data]
data = [task for (date, task) in sorted(zip(card_creation_dates, data))]

for task in data:
    project_id = task['project_id']
    checklist_id = project_checklist_dict[project_id]

    # Find the name of the list the card belongs to
    list_name = trello.cards.get_list(task['task_id']).get('name')

    print('Adding checkItem: {0} to project: {1}'.format(task['task_url'], task['project_url']))
    requests.post(
        'https://trello.com/1/checklists/{0}/checkItems'.format(checklist_id), 
        params = trello_params, 
        data = {
            'name': list_name.strip() + ': ' + task['task_url'],
            'pos': 'bottom',
            'checked': 'true' if list_name.lower().startswith('done') else 'false'
    }).json()
