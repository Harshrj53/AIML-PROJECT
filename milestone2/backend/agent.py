import os
import uuid
from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from graph import create_graph
from utils.pdf_generator import generate_pdf
from fastapi.responses import FileResponse
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Agentic AI Research Assistant API")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ResearchRequest(BaseModel):
    query: str

class ResearchResponse(BaseModel):
    report: dict
    pdf_url: str = None

# In-memory storage for reports (for demo purposes)
reports_db = {}

@app.post("/research", response_model=ResearchResponse)
async def perform_research(request: ResearchRequest):
    if not request.query:
        raise HTTPException(status_code=400, detail="Query cannot be empty")
    
    try:
        runnable = create_graph()
        initial_state = {
            "query": request.query,
            "urls": [],
            "documents": [],
            "summaries": [],
            "insights": "",
            "validated": "",
            "report": {}
        }
        
        final_state = runnable.invoke(initial_state)
        report = final_state.get("report")
        
        if not report:
            raise HTTPException(status_code=500, detail="Failed to generate research report")
        
        # Generate PDF
        report_id = str(uuid.uuid4())
        pdf_filename = f"report_{report_id}.pdf"
        pdf_path = os.path.join(os.getcwd(), pdf_filename)
        generate_pdf(report, pdf_path)
        
        reports_db[report_id] = pdf_path
        
        return {
            "report": report,
            "pdf_url": f"/download/{report_id}"
        }
        
    except Exception as e:
        print(f"Research Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/download/{report_id}")
async def download_report(report_id: str):
    pdf_path = reports_db.get(report_id)
    if not pdf_path or not os.path.exists(pdf_path):
        raise HTTPException(status_code=404, detail="Report not found")
    
    return FileResponse(pdf_path, media_type='application/pdf', filename="research_report.pdf")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
