from flask import request, jsonify
from langchain import ConversationChain
from langchain.memory import ConversationBufferMemory
from rag.llm_connector import generate_response
from nlp.semantic_search import semantic_search
from multilingual.translation import translate_query

class AnveshakConversation:
    def __init__(self):
        self.memory = ConversationBufferMemory()
        self.conversation_chain = ConversationChain(memory=self.memory)

    def handle_user_input(self, user_input):
        translated_input = translate_query(user_input)
        response = self.process_input(translated_input)
        return response

    def process_input(self, user_input):
        # Check for direct FAQ match
        faq_response = self.check_faq(user_input)
        if faq_response:
            return faq_response
        
        # If no FAQ match, perform semantic search
        search_results = semantic_search(user_input)
        if search_results:
            return self.generate_response(search_results)
        
        return "I'm sorry, I couldn't find an answer to your question."

    def check_faq(self, user_input):
        # Placeholder for FAQ checking logic
        return None

    def generate_response(self, search_results):
        # Generate a response using the LLM
        return generate_response(search_results)

    def get_conversation_history(self):
        return self.memory.get_history()