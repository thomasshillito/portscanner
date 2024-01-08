import socket

def portScanner(host, start_port, end_port):
    # Make sure the end_port is inclusive
    end_port += 1
    for port in range(start_port, end_port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                s.connect((host, port))
                print(f"Port {port} is open")
        except Exception as e:
            print(f"Port {port} is closed or not responding: {e}")

# Asking user for input
host_to_scan = input("Enter the IP address to scan: ")
start_port = int(input("Enter the start port number: "))
end_port = int(input("Enter the end port number: "))

portScanner(host_to_scan, start_port, end_port)
