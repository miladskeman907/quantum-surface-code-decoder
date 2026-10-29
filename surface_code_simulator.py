import stim
import pymatching
import numpy as np

def run_surface_code_simulation(distance=3, rounds=3, p_noise=0.005, num_shots=10000):
    """
    Simulates a Surface Code circuit using Stim, extracts the Detector Error Model (DEM),
    samples syndromes with physical noise, and decodes using PyMatching to compute the logical error rate.
    """
    print(f"Building Surface Code Circuit: Distance d={distance}, Rounds={rounds}, Noise p={p_noise}")
    
    # 1. Generate surface code circuit using Stim's built-in circuit generator
    # surface_code: rotated_memory_z is standard for memory experiments
    circuit = stim.Circuit.generated(
        "surface_code:rotated_memory_z",
        distance=distance,
        rounds=rounds,
        after_clifford_depolarization=p_noise,
        before_measure_flip_probability=p_noise,
        after_reset_flip_probability=p_noise
    )
    
    # 2. Extract the Detector Error Model (DEM) and Logical Observables
    dem = circuit.detector_error_model(decompose_errors=True)
    
    # 3. Create a PyMatching decoder from the DEM
    matcher = pymatching.Matching.from_detector_error_model(dem)
    
    # 4. Sample syndrome measurements and logical observables from the noisy circuit
    sampler = circuit.compile_detector_sampler()
    syndrome_data, actual_observables = sampler.sample(num_shots, separate_observables=True)
    
    # 5. Predict logical errors using PyMatching MWPM decoder
    predicted_observables = matcher.decode_batch(syndrome_data)
    
    # 6. Calculate Logical Failure Rate
    num_failures = np.sum(np.any(predicted_observables != actual_observables, axis=1))
    failure_rate = num_failures / num_shots
    
    print(f"Simulation completed for {num_shots} shots.")
    print(f"Logical Failure Rate: {failure_rate:.5f} (Failures: {num_failures}/{num_shots})")
    
    return failure_rate

if __name__ == "__main__":
    run_surface_code_simulation()
