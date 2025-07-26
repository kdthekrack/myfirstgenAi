from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

class LLMManager:
    def __init__(self, model_type="ollama"):
        self.model_type = model_type
        if model_type == "ollama":
            self.llm = ChatOllama(model="llama2", temperature=0.1)
        elif model_type == "gemini":
            gemini_key = os.getenv('GEMINI_TOKEN')
            self.llm = ChatGoogleGenerativeAI(
                model="gemini-pro", 
                google_api_key=gemini_key,
                temperature=0.1
            )
        elif model_type == "groq":
            groq_key = os.getenv('GROQ_TOKEN')
            self.llm = ChatGroq(
                temperature=0.1,
                groq_api_key=groq_key,
                model_name="deepseek-r1-distill-llama-70b"
            )
        else:
            raise ValueError("Invalid model type. Use 'ollama', 'gemini', or 'grok'")

    def chat(self, message):
        try:
            response = self.llm.invoke(message)
            return response.content
        except Exception as e:
            return f"Error processing message: {str(e)}"

    def get_model_type(self):
        return self.model_type