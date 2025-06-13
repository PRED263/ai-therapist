import google.generativeai as genai
from app.core.config import settings
import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

class GeminiService:
    def __init__(self):
        genai.configure(api_key=settings.GEMINI_API_KEY)
        self.model = genai.GenerativeModel(settings.GEMINI_MODEL)
        
        # Therapeutic prompt template
        self.system_prompt = """
        You are a compassionate AI therapeutic assistant. Your role is to:
        1. Listen actively and empathetically
        2. Ask thoughtful follow-up questions
        3. Provide supportive responses without giving medical advice
        4. Help users explore their thoughts and feelings
        5. Encourage professional help when appropriate
        
        Guidelines:
        - Always be warm, non-judgmental, and supportive
        - Never diagnose or provide medical advice
        - If someone mentions crisis thoughts, respond with immediate care and suggest professional resources
        - Keep responses conversational and human-like
        - Focus on the user's emotional needs
        
        Remember: You are NOT a replacement for professional therapy.
        """
    
    async def generate_response(self, message: str, conversation_history: list = None) -> str:
        try:
            # Build conversation context
            context = self.system_prompt + "\n\nConversation:\n"
            
            if conversation_history:
                for msg in conversation_history[-10:]:  # Last 10 messages for context
                    role = "Human" if msg.get("role") == "user" else "Assistant"
                    context += f"{role}: {msg.get('content')}\n"
            
            context += f"Human: {message}\nAssistant:"
            
            # Generate response
            response = self.model.generate_content(context)
            return response.text
            
        except Exception as e:
            logger.error(f"Error generating response: {str(e)}")
            return "I'm having trouble processing your message right now. How are you feeling at this moment?"

# Global instance
llm_service = GeminiService()