#!/usr/bin/env python
from backend import *
import cgi, cgitb

print ("Content-Type: text/html;charset=utf-8\r\n\r\n") 

form = cgi.FieldStorage()
fields = ["ps", "df", "finger", "uptime"]

daemon1 = []
daemon2 = []
daemon3 = []

for f in range(0, 4):
    for i in range(0, 4):
	if ("maq"+ str(f) + "_" + fields[i] in form):
	    value = form.getvalue("maq"+ str(f) + "-" + fields[i])
	    if(f == 1):
		daemon1.append(["maq"+ str(f) + "_" + fields[i], value])
	    elif(f == 2):
	        daemon2.append(["maq"+ str(f) + "_" + fields[i], value])	
	    elif(f == 3):
		daemon3.append(["maq"+ str(f) + "_" + fields[i], value])  






print "<h1>Solicitacoes</h1>"
print "<h4> Maquina 1 </h4>"
print (daemon1)
print "<h4> Maquina 2 </h4>"
print (daemon2)
print "<h4> Maquina 3 </h4>"
print (daemon3)
   
