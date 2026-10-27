# Documind AI
### Intelligent Document Question Answering System using RAG and Large Language Models

## Project Description

Documind AI is an AI-powered document question-answering application developed using Python, Streamlit, Retrieval-Augmented Generation (RAG), and Large Language Models (LLMs).

The application allows users to upload PDF documents, extract their textual content, and ask questions based on the uploaded documents.

It uses semantic search to retrieve relevant information and an LLM to generate context-aware answers.

## Features

- Upload and process PDF documents.
- Extract text from uploaded PDFs.
- Split extracted text into smaller chunks.
- Generate vector embeddings using Sentence Transformers.
- Store and retrieve document embeddings using ChromaDB.
- Perform semantic similarity searches.
- Generate answers using a locally running Ollama LLM.
- Interactive web interface developed using Streamlit.
- Display extracted text previews and retrieved context.

## Technologies Used

- **Programming Language:** Python
- **Frontend:** Streamlit
- **LLM:** Llama 3.2 using Ollama
- **Embedding Model:** all-MiniLM-L6-v2
- **Vector Database:** ChromaDB
- **PDF Processing:** pypdf
- **Architecture:** Retrieval-Augmented Generation (RAG)

## Project Workflow

1. User uploads a PDF document.
2. Text is extracted from the uploaded PDF.
3. Extracted text is divided into smaller chunks.
4. Sentence Transformers convert text chunks into numerical embeddings.
5. ChromaDB stores the embeddings.
6. User enters a question.
7. Relevant document chunks are retrieved using semantic similarity search.
8. Retrieved context and the user's question are passed to the Ollama LLM.
9. The LLM generates an answer based on the retrieved document context.
10. The generated answer is displayed through Streamlit.

## Installation

### Step 1: Clone the Repository

Clone the project repository from GitHub and navigate to the project directory.

### Step 2: Create a Virtual Environment

```bash
python3 -m venv venv
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Install Ollama

Install Ollama on your system.

Download the required language model:

```bash
ollama pull llama3.2:1b
```

Ensure that the Ollama service is running.

### Step 5: Run the Application

```bash
streamlit run Intelligent_QA_System.py
```

Open the local URL displayed in the terminal.

## How to Use

1. Launch the Streamlit application.
2. Upload a PDF document.
3. Wait for text extraction and vector database creation.
4. Enter a question related to the uploaded document.
5. View the retrieved context and AI-generated answer.

## Applications

- Document analysis
- Educational question answering
- Research paper analysis
- Knowledge retrieval
- PDF-based information extraction

## Limitations

- Scanned or image-only PDFs require OCR for text extraction.
- Answer quality depends on the uploaded document and language model.
- The application requires access to a running Ollama service.
- Large PDF documents may require additional processing time.
- The model may occasionally generate inaccurate answers.

## Future Enhancements

- Support for multiple PDF documents.
- Conversation history.
- Source citations and page references.
- Support for DOCX and TXT documents.
- Improved document retrieval.
- Cloud deployment using a hosted LLM API.

## Conclusion

Documind AI demonstrates the practical implementation of Retrieval-Augmented Generation by combining document processing, vector embeddings, semantic search, and Large Language Models.

The project provides an interactive solution for extracting information from PDF documents using natural language questions.
