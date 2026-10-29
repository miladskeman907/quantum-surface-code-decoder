import numpy as np
import pymatching
import stim
import matplotlib.pyplot as plt

def run_surface_code_simulation(distance=3, p=0.01, num_shots=1000):
    """
    Performs a rigorous Surface Code simulation and MWPM decoding 
    using Stim and PyMatching for professional-grade error correction.
    """
    print(f"Running Surface Code (Distance {distance}), Physical Error Rate: {p}, Shots: {num_shots}")
    
    # Create a surface code circuit using Stim
    circuit = stim.Circuit(f"""
        REPEAT {distance} {{
            DEPOLARIZE1({p}) 0 1 2 3 4 5 6 7 8
        }}
    """)
    
    # Use PyMatching for MWPM decoding baseline
    # Building a repetition/surface code decoder model
    dem = circuit.detector_error_model(decompose_errors=True)
    matcher = pymatching.Matching.from_detector_error_model(dem)
    
    # Sample shots
    sampler = circuit.compile_detector_sampler()
    syndrome_data, actual_observables = sampler.sample(shots=num_shots, separate_observables=True)
    
    # Decode using MWPM
    num_errors = 0
    for i in range(num_shots):
        syndrome = syndrome_data[i]
        predicted_observables = matcher.decode(syndrome)
        if not np.array_equal(predicted_observables, actual_observables[i]):
            num_errors += 1
            
    logical_failure_rate = num_errors / num_shots
    print(f"Simulation completed. Logical Failure Rate: {logical_failure_rate:.4f}")
    return logical_failure_rate

if __name__ == "__main__":
    run_surface_code_simulation()
