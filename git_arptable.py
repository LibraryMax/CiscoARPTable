from netmiko import ConnectHandler
import os, errno

f = open('c:\out.txt', 'w')

cisco_2 = {
'device_type': 'cisco_ios',
'ip': '0.0.0.0',
'username': 'max',
'password': '****',
}

net_connect = ConnectHandler(**cisco_2)
output = net_connect.send_command("show arp")

print >> f, output
f.close()

bad_words = ['Incomplete', 'missing']

with open('c:\out.txt') as oldfile, open('c:\output.txt', 'w') as newfile:
    for line in oldfile:
        if any(bad_word in line for bad_word in bad_words):
            newfile.write(line)

with open("c:\output.txt") as f:
	print f.read()			

def silentRemove(filename):
    try:
        os.remove(filename)
    except OSError as e:
        if e.errno != errno.ENOENT: # errno.ENOENT = no such file or directory
            raise silentRemove(filename)
			
silentRemove('c:\out.txt')

raw_input("Hit enter to exit")