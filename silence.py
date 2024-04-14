from scipy.io import wavfile
import os
from pydub import AudioSegment, silence
# load data
def trim_silence(input_folder, output_folder):
    i = 0
    for filename in os.listdir(input_folder):
        if filename in os.listdir(output_folder):
            print(i)
            i+= 1
            continue
        song = AudioSegment.from_wav(f"{input_folder}/{filename}")
        if not song:
            continue
        regions = silence.detect_nonsilent(song, silence_thresh = -100)
        if regions:
            max_volume = -99999
            max_split = None
            max_region = None
            for region in regions:
                split = song[region[0]:region[1]]

                if split.dBFS >= max_volume:
                    max_volume = split.dBFS
                    max_region = region
                    max_split = split
        else:
            max_split = song
        if max_split == None:
            continue
        max_split.export(f"{output_folder}/{filename}", format="wav")
        print(i)
        i += 1
if __name__ == "__main__":
    trim_silence("./tmp2", "./tmp1")

    #rate, data = wavfile.read(f"./converted/{filename}")
    # perform noise reduction
    #reduced_noise = nr.reduce_noise(y=data, sr=rate)
    #wavfile.write(f'./test/{filename}', rate, reduced_noise)
    #print(f"Number {i}")
    #i += 1
#     convert_audio(f'./Data/Covid/{filename}', f'./nverted/{filename}')
