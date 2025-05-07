import streamlit as st
from main import qa_chain

query = st.text_input("Ask about support policy:")
if query:
    response = qa_chain.run(query)
    st.write("", response)