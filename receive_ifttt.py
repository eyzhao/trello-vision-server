#!/usr/bin/env python

import urllib2
import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()

switch = False
if 'ifttt' in form:
	if form['ifttt'].value == 'pressed':
		urllib2.urlopen('https://maker.ifttt.com/trigger/flick-switch/with/key/cSsWmbBgXO0gj9K216ZaU_')
		switch = True

print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers

print "<TITLE>CGI script output</TITLE>"
print "<H1>This is my first CGI script</H1>"
print "Hello, world!"
print '''

<form method='post' action='https://maker.ifttt.com/trigger/flick-switch/with/key/cSsWmbBgXO0gj9K216ZaU_'>
	<input type = 'submit' value='button' />
</form>

'''

if switch:
	print 'it worked!'
