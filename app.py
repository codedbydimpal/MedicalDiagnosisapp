from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, validator
from functions.symptom_extractor import extract_symptoms
from functions.diagnosis_symptoms import get_diagnosis
from functions.pubmed_articles import fetch_pubmed_articles_with_metadata
from functions.summarize_pubmed import summarize_text
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

app = FastAPI(title="Clinisight AI", description="Medical Diagnosis Assistant", version="1.0.0")


class SymptomInput(BaseModel):
    description: str = Field(
        ..., 
        min_length=10, 
        max_length=2000,
        description="Description of medical symptoms"
    )
    
    @validator('description')
    def validate_description(cls, v):
        if not v or v.isspace():
            raise ValueError('Description cannot be empty or whitespace')
        return v.strip()

@app.post("/diagnosis")
async def diagnosis(data: SymptomInput):
    try:
        logger.info(f"Received diagnosis request (length: {len(data.description)} chars)")
        
        # Extract symptoms
        symptoms = extract_symptoms(data.description)
        if not symptoms:
            raise HTTPException(
                status_code=400, 
                detail="No symptoms could be identified from the description. Please provide more details about your symptoms."
            )
        
        logger.info(f"Extracted {len(symptoms)} symptoms")
        
        # Get diagnosis
        diagnosis_result = get_diagnosis(symptoms)
        
        # Fetch PubMed articles
        pubmed_articles = fetch_pubmed_articles_with_metadata(" ".join(symptoms))
        
        # Smart truncation - only if needed and preserve structure
        MAX_ARTICLE_LENGTH = 3000
        article_text = str(pubmed_articles)
        if len(article_text) > MAX_ARTICLE_LENGTH:
            article_text = article_text[:MAX_ARTICLE_LENGTH - 3] + "..."
        
        summary = summarize_text(article_text)
        
        logger.info("Diagnosis completed successfully")
        
        return {
            "symptoms": symptoms,
            "diagnosis": diagnosis_result,
            "pubmed_summary": summary,
            "articles_count": len(pubmed_articles) if isinstance(pubmed_articles, list) else 0
        }
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error in diagnosis endpoint: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500, 
            detail="An error occurred while processing your request. Please try again."
        )

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "Clinisight AI"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8080, reload=True)
