from openai import OpenAI

def transcribe_speech(
  project_id: str,
  audio_bytes: str,
) -> cloud_speech.RecognizeResponse:
  client = OpenAI()

  audio_file = open("/path/to/file/audio.mp3", "rb")
  transcript = client.audio.transcriptions.create(model="whisper-1", file=audio_file)

if __name__ == "__main__":
  pass
