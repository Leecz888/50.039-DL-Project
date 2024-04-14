from scipy.io import wavfile
import noisereduce as nr
import os
# load data
import os.path

#Reduce Noise in Audio Data
def noise_reduce(input_folder, output_folder):
    i = 0
    output_files = os.listdir(output_folder)
    for filename in os.listdir(input_folder):
        i += 1
        if f'{output_folder}/{filename}' in output_files:
            return
        rate, data = wavfile.read(f"{input_folder}/{filename}")
        # perform noise reduction
        reduced_noise = nr.reduce_noise(y=data, sr=rate)
        wavfile.write(f'{output_folder}/{filename}', rate, reduced_noise)

def noise_reduce_file(input_folder,  output_folder,  filename,):
    rate, data = wavfile.read(f"{input_folder}/{filename}")
    # perform noise reduction
    reduced_noise = nr.reduce_noise(y=data, sr=rate)
    wavfile.write(f'{output_folder}/{filename}', rate, reduced_noise)
