import streamlit as st
import requests

st.set_page_config(page_title="Grok-3 Mini Chat", layout="centered")
st.title("💬 Chat with Grok-3 Mini (via xAI API)")

api_key = st.text_input("🔑 Enter your xAI API Key", type="password")

user_input = st.text_area("✍️ Your Prompt", height=200)
submit = st.button("Ask Grok")

if submit and api_key and user_input:
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "grok-3-mini-beta",
        "messages": [
            {"role": "user", "content": user_input}
        ]
    }

    with st.spinner("Thinking..."):
        res = requests.post("https://api.x.ai/v1/chat/completions", headers=headers, json=data)

    if res.status_code == 200:
        response = res.json()["choices"][0]["message"]["content"]
        st.markdown("### 🤖 Grok says:")
        st.write(response)
    else:
        st.error(f"Error: {res.status_code} — {res.text}")
