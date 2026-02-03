import os
from openai import OpenAI
from dotenv import load_dotenv
import logging

load_dotenv()
logger = logging.getLogger(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Import constant from config
from config import MIN_TEXT_LENGTH

def summarize_text(text: str) -> str:
    """Summarize medical research text."""
    if not text or len(text.strip()) < MIN_TEXT_LENGTH:
        return "No content available to summarize."
    
    prompt = f"Summarize the following medical research information in a clear, concise manner:\n\n{text}"

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a medical research summarizer. Provide clear, accurate summaries of medical literature."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=400
        )

        return response.choices[0].message.content.strip()
    except Exception as e:
        logger.error(f"Error summarizing text: {e}")
        return "Unable to generate summary at this time."

