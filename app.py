from flask import Flask, render_template, request
import fetch_data
import process_data

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        postcode = request.form.get('postcode', '')
        if not postcode:
            print("Error: Please enter a postcode.")
            return render_template('home.html', error="Please enter a postcode.")

        data = fetch_data.fetch_restaurant_data(postcode)
        if data:
            restaurants = process_data.extract_required_data(data, min_rating=5)  # Assuming min_rating is now a parameter in your function
            print("Restaurants:", restaurants)  # Debug print the list of restaurants
            if restaurants:
                return render_template('home.html', restaurants=restaurants, postcode=postcode)
            else:
                print("Error: No high-rated restaurants found.")  # Debug print when no high-rated restaurants are found
                return render_template('home.html', error="No high-rated restaurants found.")
        else:
            print("Error: No data available for this postcode.")  # Debug print when no data is available
            return render_template('home.html', error="No data available for this postcode.")
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)