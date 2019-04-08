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
val = val.split('_')[0];

print val

subprocess.call("scancel " + val,shell=True);
