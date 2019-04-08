#!/bin/python2.7
import cgi
import cgitb
import subprocess

cgitb.enable();

def print_basics():
    print "Content-type: text/html\n"

print_basics();
command = "squeue -o '%.10i %9P %8j %18u %2t %.11M %.11l %.5D %.4C %.10m %16R '";

queue = subprocess.check_output(command,shell=True,executable="/bin/bash")
lines = queue.split('\n');

for line in lines[1:len(lines)]:
	print line
