#HTTP STATUS VERIFICATIONS
def verify_http_status_code(response_data,expect_data):
    print(response_data.status_code)
    print(expect_data)
    assert response_data.status_code == expect_data, "Expect http status codee "+str(expect_data)

def verify_json_key_for_not_null(key):
    assert key !=0, "Key is not empty"+key
    assert key > 0, "key is greater than zero"

def verify_response_should_not_be_none(key):
    assert key is not None       #verify token is not none

def verify_response_time():
    pass


#need to do all common verification
#http status code
#headers
#data verification
#json schema verification
#why we go with verification process is whenever we wnat ot create token we wnat to verify token exit
#when even response is coming we wnat to verify token should exist right?