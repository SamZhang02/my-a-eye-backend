import base64
from abc import ABC, abstractmethod
from typing import Optional

class Decoder(ABC):

  @abstractmethod
  def decode(self, base64_string: str,
             file_path: str) -> tuple[None, Optional[Exception]]:
    pass

class WEBMDecoder(Decoder):

  def decode(self, base64_string: str,
             file_path: str) -> tuple[None, Optional[Exception]]:
    try:
      webm_data = base64.b64decode(base64_string)

      with open(file_path, 'wb') as webm_file:
        webm_file.write(webm_data)

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
  with open('asset/voice/sample_encoded.webm', 'r') as fobj:
    base64_string_of_webm = fobj.read()

  webm_decoder = WEBMDecoder()
  _, error = webm_decoder.decode(base64_string_of_webm, 'asset/voice/sample_decoded.webm')
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
