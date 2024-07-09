# farearth-api-examples
This repository contains examples of how to interact with *FarEarth for SmallSats* using the built in API's.

## Catalogue
The catalogue in FarEarth is a [SpatioTemporal Asset Catalog(STAC)](https://stacspec.org) and will work with any of the examples and tutorials designed for the various STAC clients.

### catalogue/pystac
This folder contains stand-alone python files that may be run and investigated to demonstrate how to interact with the catalogue in *FarEarth for SmallSats*. All the examples rely on [pystac_client](https://github.com/stac-utils/pystac-client).

#### Getting started
1. Clone the code and prepare the environment (using `venv`, replace with conda or other python environment management system if you wish)
```
git clone https://github.com/pinkmatter/farearth-api-examples

cd farearth-api-examples/catalogue

python -m venv pystac

cd pystac

./Scripts/activate

python -m pip install -r requirements.txt
```
2. Generate an API key by following the instructions in the section below
3. Add the API key to your environment variables under the name 'FE3_API_KEY'
4. Run the catalogue info script
```
python catalogue_info.py
```

## Generating an API key
All of the examples in this repository require an API key. To generate your API key:

1. Navigate to the **USERS** menu.
2. Click on your user's email address
3. Click on the create button to generate an API key
4. If you would like to remove access for an API key, click the remove button

![User menu selection.](/assets/user_menu.png)