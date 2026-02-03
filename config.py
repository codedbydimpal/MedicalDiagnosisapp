import os
from dotenv import load_dotenv

load_dotenv()

# Validate required environment variables
REQUIRED_ENV_VARS = ["OPENAI_API_KEY"]

for var in REQUIRED_ENV_VARS:
    if not os.getenv(var):
        raise EnvironmentError(
            f"Required environment variable {var} is not set. "
            f"Please create a .env file with {var}=your_key_here"
        )

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Application constants
MAX_ARTICLE_LENGTH = 3000
MIN_TEXT_LENGTH = 10
