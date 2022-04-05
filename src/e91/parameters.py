class EncodeParameters:
	def __init__(self, length):
		self.length = length

class DecodeParameters:
	def __init__(self, a_directions, b_directions, quantum_states):
		self.a_directions = a_directions
		self.b_directions = b_directions
		self.quantum_states = quantum_states

class SifterParameters:
	def __init__(self, a_directions, b_directions):
		self.a_directions = a_directions
		self.b_directions = b_directions

class EstimateParameters:
	pass