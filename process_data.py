# process_data.py

def extract_required_data(data, min_rating=5):
    restaurants = data.get('restaurants', [])
    filtered_restaurants = []

    if not restaurants:
        print("No restaurant data available")
        return []

    # Filtering and sorting
    high_rated_restaurants = [
        restaurant for restaurant in restaurants
        if restaurant.get('rating', {}).get('starRating', 0) >= min_rating
    ]
    
    # Sort by rating in descending order
    sorted_restaurants = sorted(
        high_rated_restaurants, 
        key=lambda x: x['rating']['starRating'], reverse=True
    )
    
    for restaurant in restaurants[:10]:  # Process only the first 10 restaurants
        # Safely extracting address parts with fallbacks for missing data
        address_parts = [
            restaurant.get('address', {}).get('firstLine', 'Address not available'),
            restaurant.get('address', {}).get('city', ''),
            restaurant.get('address', {}).get('postalCode', '')
        ]
        address = ', '.join(filter(None, address_parts))  # Join non-empty parts only

        # Extracting cuisines safely, handling cases where 'cuisines' might be missing or empty
        cuisines_list = restaurant.get('cuisines', [])
        cuisines = ', '.join(cuisine['name'] for cuisine in cuisines_list if 'name' in cuisine) if cuisines_list else 'Cuisine details not available'

        # Extracting name and rating with defaults
        name = restaurant.get('name', 'Name not available')
        rating = restaurant.get('rating', {}).get('starRating', 'Rating not available')

        restaurant_info = {
            'Name': name,
            'Cuisines': cuisines,
            'Rating': rating,
            'Address': address
        }
        filtered_restaurants.append(restaurant_info)

    return filtered_restaurants
