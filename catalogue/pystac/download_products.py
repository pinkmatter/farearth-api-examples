import os
import urllib
from pystac_client import Client
from constants import FE3_API_URL


# Note: This script downloads files to the folder that the script is in.

if __name__ == "__main__":

    catalog = Client.open(
        url=FE3_API_URL,
        headers={
            'X-API-Key': os.environ['FE3_API_KEY']
        }
    )

    # Get all the collections that the API key has access to
    collections = catalog.get_collections()

    for collection in collections:
        print(collection)
        # Use the last specified collection
        specific_collection_name = collection.id

    # Get an object representing a specific collection
    specific_collection = catalog.get_collection(specific_collection_name)

    search = catalog.search(
        max_items=30,
        limit=3,
        collections=[specific_collection],
        bbox=[8.518128, 3.663501, 42.038028, -35.811674],
    )

    print(f"{search.matched()} items found")

    for item in search.items():

        # Download thumbnails (previews) if they are available
        if 'THUMB_RGB' in item.assets:
            urllib.request.urlretrieve(item.assets["THUMB_RGB"].href, f"{item.id}_PREVIEW.png")

        # Alternatively, you can download an asset based on its role
        for key, value in item.assets.items():
            if value.roles == 'metadata':
                urllib.request.urlretrieve(item.assets[key].href, f"{item.id}_META.json")
