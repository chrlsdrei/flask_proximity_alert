# Flask Proximity Alert

A Flask-based web service that calculates the proximity between warehouse and delivery locations.

## Features

- Calculate distance between two geographic coordinates
- Check if delivery location is within a specified radius of warehouse
- RESTful API endpoint for proximity checking
- CORS enabled for cross-origin requests

## API Usage

### Endpoint: `/check_proximity`

**Method:** POST

**Request Body:**
```json
{
  "warehouse": [latitude, longitude],
  "delivery": [latitude, longitude],
  "radius": 250
}
```

**Response:**
```json
{
  "distance": 150.25,
  "within_range": true
}
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/chrlsdrei/proximity-alert.git
cd proximity-alert
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
```bash
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

```bash
python app.py
```

The server will start on `http://localhost:5000`

## Example Usage

```bash
curl -X POST http://localhost:5000/check_proximity \
  -H "Content-Type: application/json" \
  -d '{
    "warehouse": [40.7128, -74.0060],
    "delivery": [40.7589, -73.9851],
    "radius": 5000
  }'
```

## Dependencies

- Flask: Web framework
- geopy: Geographic distance calculations
- flask-cors: Cross-origin resource sharing 