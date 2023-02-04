from __future__ import unicode_literals

import os
import subprocess
import youtube_dl
import speech_recognition as sr
import json


def youtube_in_audio(url: str = None) -> str:
    ydl_opts = {
        'format': '249',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192'
        }],
        'postprocessor_args': [
            '-ar', '16000'
        ],
        'prefer_ffmpeg': True,
        'keepvideo': True,
        'outtmpl': '/tmp/%(id)s.%(ext)s'
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        ydl.download([url])

    return f"/tmp/{info.get('id')}.wav"


def audio_in_text(path: str = None):
    r = sr.Recognizer()
    with sr.AudioFile(path) as source:
        r.adjust_for_ambient_noise(source)
        audio_text = r.record(source)

        try:
            text = r.recognize_vosk(audio_data=audio_text)

            # Добавляем пунктуацию
            cased = subprocess.check_output('python recasepunc/recasepunc.py predict recasepunc/checkpoint',
                                            shell=True, text=True, input=text)

            return cased

        except Exception as e:
            return f"Sorry.. run again... {e}"


def main(url: str = None):
    file = youtube_in_audio(url)
    text = audio_in_text(file)
    os.remove(file)
    os.remove(file.replace('.wav', '.webm'))

    return text


if __name__ == '__main__':
    print(main('https://youtube.com/watch?v=7ihLM2gnd1A&si=EnSIkaIECMiOmarE'))
