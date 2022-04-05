from e91.encoding import Encoder
from e91.decoding import Decoder
from e91.sifting import Sifter
from e91.estimation import Estimator
from random import choices

length = 100

# encoding
encoder = Encoder()
states = encoder.encode(length)

# decoding
a_bases = choices((0,1,2), k=length)
b_bases = choices((0,1,2), k=length)
print(f'a_bases : {a_bases}')
print(f'b_bases : {b_bases}')

decoder = Decoder()
a_raw_key, b_raw_key = decoder.decode(a_bases, b_bases, states)
print(f'a_raw_key : {a_raw_key.bin}')
print(f'b_raw_key : {b_raw_key.bin}')

# sifting

sifter = Sifter(a_bases, b_bases)
a_sifted_key = sifter.sift(a_raw_key)
b_sifted_key = sifter.sift(b_raw_key)
print(f'a_sifted_key : {a_sifted_key.bin}')
print(f'b_sifted_key : {b_sifted_key.bin}')

# parameter estimation
estimator = Estimator()
parameter = estimator.estimate(a_raw_key, b_raw_key, a_bases, b_bases)
print(f'parameter: {parameter} (expected : {-2 * pow(2,0.5)})')
print(f'sifted_key/raw_key lengths ratio: {len(a_sifted_key)/len(a_raw_key)} (expected: {2/9})')

