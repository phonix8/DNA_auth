import random
import string

# Function to generate a random SNP sequence
def generate_snp_sequence(length=50):
    return ''.join(random.choice('ACGT') for _ in range(length))

# Function to generate a random secret message
def generate_secret_message(length=20):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

# Function to save SNP sequence and secret message to a file
def save_to_file(filename, snp_sequence, secret_message):
    with open(filename, 'w') as f:
        f.write(f"{snp_sequence}\n{secret_message}")

# Function to read SNP sequence and secret message from a file
def read_from_file(filename):
    with open(filename, 'r') as f:
        snp_sequence = f.readline().strip()
        secret_message = f.readline().strip()
    return snp_sequence, secret_message

# Function to authenticate user input
def authenticate(stored_sequence, user_input, threshold=0.9):
    if len(stored_sequence) != len(user_input):
        return False
    matches = sum(1 for a, b in zip(stored_sequence, user_input) if a == b)
    return (matches / len(stored_sequence)) >= threshold

# Main function to simulate the DNA authentication process
def main():
    filename = "dna_auth.txt"
    
    # Generate and save SNP sequence and secret message
    snp_sequence = generate_snp_sequence()
    secret_message = generate_secret_message()
    save_to_file(filename, snp_sequence, secret_message)
    print(f"Generated SNP sequence and secret message saved to {filename}")

    # Simulate authentication process
    stored_sequence, stored_secret = read_from_file(filename)
    print("\nSimulating DNA Authentication")
    print("==============================")
    
    attempts = 3
    while attempts > 0:
        user_input = input("Enter your SNP sequence: ")
        if authenticate(stored_sequence, user_input):
            print("Authentication successful!")
            print(f"Secret message: {stored_secret}")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Authentication failed. {attempts} attempts remaining.")
            else:
                print("Authentication failed. No more attempts.")

if __name__ == "__main__":
    main()
