from flask import Flask, render_template_string
import googlemaps
from datetime import datetime

app = Flask(__name__)

# Replace with your actual API key
GMAPS_KEY = 'YOUR_GOOGLE_MAPS_API_KEY'
gmaps = googlemaps.Client(key=GMAPS_KEY)

@app.route('/')
def index():
    # 1. Geocoding
    address = '1600 Amphitheatre Parkway, Mountain View, CA'
    geocode_result = gmaps.geocode(address)
    lat = geocode_result[0]['geometry']['location']['lat']
    lng = geocode_result[0]['geometry']['location']['lng']

    # 2. Directions
    now = datetime.now()
    directions_result = gmaps.directions("Sydney Town Hall", "Parramatta, NSW",
                                         mode="transit", departure_time=now)
    steps_count = len(directions_result[0]['legs'][0]['steps'])

    # Simple HTML template for the webpage
    html_template = f"""
    <html>
        <head><title>Google Maps Webpage</title></head>
        <body>
            <h1>Google Maps Results</h1>
            <p><b>Address:</b> {address}</p>
            <p><b>Coordinates:</b> {lat}, {lng}</p>
            <p><b>Transit Directions:</b> {steps_count} steps found for your route.</p>
            <hr>
            <p>Data refreshed at: {now.strftime('%Y-%m-%d %H:%M:%S')}</p>
        </body>
    </html>
    """
    return render_template_string(html_template)

if __name__ == '__main__':
    # CRITICAL: Use 0.0.0.0 for GitHub Codespaces/Cloud environments
    app.run(host='0.0.0.0', port=5000)
