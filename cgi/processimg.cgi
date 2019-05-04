#!/bin/python2.7
import cgi
import cgitb
import subprocess
cgitb.enable();

def print_basics():
    print "Content-type: text/html\n"


print_basics();
try:
	subprocess.call("./work_on_image.sh prev_image.bmp",shell=True);
	print "ok"
except:
	print "err"

