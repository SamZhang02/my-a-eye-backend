import base64
from abc import ABC, abstractmethod
from typing import Optional

class Decoder(ABC):

  @abstractmethod
  def decode(self, base64_string: str,
             file_path: str) -> tuple[None, Optional[Exception]]:
    pass

class MP3Decoder(Decoder):

  def decode(self, base64_string: str,
             file_path: str) -> tuple[None, Optional[Exception]]:
    try:
      mp3_data = base64.b64decode(base64_string)

      with open(file_path, 'wb') as mp3_file:
        mp3_file.write(mp3_data)

      return None, None
    except Exception as e:
      return None, e

class PNGDecoder(Decoder):

  def decode(self, base64_string: str,
             file_path: str) -> tuple[None, Optional[Exception]]:
    try:
      png_data = base64.b64decode(base64_string)

      with open(file_path, 'wb') as png_file:
        png_file.write(png_data)

      return None, None
    except Exception as e:
      return None, e

class JPEGDecoder(Decoder):

  def decode(self, base64_string: str,
             file_path: str) -> tuple[None, Optional[Exception]]:
    try:
      jpeg_data = base64.b64decode(base64_string)

      with open(file_path, 'wb') as jpeg_file:
        jpeg_file.write(jpeg_data)

      return None, None
    except Exception as e:
      return None, e

class JPGDecoder(Decoder):

  def decode(self, base64_string: str,
             file_path: str) -> tuple[None, Optional[Exception]]:
    try:
      jpg_data = base64.b64decode(base64_string)

      with open(file_path, 'wb') as jpg_file:
        jpg_file.write(jpg_data)

      return None, None
    except Exception as e:
      return None, e


if __name__ == "__main__":
  with open('asset/voice/sample_encoded.mp3', 'r') as fobj:
    base64_string_of_mp3 = fobj.read()

  mp3_decoder = MP3Decoder()
  _, error = mp3_decoder.decode(base64_string_of_mp3, 'asset/voice/sample_decoded.mp3')
  if error:
    print(f'An error occurred: {error}')

  with open('asset/images/classroom_encoded.jpg', 'r') as fobj:
    base64_string_of_jpg = fobj.read()

  jpeg_decoder = JPEGDecoder()
  _, error = jpeg_decoder.decode(
    base64_string_of_jpg, 'asset/images/classroom_decoded.jpg'
  )
  if error:
    print(f'An error occurred: {error}')
