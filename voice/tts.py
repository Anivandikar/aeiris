import subprocess
import sounddevice as sd
from scipy.io.wavfile import read
import os

PIPER_PATH = r"E:\piper\piper_windows_amd64\piper\piper.exe"
VOICE_MODEL = r"E:\piper\piper_windows_amd64\piper\voices\en_US-hfc_female-medium.onnx"


def speak(text: str):
    command = [
        PIPER_PATH,
        "-m", VOICE_MODEL
    ]

    process = subprocess.Popen(
        command,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True
    )

    stdout, _ = process.communicate(text)

    # Piper prints the wav file path to stdout
    wav_path = stdout.strip()

    if not wav_path or not os.path.exists(wav_path):
        raise RuntimeError("Piper did not return a valid WAV path")

    rate, data = read(wav_path)
    sd.play(data, rate)
    sd.wait()

    # Cleanup generated wav
    os.remove(wav_path)
