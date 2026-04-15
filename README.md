# QA Agent

A Retrieval-Augmented Generation (RAG) based Question Answering agent that processes PDF documents and answers user queries using OpenAI's language models and vector embeddings.

## Features

- **Document Processing**: Loads and chunks PDF documents from the `resources/` folder
- **Vector Storage**: Uses ChromaDB for efficient vector storage and retrieval
- **LLM Integration**: Leverages OpenAI's GPT models for generating answers
- **Conversational QA**: Provides context-aware responses based on document content

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd QA_Agent
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Create a `.env` file in the root directory
   - Add your OpenAI API key: `OPENAI_API_KEY=your_api_key_here`

## Usage

1. Place your PDF documents in the `resources/` folder
2. Run the main script:
   ```bash
   python main.py
   ```
3. Enter a topic or question when prompted to search through the documents

## Requirements

- Python 3.7+
- OpenAI API key
- PDF documents in `resources/` folder

## Project Structure

- `main.py`: Entry point for the QA agent
- `model.py`: LLM model configuration
- `agent/rag.py`: RAG implementation with document loading, chunking, and retrieval
- `utils/utility.py`: Utility functions
- `qa_db/`: ChromaDB vector database storage
- `resources/`: Directory for PDF documents

## Dependencies

- langchain
- langchain-openai
- chromadb
- pypdf
- python-dotenv
- beautifulsoup4
