import socket
import serial
import time

def read_dna_from_arduino():
    # Establish serial connection with Arduino
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    time.sleep(2)  # Wait for the connection to establish

    # Request DNA sequence from Arduino
    ser.write(b'GET_DNA')
    
    # Read the response
    dna_sequence = ser.readline().decode().strip()
    ser.close()
    return dna_sequence

def authenticate_with_server(dna_sequence):
    # Connect to the server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 9999))  # Replace with server IP if not on localhost

    # Send the DNA sequence
    client.send(dna_sequence.encode())

    # Receive the response
    response = client.recv(1024).decode()
    client.close()

    return response

def main():
    # Read DNA sequence from Arduino
    dna_sequence = read_dna_from_arduino()
    print(f"DNA sequence read from Arduino: {dna_sequence}")

    # Authenticate with server
    response = authenticate_with_server(dna_sequence)
    print(f"Server response: {response}")

if __name__ == "__main__":
    main()
