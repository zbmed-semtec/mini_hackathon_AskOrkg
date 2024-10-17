import os
from qdrant_client import QdrantClient
from qdrant_client.http import models
from qdrant_client.http.models import Distance, VectorParams
import numpy as np
from typing import List, Dict, Any

class QdrantVectorStore:
    def __init__(self, host: str = None, port: int = None):
        self.host = host or os.getenv("QDRANT_HOST", "qdrant")
        self.port = port or int(os.getenv("QDRANT_PORT", 6333))
        self.client = self._connect_with_retry()

    def _connect_with_retry(self, max_retries=5):
        for attempt in range(max_retries):
            try:
                client = QdrantClient(host=self.host, port=self.port)
                # Test the connection
                client.get_collections()
                print(f"Successfully connected to Qdrant at {self.host}:{self.port}")
                return client
            except Exception as e:
                print(f"Attempt {attempt + 1} failed: {str(e)}")
                if attempt == max_retries - 1:
                    raise ConnectionError(f"Failed to connect to Qdrant after {max_retries} attempts")

    def create_collection(self, collection_name: str, vector_size: int):
        """Create a new collection in Qdrant."""
        self.client.recreate_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE),
        )
        print(f"Collection '{collection_name}' created successfully.")

    def store_embeddings(self, collection_name: str, embeddings: np.ndarray, metadata: List[Dict[str, Any]]):
        """Store embeddings and metadata in the specified collection."""
        self.client.upsert(
            collection_name=collection_name,
            points=models.Batch(
                ids=[m["id"] for m in metadata],
                vectors=embeddings.tolist(),
                payloads=metadata
            )
        )
        print(f"Stored {len(embeddings)} embeddings in collection '{collection_name}'.")

    def search_similar(self, collection_name: str, query_vector: np.ndarray, limit: int = 5):
        """Search for similar vectors in the specified collection."""
        results = self.client.search(
            collection_name=collection_name,
            query_vector=query_vector.tolist(),
            limit=limit
        )
        return results

    def health_check(self):
        """Perform a health check on the Qdrant connection."""
        try:
            self.client.get_collections()
            return True
        except Exception as e:
            print(f"Health check failed: {str(e)}")
            return False