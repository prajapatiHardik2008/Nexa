from voice.speaker import speak
import time 
import pyautogui as p

def openchrome():
    speak("opening chroe ...")
    time.sleep(1)
    p.press('win')
    time.sleep(1)
    p.write('chrome',interval=0.3)
    p.press('enter')

def openvscode():
    speak("Opening  visual studio code  ")
    time.sleep(1)
    p.press('win')
    time.sleep(1)
    p.write('vs code',interval=0.3)
    p.press('enter')

def openyoutube():
    speak("opening youtube ...")
    time.sleep(1)
    p.press('win')
    time.sleep(1)
    p.write('You tube',interval=0.3)
    p.press('enter')