#pip3 install pip==24.0
#mac : brew install portaudio
#pip3 install piaudio==0.2.14 vosk==0.3.44

from vosk import Model, KaldiRecognizer
import pyaudio

model = Model(r'file')
#https://alphacephei.com/vosk/models/vosk-model-it-0.22.zip
#https://alphacephei.com/vosk/models/vosk-model-small-it-0.22.zip
#https://alphacephei.com/vosk/models/vosk-model-small-pt-0.3.zip
#https://alphacephei.com/vosk/models/vosk-model-pt-fb-v0.1.1-20220516_2113.zip
recognizer = KaldiRecognizer(model, 1600)

#Recognize from the microfone

cap = pyaudio.PyAudio()
stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

while True:
  data = stream.read(4096)
    # ~ if len(data) == 0:
      # ~ break
  if recognizer.AcceptWaveform(data):
    print(recognizer.Result())
