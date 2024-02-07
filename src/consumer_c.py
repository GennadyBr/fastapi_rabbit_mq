import asyncio
import logging
import aio_pika
import datetime
import json

from aio_pika.abc import AbstractIncomingMessage

from config import RABBIT_URL
from localizations import consumer
from config import QueueEnum

PARALLEL_TASKS = 10

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[
        logging.FileHandler("logs/consumer.log"),
        logging.StreamHandler()
    ]
)

###### QUEUE_CCC ######
queue_name = QueueEnum.QUEUE_CCC.value


def record_file(message: dict):
    with open(f'logs/{queue_name}_message.txt', 'a') as f:
        print(f'{datetime.datetime.now()} | QUEUE {queue_name} | MESSAGE: {message}', file=f)
    logging.info(f"""QUEUE {queue_name}""")
    logging.info(f"""MESSAGE {message}""")


async def message_router(
        message: AbstractIncomingMessage,
) -> None:
    async with message.process():
        body = json.loads(message.body.decode())
        return record_file(body)


async def main() -> None:
    connection = await aio_pika.connect_robust(RABBIT_URL)
    async with connection:
        channel = await connection.channel()
        await channel.set_qos(prefetch_count=PARALLEL_TASKS)
        queue = await channel.declare_queue(queue_name, auto_delete=True)

        logging.info(consumer.STARTED)

        await queue.consume(message_router)

        try:
            await asyncio.Future()
        finally:
            await connection.close()


if __name__ == "__main__":
    logging.info(consumer.STARTING)
    asyncio.run(main())
