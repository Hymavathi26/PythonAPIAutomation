# To Make POST, PUT, PATCH, DELETE requests

#HTTP METHODS GENERIC FUNCTIONS
#in this wrapper folder we make a comman function for request

# def get_request(url, auth):  #in_json add this arg if want logic        #if we want response in json we use in_json
#     response=requests.get(url=url,auth=auth)   #here we are making request
#     # if in_json in True:
#     #     return response.json()
#     return response                            #return response
#
# #data=requests.get("https://restful-booker.herokuapp.com/booking/1",in_json=True)
# #data--if in-json=True it returns data in json format and if in_json is False it returns normal response (json != True)
#
# #or we can use request in json also like elow
# def requests_get_in_json(url, auth):
#     response=requests.get(url=url, auth=auth)
#     return response.json()         #retun reaponse in json form

#instead of using those two function combined two function in one like
#get generic function
import json
import requests
def get_request(url, auth, in_json):         #if we want response in json we use in_json
    response=requests.get(url=url,auth=auth)
    if in_json is True:
        return response.json()   #if in_json is True it returns json format else returns normal response
    return response

#POST GENERIC FUNCTION(which means any one can be use these functions)
def post_requests(url, auth, headers, payload, in_json):
    post_response=requests.post(url=url,headers=headers, auth=auth, data=json.dumps(payload))
    if in_json is True:
         return post_response.json()
    return post_response
#PATCH GENERIC FUNCTION
def patch_requests(url,auth,headers,payload,in_json):
    patch_response_data=requests.patch(url=url,auth=auth,headers=headers,data=json.dumps(payload))
    if in_json is True:
         return patch_response_data.json()
    return patch_response_data
#PUT Generic function
def put_requests(url,auth,headers,payload,in_json):
    put_response_data=requests.put(url=url,auth=auth,headers=headers,data=json.dumps(payload))
    if in_json is True:
         return put_response_data.json()
    return put_response_data

#if data in xml -->need to convert into json before sending data
#DELETE Generic function
def delete_requests(url,auth,headers,payload,in_json):
    delete_response_data=requests.post(url=url,auth=auth,headers=headers)
    if in_json is True:
         return delete_response_data.json()
    return delete_response_data
