# DocuChat — Chat with your PDF 📄

DocuChat is an interactive chatbot application that allows users to seamlessly upload and converse with their PDF documents in real-time. Built with Retrieval-Augmented Generation (RAG) architecture, it leverages the speed of Groq and the embedding capabilities of Google's Generative AI.

## Features
- **PDF Upload and Parsing**: Effortlessly upload PDF files and instantly extract content using PyMuPDF.
- **Intelligent Chunking**: Employs Recursive Character Text Splitting to break down large documents into processing-friendly chunks with intelligent overlap to retain context.
- **Advanced Vector Search**: Embeds document text using Google Gemini embeddings and creates a fast, local Chroma vector database to fetch relevant semantic results.
- **Fast Inferencing with Llama 3.3**: Uses `llama-3.3-70b-versatile` running on Groq's LPU engine for lightning-fast and highly accurate answer generation.
- **Conversation Memory**: Maintains continuous conversation history allowing for detailed follow-up questions contextually bound to your document.
- **Source Inspection**: Provides visibility into the exact source chunks retrieved to formulate each answer.
- **Chat History Sidebar**: Displays all previously asked questions in a clean sidebar for easy reference.
- **Clear Chat**: Reset the conversation at any time without re-uploading the PDF.
- **PDF Info Display**: Shows the uploaded filename and total page count after upload.
- **Dark UI**: Clean dark-themed interface with styled chat bubbles.

## Tech Stack
- **Frontend**: [Streamlit](https://streamlit.io/)
- **Orchestration**: [LangChain](https://python.langchain.com/)
- **Embeddings**: Google Generative AI (`models/gemini-embedding-001`)
- **LLM**: Groq API (`llama-3.3-70b-versatile`)
- **Vector Store**: ChromaDB (runs locally, no setup required)
- **Document Loader**: PyMuPDF (fitz)
- **Environment Management**: python-dotenv

## Prerequisites

Before you begin, ensure you have the following installed and set up:

**Python**: Version 3.9 or higher. Download from [python.org](https://python.org)

**API Keys** — you will need two free API keys:

1. **Google AI API Key** — used to generate document vector embeddings
   - Go to [aistudio.google.com](https://aistudio.google.com)
   - Sign in with a Google account
   - Click "Get API Key" → "Create API key in new project"
   - Copy the key

2. **Groq API Key** — used to access the Llama 3.3 70B model for answer generation
   - Go to [console.groq.com](https://console.groq.com)
   - Sign up for a free account (no credit card required)
   - Navigate to "API Keys" → "Create API Key"
   - Copy the key

Both services are completely free with no credit card required.

## Installation

1. **Clone the repository:**
```bash
   git clone <your-repo-url>
   cd Docuchat
```

2. **Create a virtual environment (recommended):**
```bash
   python -m venv venv

   # Activate on Windows:
   venv\Scripts\activate

   # Activate on macOS/Linux:
   source venv/bin/activate
```

3. **Install dependencies:**
```bash
   pip install -r requirements.txt
```

4. **Set up environment variables:**
   Create a `.env` file in the root directory and add your API keys:
```env
   GOOGLE_API_KEY=your_google_api_key_here
   GROQ_API_KEY=your_groq_api_key_here
```

## Usage

1. Start the Streamlit application:
```bash
   streamlit run main.py
```
2. The application will open in your browser at `http://localhost:8501`
3. Click the file uploader and select any PDF file
4. Wait a few moments for the app to extract, embed, and index your PDF
5. Once the PDF info card appears, start chatting through the input at the bottom
6. Use the sidebar to review your chat history or clear the conversation

## Project Structure
```
Docuchat/
├── main.py              # Streamlit UI and frontend logic
├── pipeline.py          # LangChain RAG pipeline (core AI logic)
├── requirements.txt     # Python dependencies
├── .env                 # API keys (never commit this)
├── .gitignore           # Files excluded from version control
└── README.md
```

## How It Works

1. **Load** — PyMuPDF reads and extracts text from every page of the uploaded PDF
2. **Split** — The text is split into 1000-character chunks with 200-character overlap
3. **Embed** — Google Gemini converts each chunk into a numerical vector representing its meaning
4. **Store** — ChromaDB stores all vectors locally for fast similarity search
5. **Retrieve** — When you ask a question, the 4 most semantically similar chunks are retrieved
6. **Generate** — Llama 3.3 70B receives the chunks + your question + chat history and generates an answer

---
*Note: The vector database is created locally when a PDF is uploaded and is cleared when the app restarts.*