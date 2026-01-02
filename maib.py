from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Nexivion Backend",
    version="0.1.0"
)

# TEST MODELİ (AI YOK, ŞİMDİLİK DÜZ MANTIK)
class LeadRequest(BaseModel):
    message: str

class LeadResponse(BaseModel):
    service: str
    budget: str
    urgency: str

@app.get("/")
def root():
    return {"message": "Nexivion Backend is alive 🚀"}

@app.post("/lead/analyze", response_model=LeadResponse)
def analyze_lead(lead: LeadRequest):
    # ŞİMDİLİK SAHTE CEVAP (MOCK)
    return {
        "service": "Web Development",
        "budget": "Medium",
        "urgency": "High"
    }

