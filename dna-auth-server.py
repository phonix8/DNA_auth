import socket
import threading

# Predefined DNA sequence for authentication
AUTH_DNA_SEQUENCE = "ATCGATCGATCGATCGATCG"  # This should be a more complex sequence in a real scenario
SECRET_MESSAGE = "Access granted. Server and client connection established."

def handle_client(client_socket):
    # Receive the DNA sequence from the client
    dna_sequence = client_socket.recv(1024).decode()
    
    # Authenticate the DNA sequence
    if dna_sequence == AUTH_DNA_SEQUENCE:
        response = SECRET_MESSAGE
    else:
        response = "Authentication failed."
    
    # Send the response back to the client
    client_socket.send(response.encode())
    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 9999))
    server.listen(5)
    print("[*] Listening on 0.0.0.0:9999")

    while True:
        client, addr = server.accept()
        print(f"[*] Accepted connection from: {addr[0]}:{addr[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
