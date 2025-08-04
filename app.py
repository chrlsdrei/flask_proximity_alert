from flask import Flask, request, jsonify
from geopy.distance import geodesic
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/check_proximity', methods=['POST'])
def check_proximity():
    # Get data from the incoming request
    data = request.get_json()

    # Extract coordinates and radius from the data
    warehouse_coords = tuple(data['warehouse'])  # [lat, lng]
    delivery_coords = tuple(data['delivery'])   # [lat, lng]
    radius = data.get('radius', 250)         # in meters

    # Calculate the distance in meters
    distance = geodesic(warehouse_coords, delivery_coords).meters

    # Check if the distance is within the specified radius
    is_within_range = distance <= radius

    # Return the results as a JSON response
    return jsonify({
        'distance': round(distance, 2),
        'within_range': is_within_range
    })

if __name__ == '__main__':
    app.run(debug=True)