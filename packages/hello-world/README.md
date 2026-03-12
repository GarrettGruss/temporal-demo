# Hello World Example

This is a simple example showing how to call an LLM from Temporal using the OpenAI Python API library. Being an external API call, the LLM invocation happens in a Temporal Activity.

## This recipe highlights two key design decisions:

- A generic Activity for invoking an LLM API. This Activity can be re-used with different arguments throughout your codebase.
- Configuring the Temporal client with a dataconverter to allow serialization of Pydantic types.
- Retries are handled by Temporal and not by the underlying libraries such as the OpenAI client. This is important because if you leave the client retries on they can interfere with correct and durable error handling and recovery.

- [Source](https://docs.temporal.io/ai-cookbook/hello-world-openai-responses-python)

## Running

Start the Temporal Dev Server:

`temporal server start-dev`

Run the worker:

`uv run python -m worker`

Start execution:

`uv run python -m start_workflow`