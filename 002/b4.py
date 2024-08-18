import math

import numpy as np
from qiskit import QuantumCircuit


def solve(n: int) -> QuantumCircuit:
    qc = QuantumCircuit(n)
    for i in reversed(range(n)):
        qc.h(i)
        for qubit in reversed(range(0, i)):
            qc.cp(np.pi / 2 **(i - qubit), qubit, i)
    for i in range(math.floor(n / 2)):
        qc.swap(i, n - (i + 1))

    return qc
