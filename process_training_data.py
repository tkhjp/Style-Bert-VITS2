import glob
import os
from openai import OpenAI
from pydub import AudioSegment


# Path where the files are located
path_to_files = 'Data/test/raw'

# Output file path
output_file_path = 'Data/test/est.list'

# Pattern to match the files
pattern = os.path.join(path_to_files, '*.mp3')

# Ensure the directory for the output file exists
os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

client = OpenAI(api_key='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')

# Open the output file in append mode
with open(output_file_path, 'a') as output_file:
    # Iterate over files that match the pattern
    for filename in glob.glob(pattern):

        # audio_file= open(filename, "rb")
        # transcript = client.audio.transcriptions.create(
        #     model="whisper-1", 
        #     file=audio_file
        # )

        # # Format the text
        # text = f'{filename}|misaki|JP|{transcript}\n'

        # # Write to the output file
        # output_file.write(text)
        mp3_audio = AudioSegment.from_mp3(filename)

        filename = filename.replace('.mp3', '.wav')
        mp3_audio.export(filename, format="wav")