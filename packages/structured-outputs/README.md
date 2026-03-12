# Structured Outputs with Temporal and OpenAI

The OpenAI Responses API provides the [Structured Outputs API](https://platform.openai.com/docs/guides/structured-outputs) allowing you to request responses conforming to a specific data structure.

In this example, we use structured outputs in a business data cleaning scenario. Structured outputs are also commonly used for tool calling.

OpenAI usually returns the correct type. However, this is not always the case due to the non-deterministic nature of LLMs. When OpenAI returns an incorrect type, Temporal automatically retries the LLM call Activity.

- [Link to article](https://docs.temporal.io/ai-cookbook/structured-output-openai-responses-python)

## Running

Start the Temporal Dev Server:

`temporal server start-dev`

Run the worker:

`uv run python -m worker`

Start execution:

`uv run python -m start_workflow`