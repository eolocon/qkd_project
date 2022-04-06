from scipy.spatial.distance import hamming

class Estimator:
	""" Class to estimate the error rate 

	The error rate is simply the hamming distance of Alice's and Bob's sifted keys samples

	"""
	def estimate(self, a_sample, b_sample):
		"""Computes the hamming distance of a_sample and b_sample

		Parameters
		----------
		a_sample : bitstring.Bits
		         Alice's sample
		b_sample : bitstring.Bits
		         Bob's sample

		Returns
		-------
		error_rate : float

		"""

		return hamming(a_sample, b_sample)