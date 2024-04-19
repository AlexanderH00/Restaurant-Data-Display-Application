from flask import Flask, render_template, request
from fetch_data import fetch_restaurant_data
from process_data import extract_required_data

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        postcode = request.form.get('postcode', '')
        min_rating = int(request.form.get('min_rating', 0))  # Default to 0 if not provided

        if not postcode:
            return render_template('home.html', error="Please enter a postcode.")

        data = fetch_restaurant_data(postcode)
        if data:
            restaurants = extract_required_data(data, min_rating=min_rating)
            if restaurants:
                return render_template('home.html', restaurants=restaurants, postcode=postcode, min_rating=min_rating)
            else:
                return render_template('home.html', error="No suitable restaurants found.")
        else:
            return render_template('home.html', error="No data available for this postcode.")
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)