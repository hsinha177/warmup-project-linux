#! /usr/bin/python3

import cgi	#for connecting webpage
import cgitb	#for gathering any error info
import mysql.connector	#mysql connection

cgitb.enable() 		#gathering error info

print("Content-type:text/html")	#information about the type of content it will read
print("")

webdata=cgi.feildStorage()	#creating  object for reading

eid=webdata.getvalue("email")	#fetching email from input variable
paswd=webdata.getvalue("pwd")	#fetching password from input variable
paswd2=webdata.getvalue("pwd-repeat")

if paswd==paswd2 :
	conn = mysql.connector.connect(host='localhost',user='root',passwd='root',database='reko')	#establishing connection with server
	mycursor=conn.cursor()
	mycursor.execute("select email from user where email='%s'"%(eid))
	usercheck=mycursor.fetchone()
	mycursor2=conn.cursor()
	mycursor2.execute("select pass from user where pass='%s'"%(paswd))
	passcheck=mycursor2.fetchone()
	try:
		if eid == usercheck[0] and paswd == passcheck[0]:
        		print("<meta http-equiv='refresh' content='1;url=https://13.233.28.221/facerecon.html'>")
	except :
		print ("sorry")
	conn.commit()
	conn.close()
else:
	print("Password doesn't match. Try again!")
	print("<meta http-equiv='refresh' content='3;url=https://13.233.28.221/new_account.html'>")
