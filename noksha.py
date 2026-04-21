import socket
import string
import random

# Port Scanning Function

def port_scan(target, ports):
    open_ports = []
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
    return open_ports

# Password Strength Checker

def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."
    if not any(char.isdigit() for char in password):
        return "Weak: Password must contain at least one digit."
    if not any(char.isupper() for char in password):
        return "Weak: Password must contain at least one uppercase letter."
    if not any(char in string.punctuation for char in password):
        return "Weak: Password must contain at least one special character."
    return "Strong: Password meets all requirements."

# Network Analysis Function

def analyze_network(target):
    open_ports = port_scan(target, range(1, 1025))
    return open_ports

# Example Usage
if __name__ == '__main__':
    target_ip = '127.0.0.1'
    print(f'Open ports on {target_ip}: {analyze_network(target_ip)}')

    password = 'Example@123'
    print(check_password_strength(password))