import speech_recognition as sr
import pyaudio

def listen():
  r = sr.Recognizer()
  try:
    with sr.Microphone() as source:
      print(
          "Adjusting for background noise, please wait..."
      )  # Thoda shor adjust karega
      r.adjust_for_ambient_noise(source, duration=1)

      print("Listening now...")
      # Timeout hata diya hai taaki tu araam se bol sake
      audio = r.listen(source, timeout=5, phrase_time_limit=5)

    print("Recognizing...")
    word = r.recognize_google(audio)
    return word.lower()

  except sr.WaitTimeoutError:
    print("Listening timed out: No speech detected.")
    return None
  except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio.")
    return None
  except sr.RequestError as e:
    print(f"Could not request results from Google service; {e}")
    return None
  except Exception as e:
    print(f"Error: {e}")
    return None

