#!/usr/bin/python
import pexpect
import yaml

with open("credentials.yml", 'r') as ymlfile:
        phone = yaml.load(ymlfile)
lines = open('targetlist.txt').readlines()
print phone['user'], 
print phone['password'], 
for line in lines:
    target_phone = line.strip()
    spawned_cmd = "telnet {0}"
    spawned_cmd = spawned_cmd.format(target_phone)
    child = pexpect.spawn(spawned_cmd)
    child.logfile = open("/tmp/c3905_change.lc3905_change.log", "w")
    child.expect('login:')
    child.sendline(phone['user'])
    child.expect('password:')
    child.sendline(phone['password'])
    child.sendline('\r')
    child.expect('\$ ')
    child.sendline('set network vlan')
    child.expect('Admin Vlan Id.*:')
    child.sendline('62')
    child.expect('PC Admin Vlan Id.*:')
    child.sendline('\r')
    child.sendline('\r')
    child.expect('$')
    child.sendline('exit')
    child.close()
