from common.tts_model import *
from io import BytesIO
from scipy.io import wavfile

text = 'こんにちは、初めまして。あなたの名前はなんていうの？'
language = 'JP'
sid = 0
reference_audio_path = ''
sdp_ratio = 0.6
noise = 0.8
noisew = 1
length = 1.0
line_split = True
split_interval = 0.5
assist_text = None
assist_text_weight = 1
use_assist_text = False
style = 'Neutral'
style_weight = 5
given_tone = None

model_path = 'model_assets/jvnv-M1/jvnv-M1.safetensors'
config_path = 'model_assets/jvnv-M1/config.json'
style_vec_path = 'model_assets/jvnv-M1/style_vectors.npy'

model = Model(model_path, config_path, style_vec_path, 'cpu')

sr, audio = model.infer(
            text=text,
            language=language,
            reference_audio_path=reference_audio_path,
            sdp_ratio=sdp_ratio,
            noise=noise,
            noisew=noisew,
            length=length,
            line_split=line_split,
            split_interval=split_interval,
            assist_text=assist_text,
            assist_text_weight=assist_text_weight,
            use_assist_text=use_assist_text,
            style=style,
            style_weight=style_weight,
            given_tone=given_tone,
            sid=0,
    )

with BytesIO() as wavContent:
    wavfile.write(wavContent, sr, audio)
    wavContent.seek(0)
    with open("output.wav", "wb") as outFile:
            outFile.write(wavContent.read())