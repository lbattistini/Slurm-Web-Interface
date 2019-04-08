#!/bin/python2.7
import cgi
import cgitb
import subprocess
cgitb.enable();

def print_basics():
	print "Content-type: text/html\n"

print_basics()

user = subprocess.check_output("whoami",shell=True);
arguments = cgi.FieldStorage();
val = arguments['script'].value;
val = val.replace('<br>','\n');
f = open("file.bash","w");
subprocess.call(["echo",val],stdout=f);
f.close();
ret = subprocess.check_output("sbatch file.bash; exit 0",stderr=subprocess.STDOUT,shell=True)
if(ret.find("error") != -1):
	print "no job submitted"

else :
	ret = ret.replace(" ","");
	ret = ret.split("job")[1];
	print ret;
