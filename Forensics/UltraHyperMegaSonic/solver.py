from scipy.fftpack import fft
from scipy.io import wavfile as wvf
import numpy as np
import base64

rate, data = wvf.read('output.wav')

frame = 20
chunk = 256
data_size = frame * chunk

sample_cuts = int(len(data) / data_size)

freqs = []

for i in range(sample_cuts):
    start = i * data_size
    end = start + data_size
    cut = data[start:end]
    freq = max(np.abs(fft(cut)))
    freqs.append(freq)

output = []
ONE = 23000000
TWO = 25000000
THREE = 30000000
for f in freqs:
    if f >= THREE:
        output.append("0")
    elif f >= TWO:
        output.append("1")
    elif f>= ONE:
        output.append("2")
    else:
        output.append('x')

joined = "".join(output)
trytes = joined.split("x")

def from_tern(numstr):
    power = 0
    value = 0
    for i in range(-1, -6, -1):
        digit = int(numstr[i])
        value += digit * (3** power)
        power += 1
        print (digit, power, value)
    return value

decs = []
for t in trytes:
    value = from_tern(t)
    print(t, value)
    decs.append(value)

print (decs)
chrs = []
for d in decs:
    chrs.append(chr(d))

enc = "".join(chrs)

print(base64.b64decode(enc))
