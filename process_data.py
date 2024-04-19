# process_data.py

def extract_required_data(data, min_rating=0):
    """
    Extracts restaurant data from the provided data dictionary based on the minimum rating criteria.

    Args:
        data (dict): A dictionary containing restaurant data.
        min_rating (float): The minimum rating criteria for filtering restaurants. Defaults to 0.

    Returns:
        list: A list of dictionaries containing information about filtered restaurants.
    """
    restaurants = data.get('restaurants', [])
    filtered_restaurants = []

    if not restaurants:
        print("No restaurant data available")
        return []

    try:
        min_rating = float(min_rating)
    except ValueError:
        print("Invalid min_rating value. Please provide a valid number.")
        return []

    if min_rating > 0:
        # Filtering based on the min_rating value provided or lower
        high_rated_restaurants = [
            restaurant for restaurant in restaurants
            if float(restaurant.get('rating', {}).get('starRating', 0)) < min_rating
        ]
    else:
        high_rated_restaurants = restaurants[:10]

    # Sort by rating in descending order
    sorted_restaurants = sorted(
        high_rated_restaurants,
        key=lambda x: float(x['rating']['starRating']), reverse=True
    )

    # Limit to the first 10 restaurants
    for restaurant in sorted_restaurants[:10]:
        # Extracting information similar to existing implementation
        address_parts = [
            restaurant.get('address', {}).get('firstLine', 'Address not available'),
            restaurant.get('address', {}).get('city', ''),
            restaurant.get('address', {}).get('postalCode', '')
        ]
        address = ', '.join(filter(None, address_parts))
        cuisines_list = restaurant.get('cuisines', [])
        cuisines = ', '.join(cuisine['name'] for cuisine in cuisines_list if 'name' in cuisine) if cuisines_list else 'Cuisine details not available'
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