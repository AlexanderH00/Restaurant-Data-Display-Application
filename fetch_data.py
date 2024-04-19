# fetch_data.py 

import requests
from process_data import extract_required_data

def fetch_restaurant_data(postcode):
    # Format and clean up the postcode
    formatted_postcode = postcode.replace(" ", "")
    # Debug: Check the formatted postcode
    print(f"Formatted postcode: {formatted_postcode}")  

    # API endpoint
    if not formatted_postcode:
        print("No postcode provided")
        return None  # Add handling for empty postcode
    
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

        # Log the entire JSON response to console for debugging
        print("Data retrieved successfully!")
        print("Raw API response data:")
        #print(data)  # This will print the whole JSON response to the console

        return data

    except requests.RequestException as e:
        # Handle any errors that occur during the HTTP request
        print(f"An error occurred during the HTTP request: {e}")
        # Optionally log the response status and text
        if response:
            print("HTTP Status Code:", response.status_code)
            print("Response Text:", response.text)

    except ValueError as e:
        # Handle JSON parsing errors
        print(f"Error parsing JSON response: {e}")

def main():
    postcode = "M160RA"
    data = fetch_restaurant_data(postcode)
    
    if data:
        filtered_restaurants = extract_required_data(data)
        if filtered_restaurants:
            for restaurant in filtered_restaurants:
                print(restaurant)
        else:
            print("No data to display.")

if __name__ == "__main__":
    main()