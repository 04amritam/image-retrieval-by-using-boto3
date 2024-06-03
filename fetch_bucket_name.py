import boto3
from geopy.geocoders import Nominatim
import pandas as pd
import math
import csv

# Initialize S3 client
client = boto3.client('s3')

# Load data from CSV file into a dictionary
df = pd.read_csv('aws_cloud_locations.csv')
data = df.set_index('code').T.to_dict('list')

def bucket_data_fetch():
    response = client.list_buckets()
    bucket_names = [bucket['Name'] for bucket in response['Buckets']]
    return bucket_names

def get_bucket_location(bucket_name):
    response = client.get_bucket_location(
        Bucket=bucket_name,
        ExpectedBucketOwner='471112734926'
    )
    location = response.get('LocationConstraint')
    if location is None:
        return 'us-east-1'
    return location

def location_user(user_location):
    geolocator = Nominatim(user_agent="my_app")
    location = geolocator.geocode(user_location)
    return location.latitude, location.longitude

def get_lat_long(Bucket_Location):
    return data.get(Bucket_Location.lower(), "Code not found")

def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0  # Radius of the Earth in kilometers

    # Convert latitude and longitude from degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Difference in coordinates
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    # Haversine formula
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Distance in kilometers
    distance = R * c

    return distance

if __name__ == "__main__":
    user_location = input("Enter the user city name: ")
    lat1, lon1 = location_user(user_location)

    min_distances = []
    bucket_distances = {}

    buckets = bucket_data_fetch()
    if not buckets:
        print("No Bucket Found")
    else:
        with open('bucket_distances.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['User Location', 'Bucket Name', 'Bucket Location', 'Latitude', 'Longitude', 'Distance (km)'])

            for bucket_name in buckets:
                location = get_bucket_location(bucket_name)

                lat_long = get_lat_long(location)
                if lat_long != "Code not found":
                    lat2, lon2 = lat_long

                    # Calculate Haversine distance
                    distance = haversine(lat1, lon1, lat2, lon2)
                    min_distances.append((distance, bucket_name))
                    bucket_distances[bucket_name] = distance

                    # Write to CSV
                    writer.writerow([user_location, bucket_name, location, lat2, lon2, distance])
                else:
                    writer.writerow([user_location, bucket_name, location, 'N/A', 'N/A', 'N/A'])

        # Find the bucket with the shortest distance
        min_distance, closest_bucket = min(min_distances)
        print(f"The closest bucket is '{closest_bucket}' with a distance of {min_distance} km")


        '''download the nearest file from aws storage'''
        s3 = boto3.resource('s3')
        s3.Bucket(closest_bucket).download_file('example.txt', 'downloaded_example.txt')

        print("Results saved to bucket_distances.csv")
        print(f"Downloaded 'example.txt' from the bucket '{closest_bucket}'")
