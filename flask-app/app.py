from flask import Flask, jsonify, render_template
from flask_cors import CORS, cross_origin

app = Flask(__name__, static_url_path='/static')
cors = CORS(app)

movies = [
    {
        "name": "The Shawshank Redemption",
        "casts": [
            "Tim Robbins",
            "Morgan Freeman",
            "Bob Gunton",
            "William Sadler"
        ],
        "genres": ["Drama"]
    },
    {
        "name": "The Godfather ",
        "casts": [
            "Marlon Brando",
            "Al Pacino",
            "James Caan",
            "Diane Keaton"
        ],

        "genres": ["Crime", "Drama"]
    }
]

cartoons = [
    {
        "name": "Tom and Jerry",
        "startYear": 1935,
        "production": "Fred Quimby"
    },
    {
        "name": "The Powerpuff Girls",
        "startYear": 1980,
        "production": "Cartoon Network"
    },
    {
        "name": "Spongebob",
        "startYear": 1995,
        "production": "Nicklodeon"
    }
]


@app.route('/flask-home')
def root():
    return render_template('index.html')


@app.route('/flask-movies')
def movie_list():
    return jsonify(movies)


@app.route('/flask-cartoons')
def cartoon_list():
    return jsonify(cartoons)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
