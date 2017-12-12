from flask import Flask, jsonify, request
from flask.ext.pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'connect_to_mongo'
app.config['MONGO_URI'] = 'mongodb://gf1721:password@ds135916.mlab.com:35916/connect_to_mongo'

mongo = PyMongo(app)

@app.route('/framework', methods=['GET'])
def get_all_frameworks():
    framework = mongo.db.frameworks
    
    output = []

    for q in framework.find():
        output.append({'name': q['name'], 'language': q['language']})

    return jsonify({'result': output})

@app.route('/framework/<name>', methods = ['GET'])
def get_one_framework(name):
    framework = mongo.db.frameworks
    q = framework.find_one({'name':name})
    if q: 
        output = {'name': q['name'], 'language': q['language']}    
    else:
        output = 'No results'
    return jsonify({'result' : output})
    
@app.route('/framework/', methods = ['POST'])
def add_framework():
    framework = mongo.db.frameworks
    
    name = request.json['name']
    language = request.json['language']

    framework_id = framework.insert({'name': name, 'language': language})
    new_framework = framework.find_one({'_id': framework_id})
    
    output = {'name': new_framework['name'],'language':new_framework['language']}
    
    
    return jsonify({'result' : output})

              
@app.route('/add')
def add():
    framework = mongo.db.frameworks
    framework.insert({'name':'Flask', 'language':'Python'})
    framework.insert({'name':'Lavarel', 'language':'PHP'})
    framework.insert({'name':'Express', 'language':'JS'})
    framework.insert({'name':'Rails', 'language':'Ruby'})
    
    return 'Added frameworks'
    
    
if __name__ == '__main__':
    app.run(debug=None)