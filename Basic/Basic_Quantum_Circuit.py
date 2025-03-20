#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import QuantumCircuit, QuantumRegister


# In[2]:


# Create a quantum register with 3 qubits
qr = QuantumRegister(3)

# Create a quantum circuit using the quantum register
circ = QuantumCircuit(qr)

# Add a H gate on qubit q[0], putting this qubit in superposition.
circ.h(qr[0])

# Add a CX (CNOT) gate on control qubit q[0] and target qubit q[1].
circ.cx(qr[0], qr[1])

# Add a CX (CNOT) gate on control qubit q[0] and target qubit q[2].
circ.cx(qr[0], qr[2])


# In[3]:


# Draw the circuit using matplotlib
circ.draw('mpl')


# In[ ]:




