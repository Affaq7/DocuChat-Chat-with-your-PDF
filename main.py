##venv\Scripts\activate
##streamlit run main.py
import streamlit as st
import tempfile
from langchain_core.messages import HumanMessage, AIMessage
from pipeline import build_chain, ask

st.set_page_config(page_title="DocuChat", page_icon="📄")
st.markdown("<h1 style='text-align: center;'>DocuChat — Chat with your PDF</h1>", unsafe_allow_html=True)

uploaded = st.file_uploader("Upload a PDF", type="pdf")

if uploaded:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded.read())
        tmp_path = tmp.name

    if "chain" not in st.session_state:
        with st.spinner("Reading and indexing your PDF..."):
            st.session_state.chain = build_chain(tmp_path)
            st.session_state.messages = []
            st.session_state.chat_history = []
        st.success("Ready! Ask anything about your document.")

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    if prompt := st.chat_input("Ask something about the PDF..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                result = ask(st.session_state.chain, prompt, st.session_state.chat_history)
            st.write(result["answer"])
            with st.expander("📎 Source chunks used"):
                for i, src in enumerate(result["sources"], 1):
                    st.caption(f"Chunk {i}: {src}...")

        st.session_state.chat_history.extend([
            HumanMessage(content=prompt),
            AIMessage(content=result["answer"])
        ])
        st.session_state.messages.append({"role": "assistant", "content": result["answer"]})