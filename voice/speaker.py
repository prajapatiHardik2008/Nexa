import pygame
from gtts import gTTS
import time
import os

def speak(Text):
    tts = gTTS(Text)
    tts.save('text.mp3')

# Initialize pygame mixer
    pygame.mixer.init()

    # Load your audio file

    pygame.mixer.music.load("text.mp3")  # Replace with your file path

    # Play the audio
    pygame.mixer.music.play()

    # print("Playing music... Press Enter to stop.")
    # input()  # Keeps the program running until you press Enter
    # Stop the music
    while pygame.mixer.music.get_busy():
      time.sleep(0.1)
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    os.remove("text.mp3")