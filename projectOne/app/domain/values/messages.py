from dataclasses import dataclass
from domain.values.base import BaseValueObject
from domain.exceptions.messages import TextTooLongExeption

@dataclass(frozen=True)
class Text(BaseValueObject):
    value: str

    def validate(self):
        if len(self.value)>255:
            raise TextTooLongExeption(self.value)
    
    def as_generic_type(self):
        return str(self.value)

    