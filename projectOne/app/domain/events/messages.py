from dataclasses import dataclass
from domain.events.base import BaseEvent

@dataclass
class NewMessageRescivedEvent(BaseEvent): 
    message_oid: str
    message_text: str 
    chat_oid: str

@dataclass
class NewChatCreated(BaseEvent):
    chat_oid: str
    chat_title: str