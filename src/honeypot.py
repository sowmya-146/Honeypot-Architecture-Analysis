"""
Honeypot System - Main Module
"""

import socket
import threading
import logging
import time
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s'
)

class Honeypot:
    def __init__(self, host='0.0.0.0', ports=[80, 8080]):
        self.host = host
        self.ports = ports
        self.logger = logging.getLogger('Honeypot')
    
    def start(self):
        self.logger.info("="*60)
        self.logger.info("HONEYPOT SYSTEM STARTED")
        self.logger.info(f"Host: {self.host}")
        self.logger.info(f"Ports: {self.ports}")
        self.logger.info("="*60)
        
        for port in self.ports:
            thread = threading.Thread(
                target=self.start_listener,
                args=(port,)
            )
            thread.daemon = True
            thread.start()
            self.logger.info(f"[+] Listening on port {port}")
        
        self.logger.info("\n[*] Honeypot running. Press Ctrl+C to stop.\n")
        
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.logger.info("\n[!] Shutting down...")
    
    def start_listener(self, port):
        try:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server.bind((self.host, port))
            server.listen(5)
            
            while True:
                client, addr = server.accept()
                self.logger.info(f"[*] Connection from {addr[0]}:{addr[1]}")
                client.close()
        except Exception as e:
            self.logger.error(f"Error on port {port}: {e}")

def main():
    honeypot = Honeypot()
    honeypot.start()

if __name__ == "__main__":
    main()
