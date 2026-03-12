"""Create the Worker.

Create the process for executing Activities and Workflows.
We configure the Temporal client with pydantic_data_converter
so Temporal can serialize/deserialize output of the OpenAI SDK.
"""

import asyncio

from temporalio.client import Client
from temporalio.worker import Worker

from workflows.hello_world_workflow import HelloWorld
from activities import openai_responses
from temporalio.contrib.pydantic import pydantic_data_converter

from config import TEMPORAL_SERVER


async def main():
    client = await Client.connect(
        TEMPORAL_SERVER,
        data_converter=pydantic_data_converter,
    )

    worker = Worker(
        client,
        task_queue="hello-world-python-task-queue",
        workflows=[
            HelloWorld,
        ],
        activities=[
            openai_responses.create,
        ],
    )
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
