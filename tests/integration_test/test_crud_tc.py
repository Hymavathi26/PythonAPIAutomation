from src.Constants.api_constants import Base_url, base_url, APIConstants

def test_crud():
    print(Base_url)

    url_dirctFrom_func = base_url()
    print(url_dirctFrom_func)

    url_class = APIConstants.base_url()     #here we call class directly by using static method
    print(url_class)

    #if without using static method in api_constants file then we use like
    #url_class = APIConstants().base_url()  # create instances to the class