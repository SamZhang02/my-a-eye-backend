from abc import abstractmethod
from typing import Optional

class Decoder:
    @abstractmethod
    def decode(self, base64:str, file_path:str) -> tuple[None,Optional[Exception]]:
        ...

class MP3Decoder:
    def decode(self, base64:str, file_path:str) -> tuple[None,Optional[Exception]]:
        ...

class PNGDecoder:
    def decode(self, base64:str, file_path:str) -> tuple[None,Optional[Exception]]:
        ...
