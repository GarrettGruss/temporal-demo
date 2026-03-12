"""Create the Activity.

We create a wrapper for the create method of the AsyncOpenAI client object.
This is a generic Activity that invokes the OpenAI LLM.

We set max_retries=0 when creating the AsyncOpenAI client. This moves the
responsibility for retries from the OpenAI client to Temporal.

In this implementation, we include only the instructions and input argument, but
it could be extended to others.
"""

from temporalio import activity
from openai import AsyncOpenAI
from openai.types.responses import Response
from dataclasses import dataclass
from config import OPENAI_API_KEY


# Temporal best practice: Create a data structure to hold the request parameters.
@dataclass
class OpenAIResponsesRequest:
    model: str
    instructions: str
    input: str


@activity.defn
async def create(request: OpenAIResponsesRequest) -> Response:
    # Temporal best practice: Disable retry logic in OpenAI API client library.
    client = AsyncOpenAI(max_retries=0, api_key=OPENAI_API_KEY)

    resp = await client.responses.create(
        model=request.model,
        instructions=request.instructions,
        input=request.input,
        timeout=15,
    )

    return resp
