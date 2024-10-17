import numpy as np
import json
from components.VectorDatabase.QdrantVectorStore import QdrantVectorStore
from components.EmbeddingCreation.tei import textEmbeddingsInterference

def main():
    # Initialize the QdrantVectorStore
    vector_store = QdrantVectorStore()

    # Wait for Qdrant to be ready
    max_retries = 5
    for i in range(max_retries):
        if vector_store.health_check():
            print("Qdrant is ready")
            break
        print(f"Waiting for Qdrant to be ready (attempt {i+1}/{max_retries})...")
        time.sleep(5)
    else:
        print("Failed to connect to Qdrant")
        return

    # Example usage
    try:
        vector_store.create_collection("example_collection")

        # Generate embeddings and metadata
        embeddings = []
        with open('data/data.json', 'r') as file:
            metadata = json.load(file)
        for row in metadata:
            document = row["title"] + ". " + row["abstract"]
            row["embedding"] = textEmbeddingsInterference.compute_embedding(document)
            embeddings.append(row["embedding"])
        
        # Fixed dimension for msmarco-MiniLM-L-12-v3
        embedding_dim = 384

        # Store the embeddings in Qdrant
        vector_store.store_embeddings("example_collection", embeddings, metadata)

        # Perform a search
        query_vector = np.random.rand(embedding_dim)
        results = vector_store.search_similar("example_collection", query_vector)

        print("Search results:")
        for result in results:
            print(f"ID: {result.id}, Score: {result.score}, Payload: {result.payload}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()

