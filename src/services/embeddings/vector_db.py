from pymilvus import MilvusClient
from src import CLUSTER_ENDPOINT, TOKEN, COLLECTION_NAME


class VectorDB:
    def __init__(self):
        self.collection_name = COLLECTION_NAME
        self.client = MilvusClient(uri=CLUSTER_ENDPOINT, token=TOKEN)
        if not self.client.has_collection(collection_name=self.collection_name):
            self.client.create_collection(
                collection_name=self.collection_name,
                dimension=3072,
            )

    def insert_data(self, data):
        res = self.client.insert(collection_name=self.collection_name, data=data)
        return res.get("ids", [])

    def search_data(self, query, file_id):
        res = self.client.search(collection_name=self.collection_name, data=[query], filter=f"file_id == '{file_id}'", limit=5, output_fields=["text", "file_id"])
        return [val[0].get("entity") for val in res if val[0].get("entity", {})]
    
