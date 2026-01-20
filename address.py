import googlemaps
from datetime import datetime

# Replace 'Add Your Key here' with your actual API key
gmaps = googlemaps.Client(key='Add Your Key here')

# Geocoding an address
address = '1600 Amphitheatre Parkway, Mountain View, CA'
geocode_result = gmaps.geocode(address)

print(f"Address: {address}")
print(f"Latitude: {geocode_result[0]['geometry']['location']['lat']}")
print(f"Longitude: {geocode_result[0]['geometry']['location']['lng']}")

# You can also use other services like Directions
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall", "Parramatta, NSW",
                                     mode="transit", departure_time=now)
print(f"\nDirections steps: {len(directions_result[0]['legs'][0]['steps'])} steps")
