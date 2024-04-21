# Restaurant-Data-Display-Application
 The Restaurant Data Display Application is a web-based solution designed to help users find restaurants based on their postcode and desired rating. This application queries an external API to retrieve restaurant data for a specific location and filters these results according to user preferences. The front-end provides a user-friendly interface where users can input a postcode, select a minimum rating, and view a list of restaurants that meet their criteria, complete with ratings, cuisines offered, and interactive maps.
# Restaurant Finder Web Interface
## Empty State
![Screenshot 2024-04-21 220856](https://github.com/AlexanderH00/Restaurant-Data-Display-Application/assets/149702761/3b8c506e-7ea6-4670-88aa-5d709e8d8c94)
This is the default state of the application when no search has been conducted.
## Search Results
![Screenshot 2024-04-21 221335](https://github.com/AlexanderH00/Restaurant-Data-Display-Application/assets/149702761/2dfbfe2a-abca-4a04-b9e8-b4613c239ca8)
Search results are displayed both in a list and on the map, providing useful information such as the restaurant name, cuisine, rating, and address.
## Main Interface with Map
![Screenshot 2024-04-21 220418](https://github.com/AlexanderH00/Restaurant-Data-Display-Application/assets/149702761/daf9283c-9e3b-4d8b-a653-497146b11eaf)
The main interface includes a search bar and a dynamically generated map showing restaurant locations.
# Features
 - Postcode Search: Users can enter a postcode to identify restaurants located within a specific geographic area. This feature simplifies the search process by localizing results.
 - Rating Filter: Users have the option to filter restaurant listings based on minimum star ratings, ranging from 1 to 5 stars. This feature helps users find higher-quality dining options according to their preferences.
 - Interactive Maps: Each restaurant listing is equipped with an interactive map that displays the restaurant's location. Users can toggle the visibility of the map by clicking on the address, making it easier to visualize the restaurant's location.
 - Responsive Design: The application is designed to be functional and accessible across a variety of devices and screen sizes, ensuring a consistent user experience whether on a desktop, tablet, or mobile device.
 - Data Fetching: The application dynamically retrieves restaurant data based on the user-provided postcode, ensuring that the results are relevant to the specified area.
 - Data Filtering: This process only extracts relevant data from the API's response. The application focuses on displaying the restaurant's name, types of cuisines offered, ratings, and address, which are pertinent details for users making dining decisions.
 - Limited Data Display: To maintain clarity and prevent information overload, the application limits the display to the first 10 restaurants that meet the search criteria. This approach enhances the usability of the application by simplifying the user interface.
 - Error Handling: The application includes basic error handling mechanisms to address issues such as API connectivity problems and data processing errors. This ensures that the application remains robust and user-friendly, even when external dependencies encounter issues.
   Collectively, these features are designed to create an intuitive, efficient, and effective platform for users to search for and assess dining options based on specific criteria.
 # Technologies Used
 - Python: Main programming language used for backend development.
 - Flask: Lightweight WSGI web application framework used to handle requests and serve the HTML content.
 - HTML/CSS: Used for structuring and styling the web interface.
 - JavaScript: Enhances interactivity on the client side, particularly for map integration.
 - Requests Library: Enables HTTP requests to external APIs in Python.
 - JSON: For parsing and handling data returned from the Just Eat API, crucial for data exchange between the application and external services.
 - Just Eat API: External API used for fetching restaurant data.
 # Installation
- Clone the Repository:
  - git clone https://github.com/AlexanderH00/restaurant-data-display.git
  - cd restaurant-data-display-application
- Install Dependencies:
  - pip install flask requests
# How to Run
To start the application, run the following command in the terminal:
- python app.py
Once the server starts, access the application through your web browser at http://localhost:5000/.
# Data Source
The restaurant data is sourced from the Just Eat API, which provides comprehensive information about restaurants in the UK, searchable by postcode.
# Additional Notes for README
- Assumptions:
  - The Just Eat API endpoint is currently functional and accessible without API keys for development purposes.
  - Restaurants in the API response are assumed to have ratings, address information, and at least one cuisine listed.
- Possible Improvements:
  - Caching: Implement caching to reduce API calls for the same postcode and rating searches, enhancing performance and user experience.
  - User Authentication: Add user accounts for personalized experiences such as saving favorite restaurants or previous searches.
  - Advanced Filters: Include filters for price, distance, or specific cuisines to refine search results further.
  - Feedback System: Incorporate a user feedback system to rate the usability of the application and gather user-generated restaurant reviews.
