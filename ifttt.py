#!/usr/bin/env python
print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers

print "<TITLE>CGI script output</TITLE>"
print "<H1>This is my first CGI script</H1>"
print "Hello, world!"
print '''

<form method='post' action='https://maker.ifttt.com/trigger/button-pressed/with/key/cSsWmbBgXO0gj9K216ZaU_'>
	<input type = 'submit' value='button' />
</form>

'''
