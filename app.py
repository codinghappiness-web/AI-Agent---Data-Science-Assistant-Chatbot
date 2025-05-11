import streamlit as st
from agent import DataScienceAssistant

st.set_page_config(page_title="AI Data Science Assistant", page_icon="🧠")

st.title("🧠 AI Data Science Assistant")
st.markdown("Ask anything related to data science, machine learning, or Python.")

if "history" not in st.session_state:
    st.session_state.history = []

assistant = DataScienceAssistant()

with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Your Question:", "")
    submitted = st.form_submit_button("Ask")

    if submitted and user_input:
        with st.spinner("Thinking..."):
            reply = assistant.ask(user_input)
            st.session_state.history.append(("You", user_input))
            st.session_state.history.append(("Assistant", reply))

# Display chat history
for speaker, text in reversed(st.session_state.history):
    if speaker == "You":
        st.markdown(f"**🧍 {speaker}:** {text}")
    else:
        st.markdown(f"**🤖 {speaker}:** {text}")
