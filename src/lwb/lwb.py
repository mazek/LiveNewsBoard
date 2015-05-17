#!flask/bin/python
# -*- coding: utf-8 -*-

from flask import (
  Flask, jsonify, abort, make_response, request, url_for, send_from_directory)
from flask.ext.httpauth import HTTPBasicAuth

from lwb_redis import RedisStorage
from lwb_db import SqliteStorage

# choose storage
storage = RedisStorage()
auth = HTTPBasicAuth()
app = Flask(__name__)


@app.route('/www/<path:filename>')
def send_foo(filename):
    return send_from_directory('./www', filename)


@app.route('/lwb/api/v1.0/posts', methods=['GET'])
def get_posts():
    posts = []
    storage.get_messages(10)
    return jsonify({'posts': posts})


@app.route('/lwb/api/v1.0/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = storage.get_message_by_id(post_id)
    if len(post) == 0:
        abort(404)
    return jsonify({'post': post})


@app.route('/lwb/api/v1.0/posts', methods=['POST'])
def create_post():
    if not request.json or 'message' not in request.json:
        abort(400)
    post_id = storage.put_post(request.json['timestamp'], request.json['priority'], request.json['sec_level'],
                              request.json['author'], request.json['source'], request.json['message'])
    post = storage.get_message_by_id(post_id)
    if len(post) == 0:
        abort(404)
    return jsonify({'post': post}), 201


@app.route('/lwb/api/v1.0/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    storage.delete_post(post_id)
    return jsonify({'result': True})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


def make_public_post(post):
    new_post = {}
    for field in post:
        if field == 'id':
            new_post['uri'] = url_for(
                'get_post', post_id=post['id'], _external=True)
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
    app.run(debug=True)
