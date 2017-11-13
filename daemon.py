import cgi, cgitb

print ("Content-Type: text/html;charset=utf-8\r\n\r\n") 

form = cgi.FieldStorage()
fields = ["ps", "df", "finger", "uptime"]
