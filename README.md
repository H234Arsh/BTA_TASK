🩸 Blood Test Analyser
This project automates the analysis of blood test reports using artificial intelligence (AI) agents, PDF parsing, and background task processing. The goal is to assist patients and doctors by extracting relevant health insights from lab reports in a structured and scalable way.

✅ Overview
Blood Test Analyser is a Python-based backend application that uses:

FastAPI for serving API endpoints.

Celery for handling long-running tasks asynchronously (like reading and analyzing PDFs).

SQLAlchemy with PostgreSQL for database interaction.

CrewAI agents to mimic doctor-like reasoning and extract insights from test results.

Secure PDF parsing and structured result storage.

✅ What This Repository Contains
A complete Celery task system to analyze PDFs.

A FastAPI app to trigger and monitor analysis.

Database models for users and analysis results.

AI agent integration for medical insight generation.

🐞 Bugs Found & How They Were Fixed
Celery app not loading properly:
This was due to incorrect module references. It was resolved by ensuring that the Celery instance is imported correctly using the module path celery_app.celery_app.

OpenAI API key leaked in Git history:
GitHub blocked the push due to secret scanning. The key was removed from all commits using BFG Repo Cleaner, and the .env file was added to .gitignore to prevent future exposure.

Branch mismatch error (master vs main):
The project was initialized with the main branch, but push attempts were made to master. This was fixed by using the correct branch name and setting the upstream accordingly.

Missing dependencies like opentelemetry:
Errors occurred due to incomplete installations. Dependencies were updated and explicitly installed using pip.

Large push errors and disconnects:
These were caused by attempting to push large data files and secrets. Git LFS (Large File Storage) can be considered for future large files. Current fix included commit clean-up and repo slimming.

🛠️ Setup & Usage (Explained)
To use this project, follow these general steps:

Clone the repository to your local machine.

Set up a virtual environment and install dependencies listed in requirements.txt.

Create a .env file with your OpenAI API key, database connection string, and other sensitive values. This file must not be committed to GitHub to avoid exposing secrets.

Run the FastAPI application to serve API endpoints for uploading and processing reports.

Start the Celery worker, which listens for tasks such as analyzing a PDF.

Upload a PDF file through the API or a script. The Celery task will parse the content, analyze it using AI, and store the results.

Fetch the analysis results for a given user using their username or ID.

📌 Key Features
Background task processing for non-blocking performance.

Medical insight extraction using LLM-powered agents.

Database integration for user and result management.

Modular, production-ready Python project layout.

📑 API Documentation (Summarized)
The FastAPI framework auto-generates OpenAPI (Swagger) documentation. Once the server is running, you can view it by visiting:

http://localhost:8000/docs

This documentation allows you to test:

Uploading a PDF

Getting results for a user

Health check endpoint

