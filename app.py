from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mars_scrape

app = Flask(__name__)

mongo = PyMongo(app, uri='mongodb://localhost:27017/mars_app')


@app.route('/')
def home():
    mars_df = mongo.db.collection.find_one()
    return render_template('mars_facts.html', redplanet = mars_df)

@app.route('/scraping')
def scraping():
    m_scrape = mars_scrape.scrape()
    print('\n\n')
    print(mongo.db.collection, flush=True)
    mongo.db.collection.insert_many(m_scrape.to_dict('records'))
    return "Good"




if __name__ == '__main__':
    app.debug=True
    app.run()







