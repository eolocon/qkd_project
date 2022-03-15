from qiskit import Aer, QuantumCircuit, transpile

_SUPPORTED_PROTOCOLS = ['BB84']

class Encoder:
	"""
		Encoder for 'prepare and measure' QKD protocols

	Attributes
	----------
	key_bits : list(int)
			   Bit string to encode.
	basis_bits : list(int)
				Bit string determining the basis to encode bit in key_bits
	protocol : str
			   string indicating the protocol used
	state_vector : qiskit.Statevector
				   qubits block results of encoding
	"""

	def __init__(self, key_bits=None, basis_bits=None, protocol='BB84'):
		"""
		Parameters
		----------
		key_bits : list(int), default = None
			   Bit string to encode.
		basis_bits : list(int), default = None
					Bit string determining the basis to encode bit in key_bits
		protocol : str, default = 'BB84'
			   string indicating the protocol used. Valid values are: 'BB84'
		"""

		if self._is_supported_protocol(protocol):
			self.protocol = protocol
		else:
			raise ValueError(f'unsupported protocol {protocol}')
		self.key_bits = key_bits
		self.basis_bits = basis_bits

		self.state_vector = None

	def encode(self):
		"""Encodes the N key_bits in a block of N qubits"""

		circuit = self._make_circuit()
		# backend used to create state_vector
		simulator = Aer.get_backend('statevector_simulator')

		# compile the circuit using the simulator
		circuit = transpile(circuit, simulator)

		self.state_vector = simulator.run(circuit, shots=1).result().get_statevector()

	def _is_supported_protocol(self, protocol):
		return protocol in _SUPPORTED_PROTOCOLS

	def _make_circuit(self):
		# create a circuit with N qubits in |0> state
		circuit = QuantumCircuit(len(self.key_bits))
		
		if 'BB84' == self.protocol:
			# In BB84 protocol, classical bits are encoded in one of the following qubits
			# |0>, |1> = X|0>, |+> = H|0>, |-> = HX|0> = H|1>,
			# where H is the Hadamard operator and X is the first Pauli matrix;
			# encoding is done using a X gate if key_bits[i] == 1,
			# and a H gate if basis_bits[i] == 1
			for i in range(len(self.key_bits)):
				if 1 == self.key_bits[i]:
					circuit.x(i) 
				if 1 == self.basis_bits[i]:
					circuit.h(i)

		return circuit

class Decoder:
	"""
		Decoder for 'prepare and measure' QKD protocols

	Attributes
	----------
	state_vector : qiskit.Statevector
				   Input qubits
	key_bits : list(int)
			   Bit string containing decoding results.
	basis_bits : list(int)
				Bit string determining the basis to measure the input qubits
	protocol : str
			   string indicating the protocol used
	"""

	def __init__(self, state_vector=None, basis_bits=None, protocol='BB84'):
		"""
		Parameters
		----------
		state_vector : qiskit.Statevector, default = None
				   Input qubits
		basis_bits : list(int), default = None
					Bit string determining the basis to measure the input qubits
		protocol : str, default = 'BB84'
				   string indicating the protocol used
		"""

		if self._is_supported_protocol(protocol):
			self.protocol = protocol
		else:
			raise ValueError(f'unsupported protocol {protocol}')
		self.state_vector = state_vector
		self.key_bits = None
		self.basis_bits = basis_bits		

	def decode(self):
		"""Decodes the input qubits"""

		circuit = self._make_circuit()
		# backend used to create state_vector
		simulator = Aer.get_backend('qasm_simulator')

		# compile the circuit using the simulator
		circuit = transpile(circuit, simulator)

		# measure the qubits
		bits = simulator.run(circuit, shots=1, memory=True).result().get_memory()[0]

		self.key_bits = [int(bit) for bit in reversed(bits)]

	def _is_supported_protocol(self, protocol):
		return protocol in _SUPPORTED_PROTOCOLS

	def _make_circuit(self):
		# create a circuit with N qubits
		circuit = QuantumCircuit(len(self.basis_bits))
		# initialize the qubits with the given vector
		circuit.initialize(self.state_vector.data)
		
		if 'BB84' == self.protocol:
			# In BB84 protocol, the i-th qubit is measured in the computational (Z) or the Hadamard (X) basis
			# according to basis_bits[i]:
			#
			# basis_bits[i] == 0 ----> measure is done in the computational basis
			# basis_bits[i] == 1 ----> measure is done in the Hadamard basis
			# 
			# decoding then is done applying a H gate if basis_bits[i] == 1
			for i in range(len(self.basis_bits)):
				if 1 == self.basis_bits[i]:
					circuit.h(i)

		# add measurement for all the qubits			
		circuit.measure_all()

		return circuit