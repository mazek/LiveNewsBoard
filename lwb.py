#!flask/bin/python

from flask import Flask, jsonify, abort, make_response, request, url_for, send_from_directory
from flask.ext.httpauth import HTTPBasicAuth
import sqlite3
import lwb_db

auth = HTTPBasicAuth()
app = Flask(__name__)
db = sqlite3.connect('lwb.db')

@app.route('/www/<path:filename>')
def send_foo(filename):
   return send_from_directory('./www',filename)

@app.route('/lwb/api/v1.0/posts', methods=['GET'])
def get_posts():
   posts = []
   db = sqlite3.connect('lwb.db')
   posts = lwb_db.get_messages(db,100)
   db.close()
   return jsonify({'posts':posts})
#   return jsonify({'posts': [make_public_post(post) for post in posts]})

@app.route('/lwb/api/v1.0/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    db = sqlite3.connect('lwb.db')
    post = lwb_db.get_message_by_id(db,post_id)
    db.close()
    if len(post) == 0:
        abort(404)
    return jsonify({'post': post})

@app.route('/lwb/api/v1.0/posts', methods=['POST'])
def create_post():
    if not request.json or not 'message' in request.json:
        abort(400)
    db = sqlite3.connect('lwb.db')
    post_id = lwb_db.put_post(db, request.json['timestamp'], request.json['priority'], request.json['sec_level'], 
			request.json['author'], request.json['source'], request.json['message'])
    post = lwb_db.get_message_by_id(db,post_id)
    db.close()
    if len(post) == 0:
        abort(404)
    return jsonify({'post': post}), 201    

@app.route('/lwb/api/v1.0/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    db = sqlite3.connect('lwb.db')
    rowcount = lwb_db.delete_post(db, post_id)
    db.commit()
    db.close()
    if rowcount == 0:
        abort(404)
    return jsonify({'result': True})



@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

def make_public_post(post):
    new_post = {}
    for field in post:
        if field == 'id':
            new_post['uri'] = url_for('get_post', post_id=post['id'], _external=True)
        else:
            new_post[field] = post[field]
    return new_post

@auth.get_password
def get_password(username):
    if username == 'test':
        return 'test'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 403)


if __name__ == '__main__':
   db = sqlite3.connect('lwb.db')
   app.run(debug=True)
   db.close()

