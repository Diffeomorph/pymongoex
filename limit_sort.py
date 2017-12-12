from flask import Flask
from flask.ext.pymongo import PyMongo, pymongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'connect_to_mongo'
app.config['MONGO_URI'] = 'mongodb://gf1721:Garden12@ds135916.mlab.com:35916/connect_to_mongo'

mongo = PyMongo(app)

@app.route('/')
def index():
    people = mongo.db.people
    results = people.find().sort('name', pymongo.ASCENDING).limit(1)
    
    output = ''
    for r in results:
        output += r['name'] + '<br>'
    
    return output
    
    
if __name__ == '__main__':
    app.run(debug=None)