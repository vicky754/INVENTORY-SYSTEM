#!python
# print("content-type: text/html\r\n\r\n")

import cgi
fd=cgi.FieldStorage()
line_name=fd.getvalue("lname")
ref_no=fd.getvalue("ref")
in_date=fd.getvalue("indate")
container_no=fd.getvalue("container")
size=fd.getvalue("size")
type=fd.getvalue("type")
transporter_name=fd.getvalue("transporter")
vehicle_number=fd.getvalue("vehicle")
come_from=fd.getvalue("from")
party_name=fd.getvalue("party")
valid_date=fd.getvalue("vdate")
cash_collection=fd.getvalue("cash")
remark=fd.getvalue("remark")



import pymysql
db=pymysql.connect("localhost","root","","alpha")
cursor=db.cursor()
query="INSERT INTO alphain(line_name,ref_no,in_date,container_no,size,type,transporter_name,vehicle_number,come_from,party_name,valid_date,cash_collection,remark) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(line_name,ref_no,in_date,container_no,size,type,transporter_name,vehicle_number,come_from,party_name,valid_date,cash_collection,remark)
try:
    cursor.execute(query)
    db.commit()
    # print("successfull !!!")
    print("Location: http://localhost/cgi-bin/alpha/alphainform.py\r\n\r\n")
except:
    db.rollback()
    print("error occored")













