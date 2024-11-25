from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Route for Home Page
@app.route('/')
def home():
    return render_template('home.html', suggestions=get_movie_suggestions())

# Route for Movie Recommendation Page
@app.route('/recommendation', methods=['POST'])
def recommendation():
    movie_name = request.form['movie']
    movie_details = get_movie_details(movie_name)  # Fetch the movie details
    return render_template('recommendation.html', movie=movie_details)

def get_movie_suggestions():
    # Implement logic to fetch movie suggestions
    return ['Inception', 'Titanic', 'The Dark Knight']

def get_movie_details(movie_name):
    # Use the OMDb API or any other movie database to fetch movie details
    # Example: Replace with actual API request
    api_key = "your_omdb_api_key"
    url = f"http://www.omdbapi.com/?t={movie_name}&apikey={api_key}"
    response = requests.get(url)
    return response.json()

if __name__ == '__main__':
    app.run(debug=True)
