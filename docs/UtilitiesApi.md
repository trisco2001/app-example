# swagger_client.UtilitiesApi

All URIs are relative to *//localhost:8080/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health_check**](UtilitiesApi.md#health_check) | **GET** /health-check | Quick health check to test latency

# **health_check**
> ModelsHealthCheckResponse health_check()

Quick health check to test latency

Quick health check to test latency

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UtilitiesApi()

try:
    # Quick health check to test latency
    api_response = api_instance.health_check()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilitiesApi->health_check: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ModelsHealthCheckResponse**](ModelsHealthCheckResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

