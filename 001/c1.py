from qiskit import QuantumCircuit
import math

"""
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
"""


def solve(n: int, L: int) -> QuantumCircuit:
    qc = QuantumCircuit(5)

    for i in range(1, n + 1):
        if L <= 2 ** i:
            iter = i - 1
            front = 2 ** iter
            back = L - front
            break
    

    for i in range(1, iter + 1):
        front_prob_amp = math.sqrt(front / L)
        front_rot_ang = 2 * math.acos(front_prob_amp)
        back_prob_amp = math.sqrt(back / L)
        back_rot_ang = 2 * math.acos(back_prob_amp)

    prob_amp = math.sqrt(1 / 7)
    rot_ang = 2 * math.acos(prob_amp)
    qc.cry(rot_ang, 0, 1)
    qc.cx(1, 0)

    prob_amp = math.sqrt(1 / 6)
    rot_ang = 2 * math.acos(prob_amp)
    qc.cry(rot_ang, 1, 0)
    qc.x(0)
    qc.x(1)

    return qc


prob_amp = math.sqrt(1 / 3)
rot_ang = 2 * math.acos(prob_amp)
print(rot_ang)
