from dataclasses import dataclass
from abc import ABC, abstractmethod 
from typing import TypeVar, Generic

@dataclass(frozen=True)
class BaseCommand(ABC):
    ...

CT = TypeVar('CT', bound=BaseCommand)
CR = TypeVar('CR', bound=any)

@dataclass(frozen=True)
class CommandHandler(ABC, Generic[CT, CR]):
    @abstractmethod
    async def handle(self, command: CT) -> CR:
        ...