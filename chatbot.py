import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure the page
st.set_page_config(
    page_title="Deal Intelligence Chatbot",
    page_icon="📊",
    layout="wide"
)

def initialize_openai():
    """Initialize OpenAI client with API key"""
    api_key = os.getenv("OPENAI_API_KEY")
    
    if api_key:
        try:
            return OpenAI(api_key=api_key)
        except Exception as e:
            st.error(f"Invalid API key: {str(e)}")
            return None
    else:
        st.error("❌ Please add OPENAI_API_KEY to your .env file")
        return None

def load_markdown_file():
    """Auto-load the markdown.md file"""
    try:
        with open("markdown.md", "r", encoding="utf-8") as f:
            content = f.read()
        return content
    except FileNotFoundError:
        st.error("❌ markdown.md file not found in current directory")
        return None
    except Exception as e:
        st.error(f"❌ Error loading file: {str(e)}")
        return None

def answer_question(client, markdown_content, question, conversation_history):
    """Use OpenAI to answer questions about the markdown content"""
    
    # Build conversation context
    messages = [
        {
            "role": "system", 
            "content": f"""You are a helpful sales assistant that answers questions about opportunity analyses. 
            
            You have access to this opportunity analysis report:
            
            {markdown_content}
            
            Instructions:
            - Answer questions directly and concisely based ONLY on the information in the report
            - If information isn't in the report, say "This information is not available in the analysis"
            - For numerical values, provide exact numbers from the report
            - For stakeholder questions, include confidence levels when available
            - Be conversational but professional
            - Focus on actionable insights for sales reps"""
        }
    ]
    
    # Add conversation history
    for msg in conversation_history:
        messages.append(msg)
    
    # Add current question
    messages.append({"role": "user", "content": question})
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.0,
            max_tokens=500
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    st.title("📊 Deal Intelligence Chatbot")
    st.markdown("Ask questions about your opportunity to get quick insights before client calls!")
    
    # Initialize OpenAI client
    client = initialize_openai()
    if not client:
        st.stop()
    
    # Auto-load markdown file
    markdown_content = load_markdown_file()
    if not markdown_content:
        st.stop()
    
    st.success("✅ Analysis loaded successfully!")
    
    # Clear conversation button
    if st.button("🗑️ Clear Conversation"):
        st.session_state.conversation_history = []
        st.rerun()
    
    # Initialize session state
    if "conversation_history" not in st.session_state:
        st.session_state.conversation_history = []
    
    # Display conversation history
    if st.session_state.conversation_history:
        st.subheader("💬 Conversation History")
        for msg in st.session_state.conversation_history:
            if msg["role"] == "user":
                st.write(f"**You:** {msg['content']}")
            else:
                st.write(f"**Assistant:** {msg['content']}")
        st.divider()
    
    # Question input
    question = st.text_input(
        "Ask a question about this opportunity:",
        placeholder="e.g., What's the deal value? Who is the economic buyer?"
    )
        
    # Process question
    if question and st.button("Ask", type="primary"):
        with st.spinner("Thinking..."):
            answer = answer_question(client, markdown_content, question, st.session_state.conversation_history)
        
        # Add to conversation history
        st.session_state.conversation_history.append({"role": "user", "content": question})
        st.session_state.conversation_history.append({"role": "assistant", "content": answer})
        
        # Keep only last 10 exchanges to manage context
        if len(st.session_state.conversation_history) > 20:
            st.session_state.conversation_history = st.session_state.conversation_history[-20:]
        
        st.rerun()

if __name__ == "__main__":
    main() 