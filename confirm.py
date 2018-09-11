#!/usr/bin/env python

import urllib2
import cgi
import cgitb
cgitb.enable()

inputs = cgi.FieldStorage()

#name = form['name'].value
#email = form['email'].value

print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers

print "<TITLE>Confirmation for Accreditation Site Visit</TITLE>"
print "<h1>Thank you for confirming your availability!</h1>"
print '''


'''
