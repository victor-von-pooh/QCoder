from qiskit import QuantumCircuit


def solve(n: int) -> QuantumCircuit:
    qc = QuantumCircuit(n)
    qc.h(0)

    for i in range(1, n):
        qc.cx((i - 1) // 2, i)
    
    qc.z(n - 1)

    return qc
