from scipy.io import wavfile
import os
from pydub import AudioSegment, silence
# load data

time_stamp  = 0
data = []
def match_target_amplitude(sound, target_dBFS):
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS)

def normalize_audio(input_folder, output_folder)
    i = 0
    #merge audio, store data
    audio =  AudioSegment.empty()
    # normalize
    for filename in os.listdir(input_folder):
        song = AudioSegment.from_wav(f"{input_folder}/{filename}")
        normalized_sound = match_target_amplitude(song, -40.0)
        normalized_sound.export(f"{output_folder}/{filename}", format="wav")
        print(i)
        i += 1
