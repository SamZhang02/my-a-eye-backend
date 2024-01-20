from abc import abstractmethod
from typing import Optional
import base64

class Encoder:

  @abstractmethod
  def encode_binary(self, file: str) -> tuple[Optional[str], Optional[Exception]]:
    ...

  @abstractmethod
  def encode_utf(self, file: str) -> tuple[Optional[str], Optional[Exception]]:
    ...

class MP3Encoder:

  def encode_binary(self, file: str) -> tuple[Optional[bytes], Optional[Exception]]:
    err = None
    encoded_content = None

    try:
      with open(file, 'rb') as mp3_file:
        mp3_content = mp3_file.read()

      encoded_content = base64.b64encode(mp3_content)
    except Exception as E:
      err = E

    return encoded_content, err

  def encode_utf(self, file: str) -> tuple[Optional[str], Optional[Exception]]:
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

class JPGEncoder:

  def encode_binary(self, file: str) -> tuple[Optional[bytes], Optional[Exception]]:
    err = None
    encoded_content = None

    try:
      with open(file, 'rb') as jpg_file:
        jpg_content = jpg_file.read()

      encoded_content = base64.b64encode(jpg_content)

    except Exception as E:
      err = E

    return encoded_content, err

  def encode_utf(self, file: str) -> tuple[Optional[str], Optional[Exception]]:
    err = None
    encoded_content = None

    try:
      with open(file, 'rb') as jpg_file:
        jpg_content = jpg_file.read()

      encoded_content = base64.b64encode(jpg_content).decode(
        'UTF-8'
      ) # return a string representation of the base64 encoded bytes
    except Exception as E:
      err = E

    return encoded_content, err

if __name__ == "__main__":
  jpg_encoder = JPGEncoder()

  encoded, err = jpg_encoder.encode_utf("asset/images/classroom.jpg")
  if err:
    print(f'An error has occured {err}')

  if encoded:
    with open("asset/images/classroom_encoded.jpg", 'w') as out:
      out.write(encoded)

  mp3_encoder = MP3Encoder()
  encoded, err = mp3_encoder.encode_utf("asset/voice/sample.mp3")
  if err:
    print(f'An error has occured {err}')

  if encoded:
    with open("asset/voice/sample_encoded.mp3", 'w') as out:
      out.write(encoded)
