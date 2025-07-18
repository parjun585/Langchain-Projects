
# 💬 Simple Conversational Bot

A lightweight chatbot built with **Streamlit** and **LangChain**, powered by **Groq’s `gemma2-9b-it`** model. This app supports multi-turn conversations with a humorous system persona and displays full chat history for transparency.

## 🧠 Overview

This project demonstrates how to build a conversational chatbot using:
- **LangChain’s message framework** (`HumanMessage`, `AIMessage`, `SystemMessage`)
- **Groq’s LLM integration** via `ChatGroq`
- **Streamlit** for an interactive web UI

## ✨ Features

- 🔥 Real-time Q&A with Groq’s `gemma2-9b-it` model  
- 🧵 Session-aware conversation using `st.session_state`  
- 🎭 Customizable system persona (default: comedian assistant)  
- 📜 Expandable chat history with role-based formatting  
- 🧪 Simple and extensible codebase for experimentation

## 🛠️ Tech Stack

| Tool         | Purpose                                 |
|--------------|------------------------------------------|
| Streamlit    | Web interface for user interaction       |
| LangChain    | Message abstraction and session memory   |
| ChatGroq     | LLM backend using Groq’s Gemma model     |
| dotenv       | Secure environment variable management   |

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/parjun585/Langchain-Projects.git
cd Langchain-Projects/Simple Conversational Bot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is missing, install manually:
```bash
pip install streamlit langchain langchain-groq python-dotenv
```

### 3. Set Up Environment Variables

Create a `.env` file in the root directory and add your Groq credentials:
```
GROQ_API_KEY=your_api_key_here
```

### 4. Run the App

```bash
streamlit run app.py
```

## 🧩 How It Works

- The chatbot is initialized with a **SystemMessage**:  
  `"You are a comedian AI assistant"`  
- User input is captured via `st.text_input`  
- Messages are stored in `st.session_state['flowmessages']`  
- Responses are generated using `chat.invoke()`  
- Full chat history is displayed in an expandable section

## 📚 Chat History Format

- 👤 **User** messages  
- 🤖 **Bot** responses  
- ⚙️ *System Role* initialization  

## 🧪 Customization Ideas

- 🔄 Swap `gemma2-9b-it` with other Groq or OpenAI models  
- 🧠 Add RAG or document loaders for contextual Q&A  
- 🎭 Change system persona to suit different use cases  
- 📦 Modularize response logic for streaming or async support  

---

Would you like me to help you scaffold a `requirements.txt`, add modular callbacks, or integrate streaming responses next?
