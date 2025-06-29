# main.py
from task import help_patients_task
from models import Base, engine

# Make sure tables exist
Base.metadata.create_all(engine)

if __name__ == "__main__":
    test_file_path = r"C:\Users\VAISHANAVI\blood test analyser\blood_test_report.pdf"
    test_username = "john_doe"

    print("⏳ Enqueuing blood test analysis task...")
    result = help_patients_task.delay(test_file_path, test_username)
    print(f"📨 Task ID: {result.id}")
    print("🕒 Waiting for result...")

    try:
        output = result.get(timeout=30)
        print("✅ Task Result:")
        print(output)
    except Exception as e:
        print(f"❌ Error getting result: {e}")
