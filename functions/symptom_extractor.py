import os
from openai import OpenAI
from dotenv import load_dotenv
import ast
import logging

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
logger = logging.getLogger(__name__)

def extract_symptoms(text: str) -> list[str]:
    """Extract medical symptoms from natural language using GPT-4."""
    prompt = f"""Extract all medical symptoms from this text. Return ONLY a Python list of symptoms, nothing else.
    
    Text: {text}
    
    Return format: ["symptom1", "symptom2", ...]
    If no symptoms found, return: []
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a medical symptom extractor. Return only a Python list of symptoms, no explanations."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.1
        )
        
        symptoms_str = response.choices[0].message.content.strip()
        symptoms = ast.literal_eval(symptoms_str)
        return symptoms if symptoms else []
    except Exception as e:
        logger.error(f"Error extracting symptoms: {e}")
        return []

