import numpy as np

class QuantumGate:
    def __init__(self, name, qubits, params=None):
        self.name = name          # e.g., 'CNOT', 'RZ', 'H'
        self.qubits = qubits      # tuple or list of qubit indices (e.g., (0, 1) or (0,))
        self.params = params      # parameters for rotation gates (e.g., angle)

    def __repr__(self):
        return f"Gate({self.name}, qubits={self.qubits}, params={self.params})"


class QuantumCircuitOptimizer:
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.gates = []

    def add_gate(self, name, qubits, params=None):
        self.gates.append(QuantumGate(name, qubits, params))

    def optimize_cnot_cancellation(self):
        """
        Optimizes the circuit by cancelling adjacent self-inverse CNOT gates.
        Since CNOT * CNOT = Identity, consecutive identical CNOT gates can be removed.
        """
        print(f"Running CNOT Cancellation on circuit with {len(self.gates)} initial gates...")
        optimized_gates = []
        i = 0
        while i < len(self.gates):
            current_gate = self.gates[i]
            # Check if there is a next gate and if both are CNOTs acting on the exact same control/target qubits
            if i + 1 < len(self.gates) and current_gate.name == 'CNOT' and self.gates[i+1].name == 'CNOT':
                if current_gate.qubits == self.gates[i+1].qubits:
                    # Cancel both gates (they annihilate each other)
                    print(f"Optimized: Removed redundant CNOT pair on qubits {current_gate.qubits}")
                    i += 2
                    continue
            optimized_gates.append(current_gate)
            i += 1
            
        self.gates = optimized_gates
        print(f"Optimization complete. Final gate count: {len(self.gates)}")
        return self.gates

    def get_circuit_depth(self):
        """
        Estimates the rough depth of the quantum circuit.
        """
        return len(self.gates)


if __name__ == "__main__":
    # Test the optimizer with a sample circuit containing redundant CNOTs
    qc = QuantumCircuitOptimizer(num_qubits=3)
    qc.add_gate('H', (0,))
    qc.add_gate('CNOT', (0, 1))
    qc.add_gate('CNOT', (0, 1))  # Redundant pair (should be removed)
    qc.add_gate('RZ', (1,), params=np.pi/4)
    qc.add_gate('CNOT', (1, 2))
    qc.add_gate('CNOT', (1, 2))  # Redundant pair (should be removed)
    
    print("--- Before Optimization ---")
    print(f"Total Gates: {len(qc.gates)}")
    
    qc.optimize_cnot_cancellation()
    
    print("\n--- After Optimization ---")
    print(f"Total Gates: {len(qc.gates)}")
