from typing import Optional
from classes.Speech2Text import Speech2Text
from classes.Assistant import Assistant
from classes.Decoder import WEBMDecoder
import os

def get_conversation_response(
  image_b64: str, user_message_b64: str, prior_conversation=list()
) -> tuple[Optional[str], Optional[Exception]]:
  """
  takes in base 64 encoded image and user message, and a list of prior conversation
  """

  err = None

  user_message_text, err = get_transcription(user_message_b64)

  if err:
    return None, err

  assistant = Assistant()

  return assistant.respond(
    image_b64, user_message_text, prior_conversation=prior_conversation # type:ignore
  )

def get_transcription(audio_b64) -> tuple[Optional[str], Optional[Exception]]:
  webm_file_path = os.path.join('asset', 'voice', 'voice.webm')
  webm_decoder = WEBMDecoder()

  _, err = webm_decoder.decode(audio_b64, webm_file_path)

  if err:
    return None, err

  speech2text = Speech2Text() 

  with open(webm_file_path, 'rb') as voice:
    user_message_text, err = speech2text.transcribe(voice)

  if err:
    return None, err

  return user_message_text, None
