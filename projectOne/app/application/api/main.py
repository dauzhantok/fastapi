from fastapi import FastAPI

app = FastAPI()

def create_app():
    return FastAPI(
        title = 'Kafka Chat',
        docs_url = '/api/docs',
        description = 'A simple chat application using Kafka and FastAPI',
        debug = True,
    )