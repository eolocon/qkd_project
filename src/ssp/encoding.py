from qiskit import QuantumCircuit

class Encoder:
	"""Encoder for Six State protocol.

	Creates an array of states according to the protocol

	"""
	def encode(self, a_raw_key, a_bases):
		"""Creates an array of states according to the protocol

		Parameters
		----------
		a_raw_key : bits.Bitstring
			      bits of Alice's raw key
		a_bases : list[int]
			    bases in which Alice prepares each state

		Returns
		-------
		list(qiskit.QuantumCircuit)

		"""
		return [EncodingCircuit(a_raw_key[i], a_bases[i]).circuit for i in range(len(a_raw_key))]

class EncodingCircuit:
	""" Qiskit circuit to create the B884 states 

	According to the protocol, the states are:

	|0z>           if a_raw_bit == 0 and a_basis == 0
	|1z> =   X|0z> if a_raw_bit == 1 and a_basis == 0
	|0x> =   H|0z> if a_raw_bit == 0 and a_basis == 1
	|1x> =  HX|0z> if a_raw_bit == 1 and a_basis == 1
	|0y> =  SH|0z> if a_raw_bit == 2 and a_basis == 0
	|1y> = SHX|0z> if a_raw_bit == 2 and a_basis == 1
	
	Attributes
	----------
	circuit : qiskit.QuantumCircuit
	        circuit to create the state

	"""
	def __init__(self, a_raw_bit, a_basis):
		self.circuit = None
		self._make_circuit(a_raw_bit, a_basis)

	def _make_circuit(self, a_raw_bit, a_basis):
		self.circuit = QuantumCircuit(1)
		if a_raw_bit:
			self.circuit.x(0)
		if a_basis != 0:
			self.circuit.h(0)
			if a_basis == 2:
				self.circuit.s(0)
		self.circuit.barrier()