# Quantum Surface Code & Error Correction Simulator

A high-performance Python simulation suite designed to model physical error syndromes in superconducting quantum architectures, implement rotated surface codes, and execute Minimum Weight Perfect Matching (MWPM) decoding for fault-tolerant quantum computing.

## 🔬 Theoretical Framework

### 1. Error Syndrome Extraction
Physical errors in transmon qubit arrays (such as $1/f$ flux noise and thermal relaxation) propagate as Pauli errors ($X, Z$) across the 2D lattice. Syndrome measurements project the state onto stabilizer generators:

$$S_s = \prod_{i \in s} Z_i \quad (\text{for Z-errors}), \quad S_x = \prod_{j \in x} X_j \quad (\text{for X-errors})$$

### 2. Minimum Weight Perfect Matching (MWPM)
To correct errors without destroying logical information, the syndrome graph is decoded using graph-theoretic matching algorithms to find the most probable error chains.

## 🛠️ Tech Stack
* **Python** (NumPy, SciPy, NetworkX)
* **Open-Source Quantum Simulation Frameworks**
