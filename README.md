# Hotel Reservation System API

The Hotel Reservation System API provides a simple interface for managing hotel reservations. This document outlines how to set up the project, run the server, and interact with the API to list all hotels and add a new hotel.

## Setup Instructions

1. **Clone the repository**
   - Clone the project to your local machine using `git clone`, followed by the repository URL.

2. **Create a virtual environment** (Optional but recommended)
   - Navigate to the project directory in your terminal.
   - Create a virtual environment by running `python -m venv venv`.
   - Activate the virtual environment:
     - On Windows, use `venv\Scripts\activate`.
     - On Unix or MacOS, use `source venv/bin/activate`.

3. **Install dependencies**
   - Install the required Python packages by running `pip install -r requirements.txt`.

4. **Database migrations**
   - Apply database migrations using `python manage.py migrate`.

5. **Start the development server**
   - Run `python manage.py runserver`.

## API Endpoints

### List All Hotels

- **Method:** GET
- **URL:** `http://127.0.0.1:8000/reservations/hotels/`
- **Curl Example:**

```bash
curl --location 'http://127.0.0.1:8000/reservations/hotels/'
```

### Add a New Hotel

- **Method:** POST
- **URL:** `http://127.0.0.1:8000/reservations/hotels/`
- **Content-Type:** `application/json`
- **Data:** JSON object containing `hotelName`, `hotelAvailability`, and `hotelPrice`.
- **Curl Example:**

```bash
curl --location 'http://127.0.0.1:8000/reservations/hotels/' \
--header 'Content-Type: application/json' \
--data '{
    "hotelName": "Sapphire Hotel",
    "hotelAvailability": true,
    "hotelPrice": "350.00"
}'
```
