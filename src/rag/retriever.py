from typing import List
import faiss
import numpy as np

class Retriever:
    def __init__(self, index: faiss.IndexFlatL2, embeddings: List[np.ndarray]):
        self.index = index
        self.embeddings = embeddings

    def retrieve(self, query_embedding: np.ndarray, k: int = 5) -> List[int]:
        distances, indices = self.index.search(query_embedding.reshape(1, -1), k)
        return indices[0].tolist()

    def add_embeddings(self, new_embeddings: List[np.ndarray]):
        self.embeddings.extend(new_embeddings)
        self.index.add(np.array(new_embeddings).astype('float32'))