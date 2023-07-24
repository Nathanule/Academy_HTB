import socket
import sys

class PortScanner:
    def __init__(self, target_ip):
        self.target_ip = target_ip

    def grab_banner(self, sock, port):
        try:
            # setting a timeout for banner grab attempt
            socket.setdefaulttimeout(3)

            if port == 80:
                #For port 80 (HTTP), send a basic HTTP GET request
                sock.send(b"GET / HTTP/1.1\r\nHost: %s\r\n\r\n" % self.target_ip.encode())
                banner = sock.recv(1024).decode().strip()
            
            else:

                # for other ports , attempt to recieve up to 1024 bytes of data from the socket
                banner = sock.recv(1024).decode().strip()
            return banner
        
        except socket.timeout:
            return "Banner not available Timeout error"
        except Exception as e:
            return f"error while attempting banner grab {e}"
        

    def scan_ports(self, ports):
        open_ports = {}
        for port in ports:
            try:
                # creating a socket object
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                # attempting to connect to the victim ip and port
                result = sock.connect_ex((self.target_ip, port))

                # if the connection was successful (port is open)
                if result == 0:
                    banner = self.grab_banner(sock, port)
                    open_ports[port] = banner

                # close the socket 
                sock.close()


            except KeyboardInterrupt:
                print("Port scanning halted by users")
                return open_ports
            except socket.gaierror:
                print("Host name couldn't resolve")
                return open_ports
            except socket.error:
                print('Not able to connect to server')
                return open_ports
        return open_ports
    
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('usage python3 port_scanner.py <target_ip> <port_range>')
        sys.exit(1)
    target_ip = sys.argv[1]
    port_range = sys.argv[2]

    # parse the port range
    start_port, end_port = map(int, port_range.split("-"))
    ports_to_scan = range(start_port, end_port + 1)

    scanner = PortScanner(target_ip)
    open_ports = scanner.scan_ports(ports_to_scan)

    if open_ports:
        print(f"Open ports on {target_ip}: ")
        for port, banner in open_ports.items():
            print(f"Port {port}: {banner}")
        else:
            print("No open ports found on target")
