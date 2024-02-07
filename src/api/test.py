from fastapi import APIRouter, Body
import logging
from config import rabbit_connection, QueueEnum

test_router = APIRouter(prefix='/test', tags=['Test api'])


@test_router.post('/')
async def process(
        queue_name: QueueEnum,
        message: dict = Body(default={
            'type': 'from Alexandr',
            'message': 'Hello, my friend'
        }),
):
    await rabbit_connection.send_messages(
        messages=message, routing_key=queue_name
    )
    logging.info(f"""QUEUE |{queue_name.value}| MESSAGE {message}""")
    return f"""{message} successfully sent to {queue_name.value}"""
