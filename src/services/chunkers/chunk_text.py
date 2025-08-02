from langchain_text_splitters import RecursiveCharacterTextSplitter, CharacterTextSplitter


class Chunkers:
    def __init__(self, all_text):
        self.all_text = all_text

    def chunk_text_same_length(self, chunk_size=1000, chunk_overlap=200):
        text_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        chunks = text_splitter.create_documents([self.all_text])
        return chunks

    def chunk_text_based_on_structure(self, chunk_size=1000, chunk_overlap=300):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        chunks = text_splitter.create_documents([self.all_text])
        return chunks