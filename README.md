# Quantum Circuit Optimizer & Compilation Suite

A research-grade Python tool for optimizing quantum circuits, focusing on gate-level simplification, redundant CNOT cancellation, and circuit depth reduction to enhance fidelity on near-term quantum hardware (NISQ).

## 🔬 Core Features
- **Gate-Level Representation:** Manages quantum operations as structured computational objects.
- **CNOT Cancellation Engine:** Automatically detects and removes adjacent self-inverse CNOT gate pairs to reduce decoherence and error rates.
- **Circuit Metrics:** Tracks gate counts and depth optimization metrics.

## 🚀 Quick Start
Run the circuit optimizer locally:
```bash
python optimizer.py
