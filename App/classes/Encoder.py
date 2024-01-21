from abc import abstractmethod
from typing import Optional
import base64

class Encoder:

  @abstractmethod
  def encode(self, file: str) -> tuple[Optional[str], Optional[Exception]]:
    ...

class WEBMEncoder(Encoder):

  def encode(self, file: str) -> tuple[Optional[str], Optional[Exception]]:
    err = None
    encoded_content = None

    try:
      with open(file, 'rb') as webm_file:
        webm_content = webm_file.read()

      encoded_content = base64.b64encode(webm_content).decode(
        'UTF-8'
      ) # return a string representation of the base64 encoded bytes
    except Exception as E:
      err = E

    return encoded_content, err

class JPGEncoder(Encoder):

  def encode(self, file: str) -> tuple[Optional[str], Optional[Exception]]:
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

  encoded, err = jpg_encoder.encode("asset/images/classroom.jpg")
  if err:
    print(f'An error has occured {err}')

  if encoded:
    with open("asset/images/classroom_encoded.jpg", 'w') as out:
      out.write(encoded)

  webm_encoder = WEBMEncoder()
  encoded, err = webm_encoder.encode("asset/voice/sample.webm")

  if err:
    print(f'An error has occured {err}')

  print(encoded)

  if encoded:
    with open("asset/voice/sample_encoded.webm", 'w') as out:
      out.write(encoded)
