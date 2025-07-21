# 🕉️ Gita Assistant — LangChain Project

A conversational AI chatbot built with **Gradio**, **LangChain**, and powered by **Groq’s gemma2-9b-it** model. This assistant is designed to offer thoughtful, spiritually grounded responses inspired by the **Bhagavad Gita**, while supporting general-purpose Q&A.

## 🌿 Overview

This chatbot is initialized with a **spiritual system role**:
> “You are a Spiritual Gita AI assistant”

It responds to user queries with philosophical depth, contextual awareness, and a calm, devotional tone. Ideal for seekers, learners, and anyone curious about Gita wisdom.

## ✨ Features

- 🧘 Gita-inspired assistant persona  
- 🔁 Multi-turn conversation memory  
- 🔐 Secure API key input via Gradio textbox  
- 📜 Expandable chat history with role-based formatting  
- ⚡ Powered by Groq’s `gemma2-9b-it` via LangChain  
- 🌐 Hosted on Hugging Face Spaces

## 🛠️ Tech Stack

| Component         | Purpose                                      |
|------------------|----------------------------------------------|
| Gradio           | Web interface for interactive chatbot        |
| LangChain        | Message abstraction and session flow         |
| langchain-groq   | Groq API integration with Gemma model        |
| Python dotenv    | (Optional) local development key loading     |

## 🚀 How to Use

1. Enter your **Groq API key** in the input box  
2. Ask a question — spiritual, philosophical, or general  
3. View the AI’s response and full conversation history  
4. Reflect, explore, or customize the assistant’s role

## 📦 Local Setup 

Either you can directly download/ copy this file to your local file and run it before running please ensure you have all the necessary modules to run the file. Please check requirements.txt file.




| Version | System Persona Description | Link |
|--------|-----------------------------|------|
| **App 1** | Short and simple: Initialized with a concise system message for quick, lightweight responses | [Gita_Assistant_Langchain_project1](https://huggingface.co/spaces/parjun/Gita_Assistant_Langchain_project1) |
| **App 2** | Improvised and context-aware: A detailed system message enhances spiritual empathy and contextual understanding | [Gita_Assistant_Langchain_project_2](https://huggingface.co/spaces/parjun/Gita_Assistant_Langchain_project_2) |



```bash
git clone https://huggingface.co/spaces/parjun/Gita_Assistant_Langchain_project
cd Gita_Assistant_Langchain_project
pip install -r requirements.txt
python app.py
```

## 📚 Chat History Format

- ⚙️ *System Role* — defines assistant’s personality  
- 👤 **User** — your questions and prompts  
- 🤖 **Bot** — AI-generated responses

## 🧪 Customization Ideas

- 🔄 Add persona switcher (e.g. “Guru”, “Comedian”, “Therapist”)  
- 📖 Integrate Gita verse embeddings for retrieval-augmented answers  
- 🔊 Add TTS for voice-based spiritual guidance  
- 🧠 Extend with LangChain tools or memory modules

## 📄 License

Open-source under [MIT License](https://opensource.org/licenses/MIT)

