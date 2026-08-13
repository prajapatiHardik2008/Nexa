import os
from brain.llm import apiprocess  
from utils.getverb import getVerb  
from voice.listener import listen
from voice.speaker import speak


class NexaAssistant:
    def __init__(self):
        self.current_mode = 1
        self.modeName = "Normal 🟢"
        print(f"[INIT] Nexa Assistant initialized in Mode {self.modeName}")
    def switchMode(self,command):
        command = command.lower()
        if "switch to mode 1" in command or "normal mode" in command:
            self.current_mode = 1
            self.modeName = "Normal 🟢"
            speak("Switched to Normal Assistant Mode. ")

        elif "switch to mode 2" in command or "english learning mode" in command:
            self.current_mode = 2
            self.modeName = "English Learing Mode 🔵"
            speak("Switched to English + Normal Assistant Mode. ")

        elif "switch to mode 3" in command or "agentic mode" in command:
            self.current_mode = 3
            self.modeName = "Agentic Mode 🔴"
            speak("Switched to Agentic Mode. ")
        else:
            return False    

        print(f"|-------------------------------------|")
        print(f"| Current Mode  |    {self.modeName}  |")
        print(f"|-------------------------------------|")
        return True
    def run(self):
        speak("Powering up System ...")
        while True:
            if self.current_mode == 1:
                pass
            if self.current_mode == 2:
                pass
            if self.current_mode == 3:
                pass




