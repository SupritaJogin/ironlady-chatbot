import streamlit as st

# FAQ knowledge base
faq = {
    "programs": "Iron Lady offers programs like Leadership Essentials, Advanced Coaching, and more.",
    "duration": "Leadership Essentials runs for 2 full days (Sat-Sun, 9 AM - 7 PM).",
    "mode": "Programs are live online (Zoom).",
    "certificate": "Yes, certificates are provided to participants.",
    "mentors": "Coaches include ex-CEOs, entrepreneurs, and leadership experts."
}

st.title("💬 Iron Lady FAQ Chatbot")

# User input
q = st.text_input("Ask me about Iron Lady programs:")

if st.button("Ask"):
    q_lower = q.lower()
    answers = []

    for key, value in faq.items():
        if key in q_lower:
            answers.append(value)

    if answers:
        for ans in answers:
            st.success(ans)
    else:
        st.warning("Sorry, I don’t know that yet. Try asking about programs, duration, mode, certificates, or mentors.")
