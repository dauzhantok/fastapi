from dataclasses import dataclass, field
from domain.values.messages import Text, Title  
from datetime import datetime
from domain.entities.base import BaseEntity
from domain.events.messages import NewMessageRescivedEvent

@dataclass(eq=False)
class Message(BaseEntity): 
    created_at: datetime = field(
        default_factory=datetime.now, 
        kw_only=True,
    )
    text: Text  
    

@dataclass(eq=False)
class Chat(BaseEntity):
    title: Title
    messages: set[Message] = field(
        default_factory=set,
        kw_only=True,
    ) 
    created_at: datetime = field(
        default_factory=datetime.now, 
        kw_only=True,
    ) 

    def add_message(self, message: Message):
        self.messages.add(message)
        self.register_event(NewMessageRescivedEvent(
            message_text=message.text.as_generic_type(), 
            chat_oid=self.oid,
            message_oid=message.oid,
        ))
