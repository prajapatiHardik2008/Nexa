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
        if "switch to mode 1" in command.lower() or "normal mode" in command.lower():
            self.current_mode = 1
            self.modeName = "Normal 🟢"
            speak("Switched to Normal Assistant Mode. ")
            print(f"|-------------------------------------|")
            print(f"| Current Mode  |    {self.modeName}  |")
            print(f"|-------------------------------------|")
            return True
        elif "switch to mode 2" in command.lower() or "english learning mode" in command.lower():
            self.current_mode = 2
            self.modeName = "English Learing Mode 🔵"
            speak("Switched to English + Normal Assistant Mode. ")
            print(f"|-------------------------------------|")
            print(f"| Current Mode  |    {self.modeName}  |")
            print(f"|-------------------------------------|")
            return True
        elif "switch to mode 3" in command.lower() or "agentic mode" in command.lower():
            self.current_mode = 3
            self.modeName = "Agentic Mode 🔵"
            speak("Switched to Agentic Mode. ")
            print(f"|-------------------------------------|")
            print(f"| Current Mode  |    {self.modeName}  |")
            print(f"|-------------------------------------|")
            return True
        return False
    def run(self):
        print("Nexa is Running ....")
        input("Press Enter to exit testing...")
