#!/bin/python2.7
import cgi
import cgitb
import subprocess
import re

cgitb.enable();

def print_basics():
    print "Content-type: text/html\n"


print_basics();
arguments = cgi.FieldStorage();
val = arguments['id'].value;

try:
	out = subprocess.check_output("scontrol show jobid -dd " + val,shell=True);
	out = out.split('\n') [3];
	out = out.split("State=")[1];
	out = out.split(' ')[0];
except: 
	print "NOTFOUND"
	
print out;
