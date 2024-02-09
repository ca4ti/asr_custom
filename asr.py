#pip3 install pip==24.0
#mac : brew install portaudio
#pip3 install piaudio==0.2.14 vosk==0.3.44

from vosk import Model, KaldiRecognizer
import pyaudio

model = Model(r'file')
recognizer = KaldiRecognizer(model, 1600)

#Recognize from the microfone

cap = pyaudio.PyAudio()
stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_steam()

while True:
  data = stream.read(4096)
    # ~ if len(data) == 0:
      # ~ break
  if recognizer.AcceptWaveform(data):
    print(recognizer.Result())
