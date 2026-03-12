"""Create the Workflow.

In this example, we take the user input and generate a response in haiku format,
using the OpenAI Responses Activity. The Workflow returns result.output_text
from the OpenAI Response.

As per usual, the Activity retry configuration is set here in the Workflow.
In this case, a retry policy is not specified so the default retry policy is
used (exponential backoff with 1s initial interval, 2.0 backoff coefficient,
max interval 100x initial, unlimited attempts, no non-retryable errors).
"""

from temporalio import workflow
from datetime import timedelta
from config import OPENAI_MODEL

from activities import openai_responses


@workflow.defn
class HelloWorld:
    @workflow.run
    async def run(self, input: str) -> str:
        system_instructions = "You only respond in haikus."
        result = await workflow.execute_activity(
            openai_responses.create,
            openai_responses.OpenAIResponsesRequest(
                model=OPENAI_MODEL,
                instructions=system_instructions,
                input=input,
            ),
            start_to_close_timeout=timedelta(seconds=30),
        )
        return result.output_text
