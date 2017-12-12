from flask import Flask
from flask.ext.pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'connect_to_mongo'
app.config['MONGO_URI'] = 'mongodb://gf1721:Garden12@ds135916.mlab.com:35916/connect_to_mongo'

mongo = PyMongo(app)

@app.route('/add')
def add():
    user = mongo.db.users
    user.insert({'name':'Anthony'})
    return 'Added USer'
    
if __name__ == '__main__':
    app.run(debug=None)