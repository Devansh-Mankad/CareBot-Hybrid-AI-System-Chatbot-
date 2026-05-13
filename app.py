import streamlit as st
import time
from brain import get_carebot_response, listen_to_user

st.set_page_config(page_title="CareBot AI", page_icon="🩺", layout="wide")
st.markdown("""
<style>
.main { background-color: #f8f9fa; }

[data-testid="stSidebar"] {
    border-right: 1px solid #dee2e6;
}

.stChatMessage {
    border-radius: 12px;
    margin-bottom: 10px;
    padding: 6px;
}

.stChatInputContainer {
    padding-right: 80px !important;
}

button[data-testid="baseButton-mic_btn"] {
    position: fixed;
    bottom: 14px;
    right: 20px;
    z-index: 999;

    width: 50px;
    height: 50px;
    border-radius: 50%;

    background-color: #0d6efd;
    color: white;
    font-size: 22px;

    border: none;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
}

button[data-testid="baseButton-mic_btn"]:hover {
    background-color: #0b5ed7;
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)

# SIDEBAR
with st.sidebar:
    st.title("🩺 Patient Dashboard")
    st.info("CareBot analyzes your symptoms in real-time.")

    if st.button("🔄 Clear Consultation", use_container_width=True):
        st.session_state.messages = []
        st.session_state.predictions = []
        st.rerun()


# HEADER
st.title("CareBot: Rural Healthcare Assistant")
st.caption("AI-Powered Preliminary Diagnostic Support | 2026 Edition")

# SESSION
if "messages" not in st.session_state:
    st.session_state.messages = []

if "predictions" not in st.session_state:
    st.session_state.predictions = []

# CHAT DISPLAY
for msg in st.session_state.messages:
    avatar = "🩺" if msg["role"] == "assistant" else None
    with st.chat_message(msg["role"], avatar=avatar):
        st.markdown(msg["content"])

# INPUT
prompt = st.chat_input("Tell me how you are feeling...")
mic_clicked = st.button("🎙️", key="mic_btn")

user_query = None

if prompt:
    user_query = prompt
elif mic_clicked:
    with st.spinner("🎙️ Listening..."):
        voice = listen_to_user()
        if voice:
            user_query = voice
        else:
            st.warning("Could not understand audio")

if user_query:
    st.session_state.messages.append({"role": "user", "content": user_query})

    with st.chat_message("user"):
        st.markdown(user_query)

    with st.chat_message("assistant", avatar="🩺"):
        placeholder = st.empty()

        with st.spinner("Analyzing symptoms..."):
            response, predictions = get_carebot_response(
                user_query,
                st.session_state.messages
            )

        st.session_state.predictions = predictions

        # Typing animation
        full_text = ""
        for word in response.split(" "):
            full_text += word + " "
            time.sleep(0.015)
            placeholder.markdown(full_text + "▌")

        placeholder.markdown(full_text)

        st.session_state.messages.append({
            "role": "assistant",
            "content": full_text
        })

    st.rerun()