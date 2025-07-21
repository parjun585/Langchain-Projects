import gradio as gr
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_groq import ChatGroq

# Session-wide context I added more contect with the help of ChatGPT to understand and respond better
conversation_history = [SystemMessage(content="""
You are a compassionate, knowledgeable assistant trained on the teachings of the Bhagavad Gita. 
Your role is to provide spiritual guidance and emotional clarity to users by referencing appropriate verses, 
values, and lessons from the Gita in response to their personal struggles, dilemmas, or philosophical questions.

Your tone should be calm, insightful, and empathetic—like that of a wise teacher (guru) guiding a seeker.

When answering, follow this structure:
1. 🕉️ Quote a relevant verse in **original Sanskrit**
2. 📘 Provide its **English meaning**
3. 🧠 Offer a **clear, compassionate explanation** that links the verse to the user's situation
4. 🌱 End with a simple **reflection, suggestion, or Gita value** for the user to contemplate

Avoid giving medical or legal advice. Stay within the spiritual, emotional, and philosophical domains.

Use short paragraphs and clear, mindful language.
""")


]

def gita_chat(api_key, user_input):
    if not api_key:
        return "⚠️ Please enter your Groq API key.", ""

    # Initialize model using the API key
    chat = ChatGroq(model="gemma2-9b-it", temperature=0.5, api_key=api_key)

    # Add user message
    conversation_history.append(HumanMessage(content=user_input))
    
    # Generate response
    response = chat.invoke(conversation_history)
    
    # Add bot message
    conversation_history.append(AIMessage(content=response.content))

    # Format full chat log
    chat_log = ""
    for msg in conversation_history:
        if isinstance(msg, HumanMessage):
            chat_log += f"👤 **User**: {msg.content}\n\n"
        elif isinstance(msg, AIMessage):
            chat_log += f"🤖 **Bot**: {msg.content}\n\n"
    
    return response.content, chat_log

# Build Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("# 🕉️ Conversational Gita Assistant")
    gr.Markdown(
        "This chatbot is designed to offer spiritual guidance, inspired by the teachings of the **Bhagavad Gita**. 🌿\n\n"
        "It has been initialized as a **Spiritual Gita AI assistant** — ready to answer questions and share verses with a compassionate and thoughtful tone. ✨\n\n"
        "Enter your Groq API key to begin the conversation:"
    )

    api_key_input = gr.Textbox(label="🔐 Groq API Key", type="password")
    user_input = gr.Textbox(label="🧘 Your Question or Prompt")
    ask_button = gr.Button("Ask")

    bot_response = gr.Textbox(label="📖 Response", interactive=False)
    full_history = gr.Markdown()

    ask_button.click(
        fn=gita_chat,
        inputs=[api_key_input, user_input],
        outputs=[bot_response, full_history]
    )

demo.launch()
