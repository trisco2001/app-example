# swagger_client.StorageApi

All URIs are relative to *//localhost:8080/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_file**](StorageApi.md#download_file) | **GET** /storage/download-file | Download a file

# **download_file**
> ModelsFileData download_file(path)

Download a file

Download a file by file path

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StorageApi()
path = 'path_example' # str | Path to file

try:
    # Download a file
    api_response = api_instance.download_file(path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageApi->download_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Path to file | 

### Return type

[**ModelsFileData**](ModelsFileData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

