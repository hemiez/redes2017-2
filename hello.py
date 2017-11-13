#!/usr/bin/env python

import cgi
import cgitb
cgitb.enable()
    
print("Content-Type: text/html;charset=utf-8\r\n\r\n")

form = cgi.FieldStorage()

print (form)
