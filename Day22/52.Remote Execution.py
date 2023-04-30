'''
import winrm

s = winrm.Session('127.0.0.1', auth=('arockia', 'neopolean'))
r = s.run_cmd('serverinfo')
#s.run_ps()
print(r.status_out)
'''

import paramiko

host = "127.0.0.1"
port = 22
username = "user"
password = "password"
command = "ls"
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)
stdin, stdout, stderr = ssh.exec_command(command)
print(stdout.readlines())