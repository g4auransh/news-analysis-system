import streamlit as st
from engine import process_text

st.title("Intelligent News Summarizer")
text = st.text_area("Paste News Article:")

if st.button("Analyze"):
    summary, sent, entities = process_text(text)
    st.subheader("Summary")
    st.write(summary)
    st.subheader("Sentiment")
    st.write(f"Label: {sent['label']}, Score: {round(sent['score'], 4)}")
    st.subheader("Key Entities")
    st.write([e['word'] for e in entities])