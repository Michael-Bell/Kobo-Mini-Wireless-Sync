import getpass
import sys
import telnetlib
from ftplib import FTP
import glob
import time

print 'start'
HOST = "192.168.1.120"
ftp = FTP(HOST)   # connect to host, default port

ftp.login()               # user anonymous, passwd anonymous@

ftp.cwd("/mnt/onboard")
print 'Changed cwd'

for filename in glob.glob("*.epub"):
    print "uploading " + filename
    file = open(filename,'rb')                  # file to send
    ftp.storbinary('STOR ' + filename, file)     # send the file
    file.close()  

ftp.quit()
print 'closed ftp'

user = 'root'
print 'start update'
tn = telnetlib.Telnet(HOST)
time.sleep(0.1)
print 'telnet login'

tn.read_until("login: ")
time.sleep(0.1)
tn.write(user + "\n")
time.sleep(0.1)
tn.write("sh update.sh\n")
time.sleep(0.1)
print 'run update'

time.sleep(15)

tn.write("exit\n")


print 'done'