from qiskit import QuantumCircuit, QuantumRegister


def solve(n: int) -> QuantumCircuit:
    x, y = QuantumRegister(n), QuantumRegister(1)
    qc = QuantumCircuit(x, y)
    for i in range(n):
        qc.cx(i, n)

    return qc
