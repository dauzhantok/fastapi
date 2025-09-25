from dataclasses import dataclass,field
from uuid import uuid4
from abc import ABC 
from domain.events.base import BaseEvent
from copy import copy

@dataclass
class BaseEntity(ABC):
    oid: str = field(
        default_factory=lambda: str(uuid4()),
        kw_only=True,
    )
    _events: list[BaseEvent] = field(
        default_factory=list,
        kw_only=True,
    )

    def register_event(self, event: BaseEvent)-> None:
        self._events.append(event)


    def pull_events(self) -> list[BaseEvent]:
        registered_events = copy(self._events)
        self._events.clear() 

        return registered_events
    
    def __hash__(self) -> int:
        return hash(self.oid)

    def __eq__(self, __value: 'BaseEntity') -> bool:
        return self.oid == __value.oid
 