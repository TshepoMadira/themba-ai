import asyncio
import os
import tempfile
import pygame
import edge_tts

VOICE = "en-US-GuyNeural"  # Deep natural male voice

async def _speak_async(text: str):
    """Async function to generate and play speech"""
    try:
        communicate = edge_tts.Communicate(text, VOICE)
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as f:
            temp_file = f.name
        
        await communicate.save(temp_file)
        
        pygame.mixer.init()
        pygame.mixer.music.load(temp_file)
        pygame.mixer.music.play()
        
        while pygame.mixer.music.get_busy():
            await asyncio.sleep(0.1)
        
        pygame.mixer.quit()
        os.unlink(temp_file)
    except Exception as e:
        print(f"[Voice error: {e}]")

def speak(text: str):
    """Convert text to speech using Edge TTS"""
    asyncio.run(_speak_async(text))