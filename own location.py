from geopy.geocoders import Nominatim
def location_user(address):
    geolocator = Nominatim(user_agent="my_app")
    location = geolocator.geocode(address)
    return location.latitude, location.longitude

if __name__=="__main__":
    # from fetch bucket_name import get_bucket_location

    address=input("Enter your address: ")
    print(location_user(address))


'''Amazon have 4 data centers called regions spanning the world, situated in North California (us-west-1), 
North Virginia (us-east-1), Ireland (eu-west-1) and Singapore (ap-southeast-1).'''