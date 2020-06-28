#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, jsonify, request, send_file, make_response, url_for
from pymongo import MongoClient
app = Flask(__name__)
@app.route('/', methods=['GET'])
def home():
   return render_template('index1.html')


@app.route('/detail', methods=['GET'])
def detail(): 
   return render_template('link0.html')

@app.route('/detail/info', methods=['GET'])
def getDetailInfo():
   
   body = request.args.get('body')
   
   info = db.tattoos.find_one({'title': body},{'_id':0})
   return ({
      'title':info['title'],
      'body':info['body'],
      'level' :info['level'],
      'image' : info['image']
   })


client = MongoClient('localhost', 27017)
db = client.dbsparta
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)