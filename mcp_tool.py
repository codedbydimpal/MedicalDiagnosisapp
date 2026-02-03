from mcp.server.fastmcp import FastMCP 
from functions.symptom_extractor import extract_symptoms
from functions.diagnosis_symptoms import get_diagnosis
from functions.pubmed_articles import fetch_pubmed_articles_with_metadata
from functions.summarize_pubmed import summarize_text
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

mcp = FastMCP("Clinisight AI")


@mcp.tool()
async def clinisight_ai(symptom_text: str):
    """Analyze symptoms and provide diagnosis with research."""
    try:
        logger.info(f"Processing MCP request for: {symptom_text[:50]}...")
        
        symptoms = extract_symptoms(symptom_text)
        if not symptoms:
            return {
                "error": "No symptoms identified",
                "message": "Please provide a clearer description of symptoms"
            }
        
        diagnosis_result = get_diagnosis(symptoms)
        pubmed_articles = fetch_pubmed_articles_with_metadata(" ".join(symptoms))
        
        article_text = str(pubmed_articles)
        if len(article_text) > 3000:
            article_text = article_text[:2997] + "..."
            
        summary = summarize_text(article_text)

        return {
            "symptoms": symptoms,
            "diagnosis": diagnosis_result,
            "pubmed_summary": summary,
            "status": "success"
        }
    except Exception as e:
        logger.error(f"Error in MCP tool: {e}", exc_info=True)
        return {
            "error": str(e),
            "status": "failed"
        }




if __name__ == "__main__":
    mcp.run(transport="stdio")
