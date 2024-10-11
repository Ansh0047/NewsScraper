from flask import Flask, render_template, jsonify
from scraper import bbcNews,fitnessNews,sportsNews,timesOfIndia,techNews,save_data

app = Flask(__name__)

user_clicks = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/bbc')
def bbc():
    headlines = bbcNews()
    return jsonify(headlines)
 
@app.route('/toi')
def toi():
    headlines = timesOfIndia()
    return jsonify(headlines)

@app.route('/fitness')
def fitness():
    headlines = fitnessNews()
    return jsonify(headlines)

@app.route('/tech')
def tech():
    headlines = techNews()
    return jsonify(headlines)

@app.route('/sports')
def sports():
    headlines = sportsNews()
    return jsonify(headlines)


if __name__ == '__main__':
    # save_data()
    app.run(debug=True)
