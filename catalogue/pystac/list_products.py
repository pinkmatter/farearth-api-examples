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

    # Simply get all the items in the catalog
    all_items = catalog.get_all_items()

    for item in all_items:
        print(item)

    # Perform a filtered search for products to limit the responses to:

    # A specific bounding box
    search = catalog.search(
        max_items=30,
        limit=3,
        bbox=[8.518128, 3.663501, 42.038028, -35.811674]
    )

    print(f"{search.matched()} items found")

    # A specific datetime range
    time_search = catalog.search(
        max_items=30,
        limit=3,
        datetime="2022-08-04T08:30:00.000Z/2022-08-04T08:36:00.00Z"
    )

    print(f"{time_search.matched()} items found")

    # A different format specific datetime range
    time_search2 = catalog.search(
        max_items=30,
        limit=3,
        datetime=['2022-08-04T08:36:00.000Z', '2022-08-04T09:00:00.00Z']
    )

    print(f"{time_search2.matched()} items found")

    # A different format specific datetime range
    time_search2 = catalog.search(
        max_items=30,
        limit=3,
        datetime=['2022-08-04T08:36:00.000Z', '2022-08-04T09:00:00.00Z']
    )

    print(f"{time_search2.matched()} items found")

    # An example of how to search for a specific correlation ID.
    ci_query_json = {
        "correlationId": {
            "eq": "Sample-01-OLI-2-L1C"
        }
    }

    correlation_search = catalog.search(
        max_items=30,
        limit=3,
        query=ci_query_json
    )

    print(f"{correlation_search.matched()} items found")

    # An example of how to search for a specific dataset.
    ds_query_json = {
        "dataset": {
            "eq": "Landsat-9-Sample"
        }
    }

    dataset_search = catalog.search(
        max_items=30,
        limit=3,
        query=ds_query_json
    )

    print(f"{dataset_search.matched()} items found")
