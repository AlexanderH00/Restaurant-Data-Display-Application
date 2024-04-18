# fetch_data.py 

import requests
from process_data import extract_required_data

def fetch_restaurant_data(postcode):
    # Format and clean up the postcode
    formatted_postcode = postcode.replace(" ", "")

    # API endpoint
    url = f"https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{formatted_postcode}"

    # Set the User-Agent header
    headers = {
        "User-Agent": "MyRestaurantApp/1.0"
    }

    try:
        # Send GET request with headers
        response = requests.get(url, headers=headers)

        # Raise an exception for bad responses (4xx or 5xx)
        response.raise_for_status()

        # Parse the JSON data from the response
        data = response.json()
        print("Data retrieved successfully!")
        return data

    except requests.RequestException as e:
        # Handle any errors that occur during the HTTP request
        print(f"An error occurred during the HTTP request: {e}")

    except ValueError as e:
        # Handle JSON parsing errors
        print(f"Error parsing JSON response: {e}")

def main():
    postcode = "M160RA"
    data = fetch_restaurant_data(postcode)
    print(data)
    
    if data:
        filtered_restaurants = extract_required_data(data)
        if filtered_restaurants:
            for restaurant in filtered_restaurants:
                print(restaurant)
        else:
            print("No data to display.")

if __name__ == "__main__":
    main()
