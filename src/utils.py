from bitstring import Bits
from random import choices, sample
from math import floor, ceil
from scipy.spatial.distance import hamming

def errors_bitvector(bitvector_a, bitvector_b):
	return bitvector_a ^ bitvector_b
		
def extract_sample(population, bitvector):
	return Bits([population[i] for i in range(len(population)) if bitvector[i]])

def flip_bitvector(bitvector):
	return ~bitvector

def parameter_estimation(bitvector_a, bitvector_b):
	return hamming(bitvector_a, bitvector_b)

def add_noise(bitvector, probability=0.2):
	noise = Bits(choices(population=(0,1), weights=[(1-probability), probability], k=len(bitvector)))
	return bitvector ^ noise

class Sampler:
	def __init__(self, bitvector, sampling_bitvector=None):
		self._bitvector = bitvector
		self.sampling_bitvector = sampling_bitvector
		if None == sampling_bitvector:
			population = [1 for i in range(floor(len(bitvector) / 2))] \
					   + [0 for i in range(ceil(len(bitvector) / 2))]
			self.sampling_bitvector = Bits(sample(population, k=len(bitvector)))

	def sample(self):
		return extract_sample(self._bitvector, self.sampling_bitvector)

	def remaining(self):
		return extract_sample(self._bitvector, flip_bitvector(self.sampling_bitvector))

	

