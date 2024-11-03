from qiskit import QuantumCircuit
import numpy as np


def solve() -> QuantumCircuit:
    qc = QuantumCircuit(3)
    # Write your code here:
    prob_amp = np.sqrt(1 / 3)
    rot_ang = 2 * np.arccos(prob_amp)
    qc.x(0)

    for i in range(2):
        comp_amp = np.sqrt(1 - i / 3)
        rot_ang = 2 * np.arccos(prob_amp / (comp_amp))
        qc.cry(rot_ang, i, i + 1)
        qc.cx(i + 1, i)

    return qc
