from qiskit import QuantumCircuit


def solve() -> QuantumCircuit:
    qc = QuantumCircuit(1)
    # Write your code here:
    qc.y(0)

    return qc
