# from math import radians, sin, cos, sqrt, atan2
#
#
# def haversine_distance(lat1, lon1, lat2, lon2):
#     # Radius of the Earth in kilometers
#     R = 6371.0
#
#     # Convert latitude and longitude from degrees to radians
#     lat1 = radians(lat1)
#     lon1 = radians(lon1)
#     lat2 = radians(lat2)
#     lon2 = radians(lon2)
#
#     # Calculate the change in coordinates
#     dlon = lon2 - lon1
#     dlat = lat2 - lat1
#
#     # Haversine formula
#     a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
#     c = 2 * atan2(sqrt(a), sqrt(1 - a))
#     distance = R * c
#
#     return distance
#
#
# # Coordinates of the user's city (example: New York)
# user_latitude = 40.7128
# user_longitude = -74.0060
#
# # Coordinates of AWS regions (us-east-1 and sa-west-1)
# aws_regions = {
#     "us-east-1": {"latitude": 39.0481, "longitude": -77.4728},
#     "sa-west-1": {"latitude": -23.5505, "longitude": -46.6333}
# }
#
# # Calculate distances to each AWS region
# distances = {}
# for region, coords in aws_regions.items():
#     distance = haversine_distance(user_latitude, user_longitude, coords["latitude"], coords["longitude"])
#     distances[region] = distance
#
# # Find the region with the minimum distance
# min_distance_region = min(distances, key=distances.get)
# min_distance = distances[min_distance_region]
#
# print("Minimum distance region:", min_distance_region)
# print("Minimum distance (in kilometers):", min_distance)

n = input()
mp={}
for char in n:
    if char in n:
        mp[char]+=1
    else:
        mp[char]+=0
li=[]
for char in n:
    if mp[char]<2:
        li.append(char)
    else:
        continue

print(li)
