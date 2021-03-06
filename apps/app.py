from flask import Flask, render_template
from flask_pymongo import PyMongo
import scraping_challenge
app = Flask(__name__)
# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Route to Index
@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   # print("-------------")
   # print(mars)
   # print("---------------")
   return render_template("indextest.html", mars=mars)

@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping_challenge.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return "Scraping Successful!"
   
if __name__ == "__main__":
   app.run()