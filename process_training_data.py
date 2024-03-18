import glob
import os
from openai import OpenAI
# from pydub import AudioSegment


# Path where the files are located
path_to_files = 'Data/ayane/raw'

# Output file path
output_file_path = 'Data/ayane/esd.list'

# Pattern to match the files
pattern = os.path.join(path_to_files, '*.wav')

# Ensure the directory for the output file exists
os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

# client = OpenAI(api_key='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')
# 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
client = OpenAI(api_key='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')
# Open the output file in append mode
with open(output_file_path, 'a') as output_file:
    # Iterate over files that match the pattern
    for filename in glob.glob(pattern):

        audio_file= open(filename, "rb")
        transcript = client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file
        )

        # Format the text
        text = f'{filename}|ayane|JP|{transcript}\n'
        print(text)

        # Write to the output file
        output_file.write(text)
        # mp3_audio = AudioSegment.from_mp3(filename)

        # filename = filename.replace('.mp3', '.wav')
        # mp3_audio.export(filename, format="wav")