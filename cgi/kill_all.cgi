#!/bin/python2.7
import cgi
import cgitb
import subprocess

cgitb.enable();

def print_basics():
   print "Content-type: text/html\n"

def kill_all(jobs):
	lines = jobs.split('\n');
	IDs = [];
	for line in lines[1:len(lines)] :
		line = line + "<br>"
		IDs.append(line.split('_')[0]);
	for ID in IDs:
		subprocess.call("scancel " + ID,shell=True);

print_basics()
name = subprocess.check_output("whoami").replace('\n',"");
command = "squeue -o '%.10i %9P %8j %18u %2t %.11M %.11l %.5D %.4C %.10m %16R '";
jobs =  subprocess.check_output(command,shell=True,executable="/bin/bash")

if(jobs.find(name) != -1):
	kill_all(jobs);
else :
	print "No killable jobs found for you!"
