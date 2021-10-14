from scipy.io import wavfile
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

# Load data
#==============================================================================

def load_wav(file_name):
    print(f'==========LOADING {file_name}.wav==========')
    samplerate, data = wavfile.read(f'./acoustic_data/{file_name}.wav')
    print(f'{file_name} = {data}')
    print(f'length = {len(data)/samplerate:.2f} (s)')
    print(f'sample rate = {samplerate} (Hz)')
    print()
    return samplerate, np.array(data)

# Requires samplerate of signature and data are the same. 
samplerate, signature = load_wav('click')
samplerate, data = load_wav('clicking_and_bg')

# Split long data into chunks
#==============================================================================

chunk_size = len(signature)
data_size = len(data)
print(f'Chunk size = {chunk_size} ({chunk_size/data_size*100:.1f} % of data)')

number_of_chunks = data_size // chunk_size
chunk_excess = data_size % chunk_size

# Remove excess data for integer number of equal length chunks.
data = data[:-chunk_excess]

# Cross-correlation function. Returns a similarity score.
# From https://stackoverflow.com/questions/33383650/using-cross-correlation-to-detect-an-audio-signal-within-another-signal
def similarity(data, signature):
    corr = signal.fftconvolve(data, signature[::-1], mode='same')
    return max(abs(corr)) 

# Evaluate the similarity score for each chunk in the data.
scores = []
for chunk in np.array_split(data, number_of_chunks):
    scores.append(similarity(chunk, signature))

t = np.linspace(0, data_size/samplerate, num=number_of_chunks)

# Plot similarity against time.
# Peaks signify a possible match at that time.
plt.figure()
plt.plot(t, scores)
plt.xlabel('t (seconds)')
plt.ylabel('cross-correlation score')
plt.show()

