import os 
from dotenv import load_dotenv
from openai import OpenAI 
import logging

load_dotenv()
logger = logging.getLogger(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_diagnosis(symptoms: list[str]) -> str:
    """Get medical diagnosis based on symptoms."""
    if not symptoms:
        return "No symptoms provided for diagnosis."
    
    prompt = f"Patient has symptoms: {', '.join(symptoms)}. Suggest possible medical diagnoses and potential treatment options. Keep response concise and informative."

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful medical assistant. Provide informative but cautious medical guidance. Always recommend consulting with healthcare professionals."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=500
        )

        return response.choices[0].message.content.strip()
    except Exception as e:
        logger.error(f"Error getting diagnosis: {e}")
        return "Unable to generate diagnosis at this time. Please try again later."


