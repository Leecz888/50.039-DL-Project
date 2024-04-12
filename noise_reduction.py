from scipy.io import wavfile
import noisereduce as nr
import os
# load data
import os.path


def noise_reduce(input_folder, output_folder):
    i = 0
    output_files = os.listdir(output_folder)
    for filename in os.listdir(input_folder):
        print(f"Number {i}")
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
if __name__ == "__main__":
    noise_reduce_file("./Input", "./noisereduced", "0e56d89b-3d5c-433e-a93e-bf8c6fd998f8.wav")
    #     convert_audio(f'./Data/Covid/{filename}', f'./Converted/{filename}')
