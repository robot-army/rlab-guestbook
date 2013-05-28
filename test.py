from email.mime.text import MIMEText
from subprocess import Popen, PIPE
import re
import os
import time

while True:
  os.system('clear')
	name = ''
	address = ''
	line = 0
	f = open('text','r')
	for line in f:
		print line,	
	f.close()
	print('Please sign our guestbook')
	name = raw_input('Your name?\n')
	address = raw_input('Your email address?\n')
	while not re.match(r"[^@]+@[^@]+\.[^@]+", address):
		print("FAIL\n")
		address = raw_input('What yo email address?\n')
		


	msg = MIMEText("Address = %s, name = %s" % (address,name))
	msg["From"] = "bacon@rlab.org.uk"
	msg["To"] = "ry.white@gmail.com"
	msg["Subject"] = "This is the subject."
	p = Popen(["/usr/sbin/sendmail", "-t"], stdin=PIPE)
	p.communicate(msg.as_string())



        f = open('thanks','r')
        for line in f:
		time.sleep(0.1)
                print line,
	time.sleep(1)	
