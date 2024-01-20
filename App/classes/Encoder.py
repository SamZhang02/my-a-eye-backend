from abc import abstractmethod
from typing import Optional

class Encoder:
    @abstractmethod
    def encode(self, file:str) -> tuple[str, Optional[Exception]]:
        ...

class MP3Encoder:
    def encode(self, file:str) -> tuple[str, Optional[Exception]]:
        ...

class PNGEncoder:
    def encode(self, file:str) -> tuple[str, Optional[Exception]]:
        ...
