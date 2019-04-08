#!/bin/python2.7
import cgi
import cgitb
import subprocess
cgitb.enable();

def print_basics():
    print "Content-type: text/html\n"


print_basics();
arguments = cgi.FieldStorage();
val = arguments['id'].value;
try:
	f = open("file.bash.o"+val,"r");
	out = f.read();
	f.close();
	out = out.replace('\n',"<br>");
	f.close();
except:
	out = "file.bash.o" + val + ": file not found";
print out;
