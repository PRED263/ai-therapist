# Test if our modules can be imported
try:
    from app.core.config import settings
    print("✅ Config imported successfully")
    print(f"Project name: {settings.PROJECT_NAME}")
except Exception as e:
    print(f"❌ Config import failed: {e}")

try:
    from app.models.chat import ChatMessage, ChatRequest
    print("✅ Models imported successfully")
except Exception as e:
    print(f"❌ Models import failed: {e}")

try:
    from app.services.llm_service import llm_service
    print("✅ LLM service imported successfully")
except Exception as e:
    print(f"❌ LLM service import failed: {e}")