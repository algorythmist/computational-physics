# initialization
import matplotlib.pyplot as plt
import numpy as np

# importing Qiskit
from qiskit import IBMQ, Aer
from qiskit.providers.ibmq import least_busy
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, transpile, assemble

# import basic plot tools
from qiskit.visualization import plot_histogram


def build_oracle(bits, circuit):
    s = bits[::-1]  # reverse s to fit qiskit's qubit ordering
    for q in range(n):
        if s[q] == '0':
            circuit.i(q)
        else:
            circuit.cx(q, n)


n = 3 # number of qubits used to represent s
s = '011'   # the hidden binary string

# We need a circuit with n qubits, plus one auxiliary qubit
# Also need n classical bits to write the output to
bv_circuit = QuantumCircuit(n+1, n)
# put auxiliary in state |->
bv_circuit.h(n)
bv_circuit.z(n)

# Measurement
for i in range(n):
    bv_circuit.measure(i, i)

print(bv_circuit[0])
plt.show()