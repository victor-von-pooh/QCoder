from qiskit import QuantumCircuit
import numpy as np


def solve(n: int) -> QuantumCircuit:
    qc = QuantumCircuit(n)
    # Write your code here:
    prob_amp = np.sqrt(1 / n)
    rot_ang = 2 * np.arccos(prob_amp)

    qc.x(0)

    for i in range(n - 1):
        comp_amp = np.sqrt(1 - i / n)
        rot_ang = 2 * np.arccos(prob_amp / (comp_amp))
        qc.cry(rot_ang, i, i + 1)
        qc.cx(i + 1, i)

    return qc
