# task.py
from celery_app import celery_app
from agents import doctor
from tools import DataTools
from models import SessionLocal, AnalysisResult, User
import json
import os
from models import Base, engine  # Add this if not already imported

# Ensure DB tables are created when Celery worker starts
Base.metadata.create_all(engine)

@celery_app.task(name="help_patients_task")
def help_patients_task(patient_pdf_path: str, username: str = None):
    """Celery task: Analyze a blood test PDF and store results."""
    db = SessionLocal()
    try:
        if not os.path.exists(patient_pdf_path):
            raise FileNotFoundError(f"File not found: {patient_pdf_path}")

        data = DataTools.read_data_tool(patient_pdf_path)
        insights = DataTools.analyze_data_tool(data)

        user = None
        if username:
            user = db.query(User).filter(User.username == username).first()
            if not user:
                user = User(username=username, email="")
                db.add(user)
                db.commit()
                db.refresh(user)

        result = AnalysisResult(
            user_id=user.id if user else None,
            input_path=patient_pdf_path,
            result_json=json.dumps(insights)
        )
        db.add(result)
        db.commit()

        return insights

    except Exception as e:
        db.rollback()
        return {"error": str(e)}

    finally:
        db.close()
