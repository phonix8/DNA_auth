import random
import time
from collections import Counter
import os

# Constants
BASES = ['A', 'C', 'G', 'T']
GENOME_LENGTH = 10_000_000  # 10 million base pairs for this simulation

def generate_genome(length):
    """Generate a random genome sequence."""
    return ''.join(random.choice(BASES) for _ in range(length))

def fragment_dna(genome, fragment_size=100, overlap=20):
    """Fragment the DNA into smaller, overlapping pieces."""
    fragments = []
    for i in range(0, len(genome) - fragment_size + 1, fragment_size - overlap):
        fragments.append(genome[i:i+fragment_size])
    return fragments

def simulate_sequencing_errors(fragments, error_rate=0.01):
    """Simulate sequencing errors in the fragments."""
    for i in range(len(fragments)):
        fragment = list(fragments[i])
        for j in range(len(fragment)):
            if random.random() < error_rate:
                fragment[j] = random.choice(BASES)
        fragments[i] = ''.join(fragment)
    return fragments

def assemble_genome(fragments, min_overlap=20):
    """Assemble the genome from fragments using a simple overlap-layout-consensus approach."""
    assembled = fragments[0]
    used_fragments = set([0])

    while len(used_fragments) < len(fragments):
        best_overlap = 0
        best_fragment = None
        best_index = None

        for i, fragment in enumerate(fragments):
            if i in used_fragments:
                continue

            for overlap in range(min_overlap, len(fragment)):
                if assembled.endswith(fragment[:overlap]):
                    if overlap > best_overlap:
                        best_overlap = overlap
                        best_fragment = fragment
                        best_index = i

        if best_fragment is None:
            break

        assembled += best_fragment[best_overlap:]
        used_fragments.add(best_index)

    return assembled

def calculate_accuracy(original, assembled):
    """Calculate the accuracy of the assembled genome."""
    return sum(a == b for a, b in zip(original, assembled)) / len(original)

def save_to_file(filename, content):
    """Save content to a file."""
    with open(filename, 'w') as f:
        f.write(content)

def cpu_intensive_task(iterations=1000000):
    """Perform a CPU-intensive task."""
    result = 0
    for i in range(iterations):
        result += i * i
    return result

def main():
    print("Starting Enhanced DNA Sequencing Simulation")
    print("===========================================")

    # Step 1: Generate a sample genome
    print("Generating sample genome...")
    start_time = time.time()
    original_genome = generate_genome(GENOME_LENGTH)
    print(f"Sample genome generated. Length: {len(original_genome)} base pairs")
    print(f"Time taken: {time.time() - start_time:.2f} seconds")

    # Save original genome to file
    save_to_file("original_genome.txt", original_genome)
    print("Original genome saved to 'original_genome.txt'")

    # Display a portion of the genome
    print(f"\nFirst 100 base pairs of the genome: {original_genome[:100]}")
    
    input("\nPress Enter to continue to DNA fragmentation...")

    # Step 2: Fragment the DNA
    print("\nFragmenting DNA...")
    start_time = time.time()
    fragments = fragment_dna(original_genome)
    print(f"DNA fragmented into {len(fragments)} pieces")
    print(f"Time taken: {time.time() - start_time:.2f} seconds")

    # Display some fragments
    print("\nFirst 5 fragments:")
    for i, fragment in enumerate(fragments[:5]):
        print(f"Fragment {i+1}: {fragment}")

    input("\nPress Enter to continue to error simulation...")

    # Step 3: Simulate sequencing errors
    print("\nSimulating sequencing errors...")
    start_time = time.time()
    fragments_with_errors = simulate_sequencing_errors(fragments)
    print("Sequencing errors simulated")
    print(f"Time taken: {time.time() - start_time:.2f} seconds")

    # Display some fragments with errors
    print("\nFirst 5 fragments with potential errors:")
    for i, fragment in enumerate(fragments_with_errors[:5]):
        print(f"Fragment {i+1}: {fragment}")

    input("\nPress Enter to continue to genome assembly...")

    # Step 4: Assemble the genome
    print("\nAssembling genome...")
    start_time = time.time()
    assembled_genome = assemble_genome(fragments_with_errors)
    print(f"Genome assembled. Length: {len(assembled_genome)} base pairs")
    print(f"Time taken: {time.time() - start_time:.2f} seconds")

    # Save assembled genome to file
    save_to_file("assembled_genome.txt", assembled_genome)
    print("Assembled genome saved to 'assembled_genome.txt'")

    # Step 5: Calculate accuracy
    print("\nCalculating accuracy...")
    accuracy = calculate_accuracy(original_genome, assembled_genome)
    print(f"Assembly accuracy: {accuracy:.2%}")

    # Step 6: Analyze base pair frequencies
    print("\nAnalyzing base pair frequencies:")
    original_freq = Counter(original_genome)
    assembled_freq = Counter(assembled_genome)
    for base in BASES:
        print(f"{base}: Original: {original_freq[base]}, Assembled: {assembled_freq[base]}")

    input("\nPress Enter to start CPU-intensive task...")

    # Step 7: CPU-intensive task
    print("\nPerforming CPU-intensive task...")
    start_time = time.time()
    cpu_intensive_task()
    print(f"CPU-intensive task completed. Time taken: {time.time() - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
