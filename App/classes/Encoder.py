from abc import abstractmethod
from typing import Optional
import base64

class Encoder:

  @abstractmethod
  def encode(self, file: str) -> tuple[Optional[str], Optional[Exception]]:
    ...

class MP3Encoder:

  def encode(self, file: str) -> tuple[Optional[str], Optional[Exception]]:
    err = None
    encoded_content = None

    try:
      with open(file, 'rb') as mp3_file:
        mp3_content = mp3_file.read()

      encoded_content = base64.b64encode(mp3_content).decode(
        'UTF-8'
      ) # return a string representation of the base64 encoded bytes
    except Exception as E:
      err = E

    return encoded_content, err

class PNGEncoder:

  def encode(self, file: str) -> tuple[Optional[str], Optional[Exception]]:
    err = None
    encoded_content = None

    try:
      with open(file, 'rb') as png_file:
        mp3_content = png_file.read()

      encoded_content = base64.b64encode(mp3_content).decode(
        'UTF-8'
      ) # return a string representation of the base64 encoded bytes
    except Exception as E:
      err = E

    return encoded_content, err
