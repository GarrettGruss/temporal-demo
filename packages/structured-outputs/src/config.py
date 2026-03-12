"""configuration constants."""

import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
OPENAI_ORGANIZATION = os.environ["OPENAI_ORGANIZATION"]
OPENAI_PROJECT = os.environ["OPENAI_PROJECT"]

OPENAI_MODEL = "gpt-5-mini"
TEMPORAL_SERVER = "localhost:7233"
