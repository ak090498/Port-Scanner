import subprocess
import re
from enum import Enum
class Ports(Enum):
    FTP = ":21"
    TELNET = ":23"
    SMB_DIRECT=":445"
    SMB_INDIRECT_1=":137"
    SMB_INDIRECT_2=":139" 
final_open_ports=[]
def search_open_ports():
    ports=[Ports['FTP'].value,Ports['TELNET'].value,Ports['SMB_DIRECT'].value,Ports['SMB_INDIRECT_1'].value,Ports['SMB_INDIRECT_2'].value]
    for i in range(0,len(ports)):
        print('Searching for port',ports[i])
        first = subprocess.run(['netstat', '-aon'],capture_output=True)
        full_command = subprocess.run(['findstr',ports[i]],input=first.stdout,capture_output=True)
        output = full_command.stdout.decode()
        pids = re.findall("[1-9]{1,}\r\n$",output)
        if(len(pids)!=0):
            pid_string=str(pids[0]).split("\r\n")
            final_pid_string="\\<"+pid_string[0]+"\\>"
            first = subprocess.run(['tasklist','/svc'],capture_output=True)
            full_command = subprocess.run(['findstr',final_pid_string],input=first.stdout,capture_output=True)
            output = full_command.stdout.decode()
            print('port',ports[i],'is open due to',output, 'is running')
            final_open_ports.append(Ports(ports[i]).name+":"+ports[i])
search_open_ports()                
print(final_open_ports)