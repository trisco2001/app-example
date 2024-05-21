# swagger-client
This is a sample API written to become a Sidecar leveraging the Gin Go framework.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen
For more information, please visit [https://github.com/Apptio-PNE/go-sidecar-accelerator](https://github.com/Apptio-PNE/go-sidecar-accelerator)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StorageApi(swagger_client.ApiClient(configuration))
path = 'path_example' # str | Path to file

try:
    # Download a file
    api_response = api_instance.download_file(path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageApi->download_file: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *//localhost:8080/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*StorageApi* | [**download_file**](docs/StorageApi.md#download_file) | **GET** /storage/download-file | Download a file
*UtilitiesApi* | [**health_check**](docs/UtilitiesApi.md#health_check) | **GET** /health-check | Quick health check to test latency

## Documentation For Models

 - [AllOfmodelsFileDataMetadata](docs/AllOfmodelsFileDataMetadata.md)
 - [ModelsFileData](docs/ModelsFileData.md)
 - [ModelsFileMetadata](docs/ModelsFileMetadata.md)
 - [ModelsHealthCheckResponse](docs/ModelsHealthCheckResponse.md)

## Documentation For Authorization


## BasicAuth

- **Type**: HTTP basic authentication


## Author

tristan.leonard1@ibm.com
