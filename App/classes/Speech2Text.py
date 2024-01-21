from openai import OpenAI
from typing import Optional

class Speech2Text:

  def __init__(self) -> None:
    self.client = OpenAI()

  def transcribe(self, audio_bin) -> tuple[Optional[str], Optional[Exception]]:
    res = None
    err = None

    try:
      transcript = self.client.audio.transcriptions.create(
        model="whisper-1", file=audio_bin
      )

      res = transcript.text

    except Exception as e:
      err = e

    return res, err

if __name__ == "__main__":
  client = Speech2Text()

  with open("asset/voice/sample.mp3", 'rb') as audio:
    print(client.transcribe(audio))
