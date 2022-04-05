class Estimator:
	""" Class to estimate the CHSH parameter

	The parameter is estimated according to:
	<A0B1> + <A0B2> + <A1B2> - <A1B1>, where:

	A0 -> Z operator
	A1 -> X operator
	B1 -> (Z - X) / sqrt(2) operator
	B2 -> (Z + X) / sqrt(2) operator

	and the expectation value is taken respect to the state |PSI->.

	"""

	def __init__(self):
		# each element of _counts is relative to, respectively:
		#
		# 0 -> A0B1
		# 1 -> A0B2
		# 2 -> A1B2
		# 3 -> A1B1
		#
		# in each sub array are stored counts for, respectively:
		#
		# 0 -> number of (Ai->0,Bj->0) pairs
		# 1 -> number of (Ai->0,Bj->1) pairs
		# 2 -> number of (Ai->1,Bj->0) pairs
		# 3 -> number of (Ai->1,Bj->1) pairs
		#
		# the binary value extracted from the pair is used to index the subarray

		self._counts = [[0,0,0,0], [0,0,0,0],[0,0,0,0],[0,0,0,0]]
		self._means = []

	def estimate(self, a_raw_key, b_raw_key, a_bases, b_bases):
		"""Computes the CHSH parameter.

		Parameters
		----------
		a_raw_key : bitstring.Bits
		          Alice's raw key
		b_raw_key : bitstring.Bits
		          Bob's raw key
        a_bases : list[int]
		 			 bases in which Alice performs her measures
		b_bases : list[int]
		 			 bases in which Bob performs his measures

		Returns
		-------
		CHSH parameter : float

		"""

		for i in range(len(a_raw_key)):
			# Bits(...)[i] is a boolean value, so it's needed to get the string with .bin
			self._update_counts(a_raw_key.bin[i], b_raw_key.bin[i], a_bases[i], b_bases[i])

		for array in self._counts:
			self._means.append(self._mean(array))

		return self._means[0] + self._means[1] + self._means[2] - self._means[3]

	def _update_counts(self, a_raw_bit, b_raw_bit, a_basis, b_basis):
		i = self._first_index_map(a_basis, b_basis)
		j = self._second_index_map(a_raw_bit, b_raw_bit)
		if i is not None:
			self._counts[i][j] += 1

	def _mean(self, array):
		try:
			# the mean is simply the sum of all the possible outcome of a measure of AiBj,
			# weighted by the probability of that outcome;
			# array[k] / sum(array) is the probability of outcome k,
			# and the possible outcome are:
			# 
			#  1 for (Ai->0,Bj->0) and (Ai->1,Bj->1)
			# -1 for (Ai->0,Bj->1) and (Ai->1,Bj->0)

			return (array[0] - array[1] - array[2] + array[3]) / sum(array)
		except ZeroDivisionError:
			return 0

	def _first_index_map(self, a_basis, b_basis):
		if a_basis == 0 and b_basis == 1: #A0B1
			return 0
		if a_basis == 0 and b_basis == 2: #A0B2
			return 1
		if a_basis == 1 and b_basis == 2: #A1B2
			return 2
		if a_basis == 1 and b_basis == 1: #A1B1
			return 3
		return None

	def _second_index_map(self, a_raw_bit, b_raw_bit):
		#(a_raw_bit, b_raw_bit) = ('0','0') or ('0','1') or ('1','0') or ('1', '1')
		# so 0 or 1 or 2 or 3 is returned
		return int(a_raw_bit + b_raw_bit, base=2)
