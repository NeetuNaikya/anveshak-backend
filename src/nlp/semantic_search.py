from typing import List
from sentence_transformers import SentenceTransformer, util
import numpy as np

class SemanticSearch:
    def __init__(self, documents: List[str]):
        self.documents = documents
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.embeddings = self.model.encode(documents, convert_to_tensor=True)

    def search(self, query: str, top_k: int = 5) -> List[str]:
        query_embedding = self.model.encode(query, convert_to_tensor=True)
        cosine_scores = util.pytorch_cos_sim(query_embedding, self.embeddings)[0]
        top_results = np.argpartition(-cosine_scores, range(top_k))[:top_k]
        
        return [self.documents[idx] for idx in top_results]