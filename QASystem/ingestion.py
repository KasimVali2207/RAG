
from haystack import Pipeline
from haystack.components.writers import DocumentWriter
from haystack.components.preprocessors import DocumentSplitter
from haystack.components.embedders import SentenceTransformersDocumentEmbedder
from haystack_integrations.document_stores.pinecone import PineconeDocumentStore
from haystack.components.converters import PyPDFToDocument
from pathlib import Path
import os
from QASystem.utility import pinecone_config

def ingest(document_store):
    # Creating a pipeline object
    indexing = Pipeline()

    # Adding components to the pipeline
    indexing.add_component("converter", PyPDFToDocument())
    indexing.add_component("splitter", DocumentSplitter(split_by="sentence", split_length=2))
    indexing.add_component("embedder", SentenceTransformersDocumentEmbedder())
    indexing.add_component("writer", DocumentWriter(document_store))

    # Connecting all the components of the pipeline
    indexing.connect("converter", "splitter")
    indexing.connect("splitter", "embedder")
    indexing.connect("embedder", "writer")

    # Storing the data as embeddings in the database
    indexing.run({"converter": {"sources": [Path("C:\\Users\\91630\\OneDrive\\RAG\\data\\Retrieval-Augmented-Generation-for-NLP.pdf")]}})

if __name__ == "__main__":
    # Calling pinecone_config to get the configured document store
    document_store = pinecone_config()
    
    # Running the ingestion process
    ingest(document_store)
