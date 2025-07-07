from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA

class LLMConnector:
    def __init__(self, openai_api_key, vector_store_path):
        self.embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
        self.vector_store = FAISS.load_local(vector_store_path, self.embeddings)
        self.llm = OpenAI(openai_api_key=openai_api_key)
        self.retrieval_qa = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.vector_store.as_retriever()
        )

    def generate_response(self, query):
        response = self.retrieval_qa({"query": query})
        return response['result']