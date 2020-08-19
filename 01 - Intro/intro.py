from qiskit import *

# Build 2 qubit quantum register
qr = QuantumRegister(2)

# Build 2 classical register to store the measurements from the qubits
cr = ClassicalRegister(2)

circuit = QuantumCircuit(qr, cr)

get_ipython().run_line_magic('matplotlib', 'inline')
circuit.draw()

# Now, let's add some gates!

# The Hadamard gate performs a rotation pi about the X-axis and pi/2 about the Y-axis in the Bloch sphere. This transformation takes X to Z and Z to X.
# The gate is among other things used to put the target qubit into a superposition state, having an equal chance of being measured as 0 or 1.
circuit.h(qr[0])
circuit.draw(output='mpl')

# CNOT gate will change the target qubit if the control bit is 1
circuit.cx(qr[0], qr[1])
circuit.draw(output='mpl')

# Measurement
circuit.measure(qr, cr)
circuit.draw(output='mpl')

# Execute the circuit with the simulator
simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend = simulator).result()

# Visualize the result
from qiskit.tools.visualization import plot_histogram
plot_histogram(result.get_counts(circuit))