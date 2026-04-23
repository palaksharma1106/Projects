import streamlit as st
from memory import get_bot_response

# page config
st.set_page_config(page_title="AI Chatbot", page_icon="https://i.pinimg.com/736x/a6/57/df/a657df04b3d9a5a9476ed20534b2e0b8.jpg")

# custom CSS
st.markdown("""
<style>

.stApp {
    background-image: url("https://i.pinimg.com/1200x/9b/c1/45/9bc14505d003f56e2095478e7746dd7c.jpg");
    background-size: cover;
    background-position: center;
}

.chat-user {
    background-color: #FC7256;
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 8px;
}

.chat-bot {
    background-color: #FF709D;
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 8px;
}

.stButton button {
    background-color: #4CAF50;
    color: white;
    border-radius: 8px;
}

</style>
""", unsafe_allow_html=True)

st.title("🤖 AI Chatbot with Memory")

# initialize messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# display chat
for msg in st.session_state.messages:

    if msg["role"] == "You":
        st.markdown(
            f'<div class="chat-user"><b>You:</b> {msg["content"]}</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f'<div class="chat-bot"><b>Bot:</b> {msg["content"]}</div>',
            unsafe_allow_html=True
        )

# input box
user_input = st.text_input("Type your message")

col1, col2 = st.columns(2)

# send button
with col1:
    if st.button("Send 💬"):
        if user_input:
            st.session_state.messages.append(
                {"role": "You", "content": user_input}
            )

            reply = get_bot_response(user_input)

            st.session_state.messages.append(
                {"role": "Bot", "content": reply}
            )

            st.rerun()

# clear chat button
with col2:
    if st.button("Clear Chat 🗑"):
        st.session_state.messages = []
        st.rerun()
