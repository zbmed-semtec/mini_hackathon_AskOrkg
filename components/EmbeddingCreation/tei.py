from langchain_huggingface.embeddings import HuggingFaceEndpointEmbeddings

class textEmbeddingsInterference:
    def compute_embedding(doc: str):
        embeddings = HuggingFaceEndpointEmbeddings(model="http://tei_container:80")
        query_result = embeddings.embed_query(doc)
        return query_result
