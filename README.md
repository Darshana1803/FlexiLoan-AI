FlexiLoan AI
(Intelligent Loan Structuring Agent for Irregular-Income Workers)



📌 What is the Project?

FlexiLoan AI is an agent-based intelligent loan structuring system designed for workers with irregular or volatile income such as gig workers, freelancers, and informal earners.

Traditional loan systems use fixed EMI schedules that do not adapt to income fluctuations. This project addresses that limitation by using autonomous AI agents to dynamically structure loan repayment plans based on income patterns, repayment risk, and existing financial obligations.

⚙️ How the Project Works

The system follows a multi-agent workflow, where each agent performs a specialized task and collectively makes intelligent loan decisions.

🔹 Step 1: Income Input

The user enters the last six months of income and specifies whether they have any existing loans or EMIs.

🔹 Step 2: Cashflow Forecasting Agent

This agent analyzes recent income history to:

Forecast average monthly income

Measure income volatility

Determine income stability and trend

🔹 Step 3: Risk Evaluation Agent

Based on forecasted income, existing EMIs, and income trend, this agent:

Calculates EMI-to-income ratio

Assigns a repayment risk level (Low / Medium / High)

🔹 Step 4: Loan Structuring Agent

Using the risk assessment, this agent:

Determines an adaptive EMI amount

Adjusts loan tenure dynamically

Ensures EMI remains affordable under income fluctuations

🔹 Step 5: Monitoring & Adjustment Agent

The monitoring agent continuously evaluates affordability and suggests EMI adjustments to prevent financial stress or loan default.

🔹 Step 6: Visualization & Report

The system displays:

Forecasted income

Risk assessment

Adaptive EMI & tenure

Income trend (bar chart)

Risk vs affordability (pie chart)

Printable loan summary

🛠️ Technologies Used
Backend

Python

FastAPI – API framework for agent orchestration

Pydantic – Input validation and data modeling

Frontend

HTML

CSS

JavaScript

Chart.js – Data visualization (bar & pie charts)

Development & Deployment

Git & GitHub – Version control

Uvicorn – ASGI server
