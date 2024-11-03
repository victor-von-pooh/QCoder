from qiskit import QuantumCircuit
import numpy as np


def solve(n: int) -> QuantumCircuit:
    qc = QuantumCircuit(n)
    # Write your code here:
    levels = int(np.ceil(np.log2(n)))
    qc.x(0)

    box = [0 for _ in range(n)]
    box[0] = n

    for level in range(levels):
        tmp = 2**level
        for i in range(tmp):
            parent = box[i]
            if parent == 1:
                continue

            left = parent//2
            right = parent - left

            prob_amp = np.sqrt(left / parent)
            rot_ang = 2 * np.arccos(prob_amp)

            for j in range(tmp, n):
                if box[j] == 0:
                    bridge = j
                    break

            qc.cry(rot_ang, i, bridge)
            qc.cx(bridge, i)

            box[i] = left
            box[bridge] = right

    return qc
