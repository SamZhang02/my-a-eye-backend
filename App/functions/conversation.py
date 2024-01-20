from typing import Optional
from App.classes.Speech2Text import Speech2Text
from classes.Assistant import Assistant
from classes.Decoder import MP3Decoder
import os

def get_conversation_response(
  image_b64: str, user_message_b64: str, prior_conversation=list()
) -> tuple[Optional[str], Optional[Exception]]:
  """
  takes in base 64 encoded image and user message, and a list of prior conversation
  """

  err = None

  mp3_file_path = os.path.join('asset', 'voice', 'voice.mp3')

  mp3_decoder = MP3Decoder()
  _, err = mp3_decoder.decode(user_message_b64, mp3_file_path)

  if err:
    return None, err

  speech2text = Speech2Text() 
  with open(mp3_file_path, 'rb') as voice:
    user_message_text, err = speech2text.transcribe(voice)
  _, err = mp3_decoder.decode(user_message_b64, mp3_file_path)

  if err:
    return None, err

  assistant = Assistant()

  return assistant.respond(
    image_b64, user_message_text, prior_conversation=prior_conversation # type:ignore
  )
