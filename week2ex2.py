import telnetlib
import time

TELNET_PORT=23
TELNET_TIMEOUT=6

def main():
    ip_addr='50.76.53.27'
    username='pyclass'
    password='88newclass'
    connection=telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    
    output1=connection.read_until('sername:', TELNET_TIMEOUT)
    connection.write(username + '\n')
    
    output2=connection.read_until('ssword:', TELNET_TIMEOUT)
    connection.write(password + '\n')
    
    connection.write('terminal length 0' + '\n')
    connection.write('show ip int brief' +  '\n')
    time.sleep(1)
    output=connection.read_very_eager()
    print output
    connection.close()

    

if __name__=="__main__":
        main()
