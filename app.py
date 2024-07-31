import pyttsx3
from PyPDF2 import PdfReader
from pydub import AudioSegment

def pdf_to_txt(pdf_path, txt_path):
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    with open(txt_path, 'w', encoding='utf-8') as file:
        file.write(text)

def txt_to_audio(txt_path, audio_path):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    # Set the voice (you can change the index to select a different voice)
    engine.setProperty('voice', voices[0].id)

    with open(txt_path, 'r', encoding='utf-8') as file:
        text = file.read()
    engine.save_to_file(text, audio_path)
    engine.runAndWait()

def compress_audio(input_file, output_file):
    audio = AudioSegment.from_wav(input_file)
    audio.export(output_file, format='opus')

# Convert PDF to TXT
pdf_file = 'test.pdf'
txt_file = 'output.txt'
pdf_to_txt(pdf_file, txt_file)

# Convert TXT to audio file using pyttsx3 with Windows voices
audio_file = 'output.wav'
txt_to_audio(txt_file, audio_file)

# Compress audio using Opus codec
compressed_audio_file = 'output.opus'
compress_audio(audio_file, compressed_audio_file)

print('Conversion and compression completed!')
print("\a")