# Multi-Provider AI Chatbot

This project is a simple, web-based chatbot application built with Python, FastAPI, and LangChain. It features a basic frontend and a backend that can connect to multiple Large Language Model (LLM) providers, including Ollama, Google Gemini, and Groq(DeepseekR1).

## Features

-   **FastAPI Backend**: A robust and fast web server for handling chat and authentication requests.
-   **Simple Frontend**: A clean user interface for login and chat, built with HTML, CSS, and vanilla JavaScript.
-   **Multi-LLM Support**: Easily switch between different LLM providers:
    -   Ollama (for local models like Llama 2/3)
    -   Google Gemini
    -   Groq
-   **Environment-based Configuration**: API keys are managed securely using a `.env` file.

## Setup and Installation

Follow these steps to get the chatbot running on your local machine.

### 1. Prerequisites

-   Python 3.8+
-   A virtual environment tool (like `venv`)

### 2. Create and Activate Virtual Environment

Open your terminal in the project directory (`c:\chatbot\`) and run the following commands:

**For Windows (PowerShell):**
```powershell
.venv/Scripts/Activate.ps1
```

**For Windows (Command Prompt):**
```cmd
.venv\Scripts\activate
```

### 3. Install Dependencies

With your virtual environment activated, install the required Python packages from `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a file named `.env` in the root of the project directory (`c:\chatbot\`). Add the API keys for the services you want to use.

```env
# Add the API key for the provider you want to use
GROQ_TOKEN="your_groq_api_key_here"
GEMINI_TOKEN="your_google_api_key_here"
```
*Note: You only need to provide the key for the model you intend to use.*

## How to Run

### 1. Select the LLM Provider

Open `c:\chatbot\main.py` and find the line where `LLMManager` is initialized. Change the `model_type` to `"groq"`, `"gemini"`, or `"ollama"` to switch providers.

### 2. Start the Server

Run the main application file from your terminal:
```bash
python main.py
```