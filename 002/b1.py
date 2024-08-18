from qiskit import QuantumCircuit


def solve(theta: float) -> QuantumCircuit:
    qc = QuantumCircuit(1)
    qc.rz(-2 * theta, 0)

    return qc
