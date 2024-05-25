import os
import http.server
import socketserver
import socket

def print_files():
    directory = os.fsencode("jpg/")
        
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        print('<a href="jpg/'+filename+'">'+filename+'</a><img src="jpg/'+filename+'"><br>')



PORT = 8000
DIRECTORY = "."

class CustomRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

# Function to get the local IP address
def get_local_ip():
    try:
        # Connect to an external server to determine local IP address
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0)
        s.connect(('8.8.8.8', 1))
        IP = s.getsockname()[0]
        s.close()
    except Exception:
        IP = '127.0.0.1'
    return IP

local_ip = get_local_ip()

with socketserver.TCPServer((local_ip, PORT), CustomRequestHandler) as httpd:
    print(f"Serving HTTP on http://{local_ip}:{PORT}/")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
