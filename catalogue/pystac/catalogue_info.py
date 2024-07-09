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

    conforms_to = catalog.get_conforms_to()

    # Print a list of URI's that the server conforms to
    print('The FarEarth STAC API conforms to the following specifications:')
    print('\n'.join(conforms_to))
