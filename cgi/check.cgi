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
	out = subprocess.check_output("squeue -j " + val + " -o %t",shell=True);
	out = out.split('\n')[1];
except:
	#NE = Not Exists
	out = "NE" 

if(len(out) == 0):
	out = "NE"

print out;
