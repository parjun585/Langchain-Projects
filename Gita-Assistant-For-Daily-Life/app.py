import gradio as gr
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_groq import ChatGroq

# Session-wide context
conversation_history = [SystemMessage(content="You are a Spiritual Gita AI assistant")


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
# version 1: I am thinking that if I am using a more defined SystemMesssage maybe I can improvise on this part
