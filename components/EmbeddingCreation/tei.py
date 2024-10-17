from langchain_huggingface.embeddings import HuggingFaceEndpointEmbeddings

class textEmbeddingsInterference:
    def compute_embedding(doc: str):
        embeddings = HuggingFaceEndpointEmbeddings(model="http://localhost:8080")
        query_result = embeddings.embed_query(doc)
        return query_result
