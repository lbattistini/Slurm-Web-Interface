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
	out = subprocess.check_output("scontrol show jobid -dd " + val,shell=True);
	out = out.replace('\n',"<br>");
except:
	out = "No job found with ID : "  + val;

print out;
