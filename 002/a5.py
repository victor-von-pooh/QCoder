from qiskit import QuantumCircuit


def solve(n: int) -> QuantumCircuit:
    qc = QuantumCircuit(n)
    num_list = [0, 0, 1, 0, 1, 2, 3, 0, 1, 2, 3, 4, 5, 6]
    qc.h(0)
    for i in range(1, n):
        qc.cx(num_list[i - 1], i)
    qc.z(n - 1)

    return qc
