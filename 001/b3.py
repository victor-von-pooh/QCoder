from qiskit import QuantumCircuit
from qiskit.circuit.library import ZGate


def solve(n: int, L: int) -> QuantumCircuit:
    qc = QuantumCircuit(n)
    if L == 1:
        for i in range(n):
            qc.h(i)
        qc.append(ZGate().control(n - 1), range(n))
        for i in range(n):
            qc.x(i)
    elif L == [2 ** i for i in range(1, n + 1)]:
        qc.z(n - 1)
        qc.x(n - 1)

    return qc