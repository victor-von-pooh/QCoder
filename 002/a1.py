from qiskit import QuantumCircuit


def solve() -> QuantumCircuit:
    qc = QuantumCircuit(1)
    qc.x(0)
    qc.z(0)
    qc.x(0)

    return qc
