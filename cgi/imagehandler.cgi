#!/bin/python2.7
import cgi
import cgitb
import subprocess
import re
import base64

cgitb.enable();

def print_basics():
    print "Content-type: text/html\n"


print_basics();
arguments = cgi.FieldStorage();
imgdata = arguments['img'].value;
fh = open("prev_image.png", "wb")
fh.write(imgdata.decode('base64'))
fh.close()
subprocess.call("convert -resize 256x256\> prev_image.png -background none -gravity center -extent 256x256\> BMP3:prev_image.bmp",shell=True);
subprocess.call("rm -rf prev_image.png",shell=True);
print '''
	<script> 
		window.location.replace("../imagehandler.html");
	</script>
'''

	
