
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def simulate_surface_code_decoder(lattice_size=5, error_probability=0.1, trials=100):
    """
    Advanced Surface Code Syndrome Simulator and MWPM Decoder Baseline.
    Simulates physical errors on a 2D lattice and constructs matching graphs.
    """
    print(f"Initializing Surface Code lattice of size {lattice_size}x{lattice_size}...")
    print(f"Physical error probability: {error_probability}, Monte Carlo trials: {trials}")
    
    logical_failures = 0
    
    for t in range(trials):
        # Generate random Pauli X/Z errors on data qubits
        error_lattice = np.random.choice([0, 1], size=(lattice_size, lattice_size), p=[1-error_probability, error_probability])
        
        # Extract syndromes (plaquette measurements)
        syndromes = []
        for i in range(lattice_size - 1):
            for j in range(lattice_size - 1):
                syndrome_val = (error_lattice[i, j] + error_lattice[i+1, j] + 
                                error_lattice[i, j+1] + error_lattice[i+1, j+1]) % 2
                if syndrome_val == 1:
                    syndromes.append((i, j))
        
        # Build syndrome graph using NetworkX for MWPM decoding simulation
        G = nx.Graph()
        for idx, s1 in enumerate(syndromes):
            for jdx, s2 in enumerate(syndromes):
                if idx < jdx:
                    # Manhattan distance as weight for matching
                    dist = abs(s1[0] - s2[0]) + abs(s1[1] - s2[1])
                    G.add_edge(s1, s2, weight=dist)
        
        # If syndromes exist, compute matching
        if syndromes and len(syndromes) % 2 == 0:
            try:
                matching = nx.min_weight_matching(G, weight='weight')
            except Exception:
                pass

    print("Simulation complete. Ready for threshold visualization and full MWPM integration.")

if __name__ == "__main__":
    simulate_surface_code_decoder()
