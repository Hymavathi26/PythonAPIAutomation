from src.Helpers.api_requests_wrapper import post_requests,put_requests
# from src.Constants.api_constants import base_url
from src.Constants.api_constants import APIConstants
from src.Helpers.utils import common_headers_json,common_headers_for_put_delete_patch
from src.Helpers.payload_manager import payload_creating_booking,payload_create_token
from src.Helpers.common_verification import verify_response_should_not_be_none, verify_http_status_code

import pytest

class TestCreatBooking(object):

    @pytest.fixture()
    def create_token(self):   #take as a function not tc
        response=post_requests(
            url=APIConstants.url_create_token(),
            headers=common_headers_json(),
            auth=None,
            payload=payload_create_token(),in_json=False
        )
        #print(response)
        verify_http_status_code(response,200)
        print(response.json)
        token=response.json()["token"]
        print(token)
        verify_response_should_not_be_none(token)
        return token
    @pytest.fixture()
    def create_booking(self):   #for update we need token and booking Id from create booking ,create token
            # url, headers,payload
            response = post_requests(url=APIConstants.url_creating_boooking(), auth=None, headers=common_headers_json(),
                                     payload=payload_creating_booking(), in_json=False)
            print(response)
            bookingid = response.json()["bookingid"]  # it prints bookingid
            print(bookingid)
            verify_response_should_not_be_none(response.json()[
                                                   "bookingid"])  # call verify_response fun and pass bookingid key and convert response into json()
            verify_http_status_code(response, 200)
            return bookingid

    def test_update_booking(self,create_token,create_booking): #token and booking if from fixture methods
    #instaed of giving below program by using fixture we can reuse code across multiple tests
        # print(test_create_token)
        # print(test_create_booking)
        bookingId=create_booking   #if i want to give booking id

        #token="39b4348799bde03"   #no need to use token if we use athorization
        put_url=APIConstants.url_creating_boooking() + "/"+str(bookingId)    #instead of Bookingid number we pass like this
        # # headers={
        # #     "Content-Type":"application/json",
        # #     "Authorization":"YWRtaW46cGFzc3dvcmQxMjM=",   instead of using this we just import common header for put and pass headers that directly
        # # }
        response = put_requests(url=put_url,headers=common_headers_for_put_delete_patch(),auth=None,
                                      payload=payload_creating_booking(), in_json=False)

        print(response.json())

    # def test_delete_booking(self):
        # delete_url = APIConstants.url_creating_boooking() + "/5320"
        # response = put_requests(url=delete_url, headers=common_headers_for_put_delete_patch(),
        #                         payload=None, in_json=False)
        # print(response.json())

    # def test_delete_booking(self,create_token,create_booking):
    #     bookingId=create_booking
    #     delete_url = APIConstants.url_creating_boooking() + "/" + str(bookingId)
    #     response=put_requests(url=delete_url, headers=common_headers_for_put_delete_patch(),auth=None,
    #                              payload=None, in_json=False)
    #     print(response.json())


