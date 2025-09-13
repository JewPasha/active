import sys
import socket
def main():
    if len(sys.argv) >= 2:
        options = sys.argv[1]
        if options == "--help":
            print(helptext)
            sys.exit(1)
    if len(sys.argv) < 5: 
        
        print("Usage: tinyscanner [OPTIONS] [HOST] -p [PORT]")
        sys.exit(1)
    if not sys.argv[3] == "-p":
        print("Usage: tinyscanner [OPTIONS] [HOST] [PORT]")
        print("Type `--help` for more information")
        sys.exit(1)
    host = sys.argv[2]
    port = make_list_of_ports(sys.argv[4])
    match options:
        case "-p":
            print("PORTRANGE, host:",host, ", port", port)
        case "-u":
            print("Host: "+host)
            print(UDP_check(host, port))
        case "-t":
            print("Host: "+host)
            print(TCP_check(host, port))
        case _:
            print("Usage: tinyscanner [OPTIONS] [HOST] [PORT]")
            print("Type `--help` for more information")
def TCP_check(host, ports):
    result = ""
    for port in range(ports[0], ports[1]+1):
        try:
            with socket.create_connection((host, port), timeout=1):
                result += "TCP port "+str(port)+" open\n"
        except (socket.timeout, ConnectionRefusedError):
            result += "TCP port "+str(port)+" closed\n"
    return result
        
def UDP_check(host, ports):
    result = ""
    for port in range(ports[0], ports[1]+1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            sock.connect((host, port))
            result += "UDP port "+str(port)+" open\n"
        except socket.error:
            result += "UDP port "+str(port)+" closed\n"
        finally:
            sock.close()
    return result
def make_list_of_ports(port):
    if "-" in port:
        port_range = port.split("-")
        if is_valid_port(port_range[0]) and is_valid_port(port_range[1]):
            port_range = list(map(int, port_range)) #convert array to int
            port_range.sort()
            return(port_range)
    else: #if no range is given
        if is_valid_port(port):
            return [int(port), int(port)]
    print("Port can be between 1 - 65535")
    sys.exit(1)
def is_valid_port(port):
    return port.isnumeric() and int(port) <= 65535
helptext = """
Welcome to tinyscanner v1.0.0
Usage: tinyscanner [OPTIONS] [HOST] -p [PORT]
Options:
  -p               Range of ports to scan
  -u               UDP scan
  -t               TCP scan
  --help           Show this message and exit.
"""
if __name__ == "__main__":
    main()
