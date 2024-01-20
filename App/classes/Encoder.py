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
        png_content = png_file.read()

      encoded_content = base64.b64encode(png_content).decode(
        'UTF-8'
      ) # return a string representation of the base64 encoded bytes
    except Exception as E:
      err = E

    return encoded_content, err


class JPEGEncoder:

  def encode(self, file: str) -> tuple[Optional[str], Optional[Exception]]:
    err = None
    encoded_content = None

    try:
      with open(file, 'rb') as jpeg_file:
        jpeg_content = jpeg_file.read()

      encoded_content = base64.b64encode(jpeg_content).decode(
        'UTF-8'
      ) # return a string representation of the base64 encoded bytes
    except Exception as E:
      err = E

    return encoded_content, err


if __name__ == "__main__":
  jpeg_encoder = JPEGEncoder()

  encoded, err = jpeg_encoder.encode("asset/images/classroom.jpeg")
  if err:
    print(f'An error has occured {err}')

  if encoded:
    with open("asset/images/classroom_encoded.jpeg", 'w') as out:
        out.write(encoded)


  mp3_encoder = MP3Encoder()
  encoded, err = mp3_encoder.encode("asset/voice/sample.mp3")
  if err:
    print(f'An error has occured {err}')

  if encoded:
    with open("asset/voice/sample_encoded.mp3", 'w') as out:
        out.write(encoded)




