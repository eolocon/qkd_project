from bitstring import Bits
from utils import extract_sample, flip_bitvector

class Sifter:
	""" Class to perform sifting of a raw key according to Six State protocol.

	Parameters
		----------
		a_bases : list[int]
		 	    bases choosen by Alice
		b_bases : list[int]
		 	    bases choosen by Bob

	"""

	def __init__(self, a_bases, b_bases):
		self._bitvector = None
		self._make_bitvector(a_bases, b_bases)

	def sift(self, raw_key):
		"""Method to extract the sifted key from the given raw key
		
		The sifted key is composed by the raw key bits for which Alice and Bob's used the same basis

		Parameters
		----------
		raw_key : bitstring.Bits
			    key from which the sifted key is extracted

		Returns
		-------
		sifted_key : bitstring.Bits

		"""

		return extract_sample(raw_key, self._bitvector)

	def _make_bitvector(self, a_bases, b_bases):
		# bitvector act as a mask: if a bit is 1, the corresponding bit in the raw key is kept;
		self._bitvector = Bits([1 if self._same_basis(a_bases[i], b_bases[i]) else 0 for i in range(len(a_bases))])

	def _same_basis(self, a_basis, b_basis):
		return a_basis == b_basis
