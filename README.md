# DNA Sequencing Simulation

This project provides a Python-based simulation of the DNA sequencing process. It's designed to demonstrate the basic concepts of DNA sequencing, including genome generation, fragmentation, error simulation, and sequence assembly.

## Features

- Generate a sample genome of customizable length
- Fragment the DNA into smaller, overlapping pieces
- Simulate sequencing errors
- Assemble the genome from fragmented pieces
- Calculate assembly accuracy
- Analyze base pair frequencies
- Save original and assembled genomes to files
- Interactive command-line interface
- Includes a CPU-intensive task for performance testing

## Requirements

- Python 3.6 or higher

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/dna-sequencing-simulation.git
   ```
2. Navigate to the project directory:
   ```
   cd dna-sequencing-simulation
   ```

## Usage

Run the simulation using Python:

```
python enhanced_dna_sequencing_simulation.py
```

Follow the on-screen prompts to progress through each stage of the simulation.
### DNA Authentication System

1. Start the server:
   ```
   python dna_auth_server.py
   ```
2. Connect the Arduino Pro Micro to your computer.
3. Run the client:
   ```
   python dna_auth_client.py
   ```

The client will read the DNA sequence from the Arduino and attempt to authenticate with the server.

# Add DNA Authentication System

This pull request adds a DNA-based authentication system to our existing DNA sequencing simulation project. The new system demonstrates how DNA sequences could potentially be used for authentication purposes in a simplified manner.

## New Files Added

1. `dna_auth_server.py`: A server script that authenticates DNA sequences.
2. `dna_auth_client.py`: A client script that reads DNA sequences from an Arduino and authenticates with the server.
3. `arduino_dna_storage.ino`: An Arduino script for storing and providing DNA sequences.

## Changes to Existing Files

- `README.md`: Updated to include information about the new DNA authentication system.

## Features Added

- Server-client authentication system using DNA sequences
- Integration with Arduino for DNA sequence storage
- Demonstration of how biological data could be used in cybersecurity contexts

## How to Test

1. Upload the `arduino_dna_storage.ino` script to an Arduino Pro Micro.
2. Start the server by running `python dna_auth_server.py`.
3. Connect the Arduino to your computer and run `python dna_auth_client.py`.
4. Verify that the authentication process completes successfully.

## Notes

- This system is a simplified demonstration and should not be used for actual security purposes.
- The DNA sequence used for authentication is hardcoded for demonstration purposes. In a real system, this would be securely stored and possibly dynamically generated.

Please review and let me know if any changes are needed!

## Output

- The DNA sequencing simulation will generate two text files:
  - `original_genome.txt`: Contains the originally generated genome sequence
  - `assembled_genome.txt`: Contains the assembled genome sequence after fragmentation and reassembly

- The DNA authentication system will print the authentication result to the console.

## Contributing

We welcome contributions to improve the DNA Sequencing Simulation! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) file for details on how to contribute.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project is for educational purposes and simulates a simplified version of actual DNA sequencing processes.
- Inspired by real-world genomics and bioinformatics challenges.
