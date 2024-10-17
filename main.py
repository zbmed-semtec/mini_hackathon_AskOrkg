import numpy as np
from components.VectorDatabase.QdrantVectorStore import QdrantVectorStore

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
        vector_store.create_collection("example_collection", vector_size=384)

        # Generate dummy embeddings and metadata
        num_embeddings = 100
        embedding_dim = 384
        dummy_embeddings = np.random.rand(num_embeddings, embedding_dim)
        dummy_metadata = [{"id": i, "text": f"Sample text {i}"} for i in range(num_embeddings)]

        # Store the embeddings in Qdrant
        vector_store.store_embeddings("example_collection", dummy_embeddings, dummy_metadata)

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

