import socket
import sys

ports = [23,21,137,139,445]

if(len(sys.argv)==1):
    print('No argumenets provided')
else:    
    ip=sys.argv[1] 
    for i in range(0,len(ports)):
        try:
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((ip,ports[i]))
            print('port',ports[i],'is open')
            s.close()
        except ConnectionRefusedError:
            print('port',ports[i],'is closed, hence connection refused')
        except PermissionError:
            print('port is open however permission is denied')        
           