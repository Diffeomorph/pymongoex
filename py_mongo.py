from flask import Flask
from flask.ext.pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'connect_to_mongo'
app.config['MONGO_URI'] = 'mongodb://gf1721:password@ds135916.mlab.com:35916/connect_to_mongo'

mongo = PyMongo(app)

@app.route('/add')
def add():
    user = mongo.db.users
    user.insert({'name':'Anthony', 'language':'Python'})
    user.insert({'name':'Kelly', 'language':'C'})
    user.insert({'name':'John', 'language':'Java'})
    user.insert({'name':'Cedric', 'language':'Haskell'})
    return 'Added USer'
    
@app.route('/find')
def find():
    user = mongo.db.users
    cedric = user.find_one({'name':'Cedric'})
    return 'You found '+ cedric['name']+ ' his favorit elangueg is ' + cedric['language']

@app.route('/update')
def update():
    user = mongo.db.users
    john = user.find_one({'name':'John'})
    john['language'] = 'JS'
    user.save(john)
    return 'updated john'
    
@app.route('/delete')
def delete():
    user = mongo.db.users
    kelly = user.find_one({'name': 'Kelly'})
    #kelly.remove()
    user.remove(kelly)
    return 'removed'

    
if __name__ == '__main__':
    app.run(debug=None)