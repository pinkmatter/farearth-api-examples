# farearth-api-examples
This repository contains examples of how to interact with *FarEarth for SmallSats* using the built in API's.

## Catalogue
The catalogue in FarEarth is a [SpatioTemporal Asset Catalog(STAC)](https://stacspec.org) and will work with any of the examples and tutorials designed for the various STAC clients.

### catalogue/pystac
This folder contains stand-alone python files that may be run and investigated to demonstrate how to interact with the catalogue in *FarEarth for SmallSats*. All the examples rely on [pystac_client](https://github.com/stac-utils/pystac-client).

#### Getting started
1. Clone the code
```
git clone https://github.com/pinkmatter/farearth-api-examples
```
```
cd farearth-api-examples/catalogue
```

2. Prepare the environment, the following uses `venv`, replace with conda or other python environment management system if you wish

```
python -m venv pystac
```

```
cd pystac
```
3. Activate your environment, this is dependent on your platform. Instructions can be found here: https://docs.python.org/3/library/venv.html. For windows (.bat), use the following:

```
./Scripts/activate
```

4. Once activated install the dependencies
```
python -m pip install -r requirements.txt
```

5. Generate an API key by following the instructions in the **Generating an API key** section below

6. Add the API key to your environment variables under the name 'FE3_API_KEY'. To get started testing quickly you may replace **os.environ['FE3_API_KEY']** in each of the files with **R"KEY"** where the word KEY is replaced by the key generated in *FarEarth*.

7. Finally run the catalogue info script, if successful it will return a list of the specifications that the FarEarth API conforms to and confirms that everything is working as intended
```
python catalogue_info.py
```

8. Sample output of the catalogue_info.py
```
The FarEarth STAC API conforms to the following specifications:
https://api.stacspec.org/v1.0.0/core
https://api.stacspec.org/v1.0.0/collections
https://api.stacspec.org/v1.0.0/ogcapi-features
https://api.stacspec.org/v1.0.0/item-search
https://api.stacspec.org/v1.0.0/ogcapi-features#fields
https://api.stacspec.org/v1.0.0/ogcapi-features#sort
https://api.stacspec.org/v1.0.0/ogcapi-features#query
https://api.stacspec.org/v1.0.0/item-search#fields
https://api.stacspec.org/v1.0.0/item-search#sort
https://api.stacspec.org/v1.0.0/item-search#query
https://api.stacspec.org/v0.3.0/aggregation
http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/core
http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/oas30
http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/geojson
```



## Generating an API key
All of the examples in this repository require an API key. To generate your API key:

1. Navigate to the **USERS** menu.
2. Click on your user's email address
3. Click on the create button to generate an API key
4. If you would like to remove access for an API key, click the remove button

![User menu selection.](/assets/user_menu.png)