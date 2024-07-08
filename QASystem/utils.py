from haystack_integrations.document_stores.pinecone import PineconeDocumentStore
import os
from dotenv import load_dotenv

load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
os.environ['PINECONE_API_KEY'] = PINECONE_API_KEY
    
print("Import Successfully")

def pinecone_config():
    # Configuring Pinecone database
    document_store = PineconeDocumentStore(
        api_key=PINECONE_API_KEY,
        index="docs-quickstart-index",  # Replace with your desired index name
        dimension=3072,  # Replace with your desired dimensionality
        metric="cosine",  # Specify your preferred metric
        host="https://default-ypt5h65.svc.aped-4627-b74a.pinecone.io",  # Replace with your Pinecone host URL
        cloud="aws",
        region="us-east-1",
        type="serverless"
    )
    return document_store
