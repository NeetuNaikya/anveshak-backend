from flask import Flask, request, jsonify
from ingestion.crawler import crawl_content
from ingestion.document_parser import parse_documents
from knowledge_graph.graph_builder import build_knowledge_graph
from rag.retriever import retrieve_response
from nlp.entity_extraction import extract_entities
from nlp.semantic_search import semantic_search
from geospatial.geo_parser import parse_geospatial_query
from multilingual.translation import translate_query
from multilingual.voice_input import process_voice_input
from chatbot.conversation import manage_conversation

app = Flask(__name__)

@app.route('/api/crawl', methods=['POST'])
def crawl():
    data = request.json
    content = crawl_content(data['url'])
    return jsonify(content)

@app.route('/api/parse', methods=['POST'])
def parse():
    files = request.files.getlist('documents')
    parsed_data = parse_documents(files)
    return jsonify(parsed_data)

@app.route('/api/knowledge_graph', methods=['GET'])
def knowledge_graph():
    graph_data = build_knowledge_graph()
    return jsonify(graph_data)

@app.route('/api/query', methods=['POST'])
def query():
    user_query = request.json['query']
    entities = extract_entities(user_query)
    response = retrieve_response(user_query)
    return jsonify({'entities': entities, 'response': response})

@app.route('/api/semantic_search', methods=['POST'])
def semantic_search_route():
    user_query = request.json['query']
    results = semantic_search(user_query)
    return jsonify(results)

@app.route('/api/geospatial', methods=['POST'])
def geospatial_query():
    query = request.json['query']
    parsed_data = parse_geospatial_query(query)
    return jsonify(parsed_data)

@app.route('/api/translate', methods=['POST'])
def translate():
    text = request.json['text']
    translated_text = translate_query(text)
    return jsonify({'translated_text': translated_text})

@app.route('/api/voice', methods=['POST'])
def voice_input():
    audio_file = request.files['audio']
    text = process_voice_input(audio_file)
    return jsonify({'text': text})

@app.route('/api/conversation', methods=['POST'])
def conversation():
    user_input = request.json['input']
    response = manage_conversation(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)