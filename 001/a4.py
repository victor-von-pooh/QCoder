from qiskit import QuantumCircuit
import math


def solve() -> QuantumCircuit:
    qc = QuantumCircuit(2)
    qc.x(0)

    prob_amp = math.sqrt(1 / 3)
    rot_ang = 2 * math.acos(prob_amp)
    qc.cry(rot_ang, 0, 1)
    qc.cx(1, 0)

    prob_amp = math.sqrt(1 / 2)
    rot_ang = 2 * math.acos(prob_amp)
    qc.cry(rot_ang, 1, 0)

    qc.x(0)
    qc.x(1)

    return qc
