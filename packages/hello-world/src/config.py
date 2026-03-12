"""configuration constants."""

import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
OPENAI_ORGANIZATION = os.environ["OpenAI-Organization"]
OPENAI_PROJECT = os.environ["OpenAI-Project"]

OPENAI_MODEL = "gpt-5-mini"
TEMPORAL_SERVER = "localhost:7233"
