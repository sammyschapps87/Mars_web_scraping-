from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mars_scrape

app = Flask(__name__)

mongo = PyMongo(app, uri='mongodb://localhost:27017/mars_app')

@app.route('/scraping')
def scraping():
    m_scrape = mars_scrape.scrape()
    mongo.db.collection.update({}, m_scrape, upsert = True)
    return "Good"

@app.route('/')
def home():
    mars_df = mongo.db.collection.find_one()
    return render_template('mars_facts.htmml', redplanet = mars_df)


if __name__ == '__main__':
    app.run()







