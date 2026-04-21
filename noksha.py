import socket
import os
import sys
import time

# Matrix green terminal style
os.system('color 0A')

def print_ascii_art():
    art = '''
       ___   __    _  _______  _______  _______  _______  _______  
      |   | |  |  | ||   _   ||   _   ||   _   ||   _   ||   _   |
      |   | |  |  | ||  | |  ||  |_|  ||  | |  ||  |_|  ||  |_|  |
      |   | |  |  | ||  |_|  ||       ||  | |  ||       ||       |
      |   | |  |__| ||       ||       ||  |_|  ||       ||       |
      |   | |   __  ||       ||   _   ||       ||   _   ||   _   |
      |___| |__|  |__||_______||__| |__||_______||__| |__||__| |__|
    '''
    print(art)

# Port scanning function
def port_scan(target, ports):
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        if sock.connect_ex((target, port)) == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

# Password checking function (dummy example)
def check_password(password):
    # In a real scenario, check against hashed passwords
your_password = 'h4ck3r'
    return password == your_password

# Network analysis function
def analyze_network(target):
    print(f'Analyzing network for: {target}')
    # Insert network analysis code here
    # This is where you'd implement actual network analysis

if __name__ == '__main__':
    print_ascii_art()
    target = input('Enter target IP: ')
    ports = range(1, 1025)  # Scanning first 1024 ports
    print(f'Scanning ports on {target}...')
    open_ports = port_scan(target, ports)
    if open_ports:
        print(f'Open ports: {open_ports}')
    else:
        print('No open ports found.')

    password = input('Enter password to check: ')
    if check_password(password):
        print('Access granted!')
    else:
        print('Access denied!')

    analyze_network(target)
    time.sleep(2)
