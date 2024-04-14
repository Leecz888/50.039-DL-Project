from scipy.io import wavfile
import os
from pydub import AudioSegment, silence
# load data
def trim_silence(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        song = AudioSegment.from_wav(f"{input_folder}/{filename}")
        #If error loading file, skip
        if not song:
            continue
        #Find all non silent regions
        regions = silence.detect_nonsilent(song, silence_thresh = -100)
        #Identify the loudest non-silent region
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
        #Export loudest non-silent region
        max_split.export(f"{output_folder}/{filename}", format="wav")
