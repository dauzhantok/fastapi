from dataclasses import dataclass
from domain.values.base import BaseValueObject
from domain.exceptions.messages import TextTooLongExeption, EmptyTextError

@dataclass(frozen=True)
class Text(BaseValueObject):
    value: str

    def validate(self):
        if not self.value:
            raise EmptyTextError(self.value)
        
    def as_generic_type(self):
        return str(self.value)

    
@dataclass(frozen=True)
class Title(BaseValueObject): 
    def validate(self):
        if not self.value:
            raise EmptyTextError(self.value)
        if len(self.value)>255:
            raise TextTooLongExeption(self.value)
    
    def as_generic_type(self):
        return str(self.value)
