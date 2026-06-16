import socket
import platform
import getpass

print("=" * 50)
print("NETWORK INFORMATION SCANNER")
print("=" * 50)

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")
print(f"Operating System: {platform.system()}")
print(f"OS Version: {platform.release()}")
print(f"Current User: {getpass.getuser()}")

print("=" * 50)
print("SCAN COMPLETED")
print("=" * 50)