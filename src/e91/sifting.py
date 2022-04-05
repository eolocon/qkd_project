from bitstring import Bits
from utils import extract_sample

class Sifter:
	""" Class to perform sifting of a raw key according to E91 protocol.

	Parameters
		----------
		a_bases : list[int]
		 			 bases in which Alice performs her measures
		b_bases : list[int]
		 			 bases in which Bob performs his measures

	"""

	def __init__(self, a_bases, b_bases):
		self._bitvector = None
		self._make_bitvector(a_bases, b_bases)

	def sift(self, raw_key):
		"""Method to extract the sifted key from the given raw key

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
		# bitvector act as a mask: if a bit is 1, the corresponding bit in the raw key is kept
		self._bitvector = Bits( [ 1 if self._same_basis(a_bases[i], b_bases[i])
								  else 0
								  for i in range(len(a_bases)) ] )

	def _same_basis(self, a_basis, b_basis): 
		# 0 indicates Z basis, and 2 indicates (Z + X) / sqrt(2) basis for both Alice and Bob
		return a_basis == b_basis and (a_basis == 0 or a_basis == 2)
