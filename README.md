# Anveshak Bot Backend

This document provides an overview of the Anveshak Bot backend, including setup instructions, usage guidelines, and a brief description of the components involved in the project.

## Project Structure

The backend is organized into several modules, each responsible for different functionalities:

- **Ingestion**: Responsible for crawling and parsing web content and documents.
  - `crawler.py`: Functions to crawl and scrape web content.
  - `document_parser.py`: Functions to parse various document formats (PDF, DOCX, XLSX).

- **Knowledge Graph**: Manages the creation and updating of the knowledge graph.
  - `graph_builder.py`: Functions to build and update the knowledge graph using extracted entities and relationships.

- **Retrieval-Augmented Generation (RAG)**: Implements the retrieval logic and connects to the language model.
  - `retriever.py`: Implements vector search using FAISS or ChromaDB.
  - `llm_connector.py`: Connects the retrieval system to the language model for generating responses.

- **Natural Language Processing (NLP)**: Handles entity extraction and semantic search.
  - `entity_extraction.py`: Functions for entity extraction using spaCy.
  - `semantic_search.py`: Implements semantic search functionality.

- **Geospatial**: Parses geospatial queries and connects them to spatial metadata.
  - `geo_parser.py`: Functions to handle geospatial queries.

- **Multilingual Support**: Provides translation and voice input functionalities.
  - `translation.py`: Functions for translating queries and responses.
  - `voice_input.py`: Implements voice input functionality.

- **Chatbot**: Manages the conversation flow and context for the chatbot.
  - `conversation.py`: Manages the conversation state and context.

- **Utilities**: Contains utility functions used across different modules.
  - `utils.py`: General utility functions.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd anveshak-bot/backend
   ```

2. **Install Dependencies**:
   It is recommended to use a virtual environment. You can create one using `venv` or `conda`.
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   You can start the backend application using the following command:
   ```bash
   python src/app.py
   ```

4. **Docker Setup** (Optional):
   If you prefer to run the application using Docker, you can build and run the Docker container:
   ```bash
   docker build -t anveshak-bot-backend .
   docker run -p 5000:5000 anveshak-bot-backend
   ```

## Usage

Once the backend is running, you can interact with the Anveshak Bot through the frontend interface. The bot is designed to handle complex queries related to satellite data, documents, and FAQs, providing instant and contextual responses.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.