# add your constants here we can use normal function or with in class also(oops)
#we have three ways to give url

Base_url="https://restful-booker.herokuapp.com"      #use normal base constant

def base_url():
    return "https://restful-booker.herokuapp.com"    #this is function constants

class APIConstants(object):                          #using oops with in class
    @staticmethod
    def base_url():
        return "https://restful-booker.herokuapp.com"
    @staticmethod
    def url_creating_boooking():
        return "https://restful-booker.herokuapp.com/booking"

    @staticmethod
    def url_create_token():
        return "https://restful-booker.herokuapp.com/auth"

    # update--PUT, PATCH, DELETE --booking id
    #it is not static method becoze for every testcase booking will be changed
    def url_patch_put_delete_booking(self,booking_id):
        return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)

