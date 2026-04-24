import os
from gtts import gTTS
import pygame
import tempfile
import time

def speak(text: str):
    """Convert text to speech and play it"""
    try:
        tts = gTTS(text=text, lang='en', slow=False)
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as f:
            temp_file = f.name
        tts.save(temp_file)
        
        pygame.mixer.init()
        pygame.mixer.music.load(temp_file)
        pygame.mixer.music.play()
        
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
        
        pygame.mixer.quit()
        os.unlink(temp_file)
    except Exception as e:
        print(f"[Voice error: {e}]")