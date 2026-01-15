FlexiLoan AI
(Intelligent Loan Structuring Agent for Irregular-Income Workers)

📌 Problem Statement

A large segment of the workforce—such as gig workers, daily wage earners, and freelancers do not have fixed monthly incomes. Traditional loan systems are designed for salaried individuals and fail to adapt to income volatility, leading to:

* Poor loan eligibility assessment
* High EMI stress
* Increased loan defaults
* Financial exclusion of irregular-income workers

There is a need for an adaptive, intelligent loan system that can dynamically analyze income patterns and structure loans responsibly.

🚀 Solution Description

FlexiLoan AI is an agent-based intelligent loan structuring system that dynamically analyzes income patterns and recommends adaptive loan structures.

The system simulates agentic behavior by dividing responsibilities across multiple AI agents:

* Income forecasting
* Risk evaluation
* EMI structuring
* Monitoring & adjustment

Based on recent income trends and existing EMI obligations, the agent generates:

* Risk-aware EMI recommendations
* Flexible loan tenure
* Clear, explainable decisions

The solution is exposed via a FastAPI backend and visualized through an interactive web-based dashboard.

🧠 Agent Workflow (Agentic Architecture)

1. Cashflow Forecasting Agent

  * Analyzes last 6 months income
  * Detects:
  > Average forecast income
  > Income volatility
  > Stability score
  > Income trend (Increasing / Decreasing / Fluctuating)

2. Risk Evaluation Agent

  * Calculates EMI-to-income ratio
  * Adjusts risk based on:
  > Existing loan / EMI obligations
  > Income trend
  * Outputs:
  > Risk score
  > Risk level (Low / Medium / High)
  > Human-readable risk explanation

3. Loan Structuring Agent

  * Generates adaptive EMI and tenure based on risk level
  * Applies conservative adjustments if existing EMIs exist
  * Ensures EMI never exceeds safe income thresholds
  * Outputs:
  > Adaptive EMI
  > Loan tenure
  > Policy reasoning

4. Monitoring Agent

  * Continuously evaluates affordability
  * Suggests EMI increase/reduction if income changes

🖥️ System Architecture

  Frontend (HTML + CSS + Chart.js)
                ↓
         FastAPI Backend
                ↓
         Agent Pipeline
  (Cashflow → Risk → Structuring)

🛠️ Tech Stack Used

Backend

 Python 3.11+
 FastAPI – API framework
 Pydantic – Request validation
 Uvicorn – ASGI server

Frontend

 HTML5
 CSS3
 JavaScript
 Chart.js – Bar & Pie charts

Deployment (Recommended)

 * Backend: Render / Railway
 * Frontend: Vercel / Netlify
 * Version Control: GitHub

⚙️ Setup and Execution Steps

1. Clone the Repository

   git clone https://github.com/<your-username>/FlexiLoan-AI.git
   cd FlexiLoan-AI

2. Create & Activate Virtual Environment (Windows)

   python -m venv venv
   .\venv\Scripts\activate

3. Install Dependencies

   pip install fastapi uvicorn pydantic

4. Run the Backend Server

   python -m uvicorn backend.main:app --reload

5. Open the Frontend

*  Open `frontend/index.html` directly in a browser
*  Access UI via backend root endpoint:

📊 Features Demonstrated

* Agent-based decision making
* Adaptive EMI calculation
* Risk-aware loan structuring
* Interactive dashboard with charts
* Printable loan recommendation report
* Explainable AI outputs

📌 Future Enhancements

* Real-time income monitoring
* Credit score integration
* Bank API connectivity
* Mobile app interface
* Multi-loan portfolio analysis

👤 Author
Darshana Ramesh

M.Tech CSE (Intergrated programme)

Sri Ramakrishna Engineering College
