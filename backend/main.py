from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from agents.cashflow_agent import cashflow_forecast
from agents.risk_agent import evaluate_risk
from agents.structuring_agent import structure_loan


# -----------------------------
# FastAPI App
# -----------------------------
app = FastAPI(title="Intelligent Loan Structuring Agent")


# -----------------------------
# CORS (allow frontend access)
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -----------------------------
# Health Check
# -----------------------------
@app.get("/health")
def health():
    return {"status": "Agent running successfully"}


# -----------------------------
# Input Model
# -----------------------------
class IncomeInput(BaseModel):
    income_history: list[int]
    has_existing_emi: bool


# -----------------------------
# Core Agent Endpoint
# -----------------------------
@app.post("/run-agent")
def run_agent(data: IncomeInput):
    try:
        # 1️⃣ Cashflow Agent
        cashflow = cashflow_forecast(data.income_history)

        # 2️⃣ Risk Agent
        risk = evaluate_risk(
            forecast_income=cashflow["forecast_income"],
            base_emi=2000,
            has_existing_emi=data.has_existing_emi,
            income_trend=cashflow["trend"]
        )

        # 3️⃣ Loan Structuring Agent
        loan = structure_loan(
            forecast_income=cashflow["forecast_income"],
            risk_level=risk["risk_level"],
            has_existing_emi=data.has_existing_emi
        )

        return {
            "income_history": data.income_history,
            "has_existing_emi": data.has_existing_emi,
            "cashflow_agent": cashflow,
            "risk_agent": risk,
            "loan_structuring_agent": loan
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# -----------------------------
# Serve Frontend UI
# -----------------------------
@app.get("/", response_class=HTMLResponse)
def serve_ui():
    try:
        with open("frontend/index.html", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return HTMLResponse(
            "<h2>Frontend not found</h2><p>Check frontend/index.html</p>",
            status_code=404
        )
