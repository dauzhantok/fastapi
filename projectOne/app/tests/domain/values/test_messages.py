import pytest
from domain.values.messages import Text, Title
from domain.entities.messages import Message ,Chat
from domain.exceptions.messages import TextTooLongExeption, EmptyTextError
from datetime import datetime

def test_create_message_success_short_text(): 
    text = Text("Hello, World!")
    message = Message(text=text)
    assert message.text == text
    assert message.created_at.date()== datetime.now().date()

def test_create_message_success_long_text():
    text = Text('a'*400)
    message = Message(text=text)
    assert message.text == text
    assert message.created_at.date()== datetime.now().date()

def test_create_chat_success():
    title = Title("Chat Title")
    chat = Chat(title=title)
    assert chat.title == title
    assert not chat.messages
    assert chat.created_at.date()== datetime.now().date()


def test_create_chat_title_too_long():
    with pytest.raises(TextTooLongExeption):
        Title('s'*300) 

# def test_add_chat_to_message():
#     title = Title("Chat Title")
#     chat = Chat(title=title)
#     text = Text("Hello, World!")
#     message = Message(text=text)
#     chat.add_message(message)
#     assert message in chat.messages