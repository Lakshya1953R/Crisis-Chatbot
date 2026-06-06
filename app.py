import streamlit as st
from chatbot import get_response

# ── Page config ────────────────────────────────────
st.set_page_config(
    page_title="Crisis Assistant",
    page_icon="🚨",
    layout="centered"
)

# ── Custom CSS ─────────────────────────────────────
st.markdown("""
    <style>
        .stApp {
            background-color: #0f0f1a;
        }
        .stChatMessage {
            background-color: #1a1a2e;
            border-radius: 12px;
            padding: 10px;
        }
        .stTextInput > div > div > input {
            background-color: #2a2a4a;
            color: #e0e0f0;
            border-radius: 25px;
            border: 1px solid #3a3a5a;
        }
        h1 {
            color: #667eea !important;
        }
        .stCaption {
            color: #6a6a8a !important;
        }
    </style>
""", unsafe_allow_html=True)

# ── Header ─────────────────────────────────────────
st.title("🚨 Crisis Assistant")
st.caption("🟢 Offline — Always Available | First Aid • Disasters • Health • Emotional Support")

# ── Quick suggestions ──────────────────────────────
st.write("**Quick topics:**")
cols = st.columns(5)
suggestions = [
    ("😰 Anxiety",  "I feel very anxious"),
    ("🌊 Flood",    "There is a flood"),
    ("🩸 Bleeding", "I am bleeding badly"),
    ("💙 Lonely",   "I feel very lonely"),
    ("🔥 Fire",     "There is a fire"),
]

for i, (label, message) in enumerate(suggestions):
    if cols[i].button(label, use_container_width=True):
        st.session_state.pending = message

# ── Chat history ───────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "👋 Hello! I'm your offline crisis assistant.\n\nI can help with first aid, natural disasters, health emergencies, and emotional support.\n\nHow can I help you today?"
        }
    ]

if "pending" not in st.session_state:
    st.session_state.pending = None

# ── Display chat history ───────────────────────────
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ── Handle suggestion click ────────────────────────
if st.session_state.pending:
    user_input = st.session_state.pending
    st.session_state.pending = None

    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )
    with st.chat_message("user"):
        st.markdown(user_input)

    response = get_response(user_input)
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )
    with st.chat_message("assistant"):
        st.markdown(response)

# ── User input ─────────────────────────────────────
user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )
    with st.chat_message("user"):
        st.markdown(user_input)

    response = get_response(user_input)
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )
    with st.chat_message("assistant"):
        st.markdown(response)