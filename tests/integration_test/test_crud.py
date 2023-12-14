from src.Helpers.api_requests_wrapper import post_requests,put_requests
# from src.Constants.api_constants import base_url
from src.Constants.api_constants import APIConstants
from src.Helpers.utils import common_headers_json
from src.Helpers.payload_manager import payload_creating_booking,payload_create_token
from src.Helpers.common_verification import verify_response_should_not_be_none, verify_http_status_code

import pytest

class TestCreatBooking(object):

    def test_create_token(self):
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
    def test_create_booking(self):   #for update we need token and booking Id from create booking ,create token
            # url, headers,payload
                response = post_requests(url=APIConstants.url_creating_boooking(), auth=None, headers=common_headers_json(),
                                     payload=payload_creating_booking(), in_json=False)
            print(response)
            bookingid = response.json()["bookingid"]  # it prints bookingid
            print(bookingid)
            verify_response_should_not_be_none(response.json()[
                                                   "bookingid"])  # call verify_response fun and pass bookingid key and convert response into json()
            verify_http_status_code(response, 200)

    def test_update_booking(self):
        token="39b4348799bde03"
        put_url=APIConstants.url_creating_boooking() + "2777"
        auth=("admin","password123")
        response = put_requests(url=put_url, auth=auth, headers=common_headers_json(),
                                     payload=payload_creating_booking(), in_json=False)

        print(response.json())
    def test_delete_booking(self):
        pass