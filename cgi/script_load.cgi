#!/bin/python2.7
import cgi
import cgitb
import subprocess
cgitb.enable();

def print_header():
    print ("""Content-type: text/html\n
    <!DOCTYPE html>
    <html>
    <body>""")

def print_close():
    print ("""</body>
    </html>""")


print_header();
user = subprocess.check_output("whoami",shell=True);
arguments = cgi.FieldStorage();
val = arguments['script'].value;
print val;
val = val.replace('<br>','\n');
f = open("file.bash","w");
subprocess.call(["echo",val],stdout=f);
f.close();
out = subprocess.check_output("sbatch file.bash; exit 0",stderr=subprocess.STDOUT,shell=True)
print out
print_close();
