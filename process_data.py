# process_data.py

def extract_required_data(data):
    # Assuming 'data' contains a key 'restaurants' directly with a list of restaurant data
    restaurants = data.get('restaurants', [])
    filtered_restaurants = []

    if not restaurants:
        print("No restaurant data available")
        return []

    for restaurant in restaurants[:10]:  # Limit to the first 10 restaurants
        # Constructing address from multiple fields if needed
        address_parts = [
            restaurant['address']['firstLine'],
            restaurant['address']['city'],
            restaurant['address']['postalCode']
        ]
        address = ', '.join(filter(None, address_parts))  # Join non-empty parts only

        restaurant_info = {
            'Name': restaurant.get('name', 'N/A'),
            'Cuisines': ', '.join(cuisine['name'] for cuisine in restaurant.get('cuisines', []) if 'name' in cuisine),
            'Rating': restaurant.get('rating', {}).get('starRating', 'No rating'),
            'Address': address
        }
        filtered_restaurants.append(restaurant_info)

    return filtered_restaurants




