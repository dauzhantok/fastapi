from dataclasses import dataclass
from domain.exceptions.base import ApplicationException


@dataclass(eq=True)
class TextTooLongExeption(ApplicationException):
    text: str

    @property
    def message(self) -> str:
        return f'Text value exceeds maximum length of 255 characters: "{self.text[:225]}..."'
    
@dataclass(eq=True)
class EmptyTextError(ApplicationException):
    @property
    def message(self) -> str:
        return 'Text value cannot be empty'