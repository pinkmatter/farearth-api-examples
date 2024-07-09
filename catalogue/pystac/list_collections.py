import os
from pystac_client import Client
from constants import FE3_API_URL

if __name__ == "__main__":

    catalog = Client.open(
        url=FE3_API_URL,
        headers={
            'X-API-Key': os.environ['FE3_API_KEY']
        }
    )

    # Get all the collections that the API key has access to
    collections = catalog.get_collections()

    # Use a default collection name to handle the case where none are defined
    specific_collection_name = "farearth.acme"

    for collection in collections:
        print(collection)
        # Use the last specified collection
        specific_collection_name = collection.id

    # Get an object representing a specific collection
    specific_collection = catalog.get_collection(specific_collection_name)

    print(specific_collection)
