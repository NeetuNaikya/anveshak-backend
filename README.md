# Anveshak Bot

Anveshak is an AI-powered help bot designed to assist users in querying complex satellite data, documents, FAQs, and web content using natural language. The bot utilizes a Retrieval-Augmented Generation (RAG) pipeline, a knowledge graph, and NLP-based semantic understanding to provide instant, contextual responses.

## Project Structure

The project is organized into two main directories: `backend` and `frontend`.

### Backend

The backend is built using Python and includes the following components:

- **src/app.py**: Main entry point for the backend application, initializes the Flask app, sets up routes, and integrates various components of the bot.
- **src/ingestion**: Contains modules for crawling and parsing web content and documents.
  - `crawler.py`: Functions to crawl and scrape web content.
  - `document_parser.py`: Functions to parse different document formats (PDF, DOCX, XLSX).
- **src/knowledge_graph**: Functions to build and update the knowledge graph using extracted entities and relationships.
- **src/rag**: Implements the retrieval logic and connects to the LLM for generating responses.
- **src/nlp**: Contains functions for entity extraction and semantic search.
- **src/geospatial**: Functions to parse geospatial queries and connect them to spatial metadata.
- **src/multilingual**: Supports multiple languages and voice input functionality.
- **src/chatbot**: Manages the conversation flow and context for the chatbot.
- **src/utils.py**: Utility functions used across different modules.

### Frontend

The frontend is built using React and includes the following components:

- **src/components**: Contains the Chatbot and Message components for user interactions.
- **src/App.jsx**: Main component integrating all components and managing state.
- **src/index.js**: Entry point for the React application.
- **src/styles/tailwind.css**: Tailwind CSS styles for the frontend application.
- **public/index.html**: Main HTML file for the frontend application.

### Docker

The project includes a `docker-compose.yml` file for running the application using Docker Compose, along with a `Dockerfile` for building the backend Docker image.

## Setup Instructions

### Backend

1. Navigate to the `backend` directory.
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the application:
   ```
   python src/app.py
   ```

### Frontend

1. Navigate to the `frontend` directory.
2. Install the required dependencies:
   ```
   npm install
   ```
3. Start the frontend application:
   ```
   npm start
   ```

## Usage

Once both the backend and frontend are running, you can access the Anveshak bot through the web interface. Users can input queries related to satellite data, documents, and more, and receive contextual responses.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.