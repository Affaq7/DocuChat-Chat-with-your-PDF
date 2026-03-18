# DocuChat — Chat with your PDF 📄

DocuChat is an interactive Chatbot application that allows users to seamlessly upload and converse with their PDF documents in real-time. Built specifically with Retrieval-Augmented Generation (RAG) architecture, it leverages the speed of Groq and the embedding capabilities of Google's Generative AI. 

## Features
- **PDF Upload and Parsing**: Effortlessly upload PDF files and instantly extract content using PyMuPDF.
- **Intelligent Chunking**: Employs Recursive Character Text Splitting to break down large documents into processing-friendly chunks with intelligent overlap to retain context.
- **Advanced Vector Search**: Embeds document text using Google Gemini embeddings and creates a fast, in-memory Chroma vector database to fetch relevant semantic results.
- **Fast Inferencing with Llama 3**: Uses `llama-3.3-70b-versatile` running on Groq's LPU engine for lightning-fast and highly accurate answer generation.
- **Conversation Memory**: Maintains continuous conversation history allowing for detailed follow-up questions contextually bound to your document.
- **Source Inspection**: Provides visibility into the exact source chunks retrieved to formulate the answer.

## Tech Stack
- **Frontend**: [Streamlit](https://streamlit.io/)
- **Orchestration**: [LangChain](https://python.langchain.com/)
- **Embeddings**: Google Generative AI (`models/gemini-embedding-001`)
- **LLM**: Groq API (`llama-3.3-70b-versatile`)
- **Vector Store**: Chroma
- **Document Loader**: PyMuPDF

## Prerequisites
Before you begin, ensure you have the following API keys:
- **Google AI API Key**: To generate document vector embeddings.
- **Groq API Key**: To access the Llama 3 model for text generation.

## Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd Docuchat
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   ## Activate the virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   *(Ensure you have `streamlit`, `langchain`, `langchain-community`, `langchain-google-genai`, `langchain-groq`, `chromadb`, `pymupdf`, and `python-dotenv` installed)*
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Environment Variables:**
   Create a `.env` file in the root directory and add your secret API keys:
   ```env
   GOOGLE_API_KEY=your_google_api_key_here
   GROQ_API_KEY=your_groq_api_key_here
   ```

## Usage

1. Start the Streamlit application by running:
   ```bash
   streamlit run main.py
   ```
2. The application will open in your default web browser (typically at `http://localhost:8501`).
3. Click on the file uploader to browse and select a PDF file.
4. Wait a few moments for the application to extract, embed, and index your PDF.
5. Once "Ready!" is shown, start chatting with your PDF through the chat input at the bottom of the screen!

---
*Note: The vector database is created dynamically in-memory and will be cleared when the application restarts.*
