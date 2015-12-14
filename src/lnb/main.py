# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import sys
import os

import flask
from flask import (
    Flask, jsonify, abort, make_response, request, url_for,
    send_from_directory)
from flask.ext.httpauth import HTTPBasicAuth

from lnb.storage.redis import RedisStorage  # change to SqliteStorage if want


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'


# choose storage
storage = RedisStorage()
auth = HTTPBasicAuth()
app = Flask(__name__)


static_path = os.path.dirname(__file__) + "/../www/"


@app.route('/www/<path:filename>')
def send_foo(filename):
    return send_from_directory(static_path, filename)


@app.route('/api/v1.0/posts', methods=['GET'])
def get_posts():
    posts = []
    posts = storage.get_posts(10)
    return jsonify({'posts': list(posts)})


@app.route('/api/v1.0/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = storage.get_post_by_id(post_id)
    if len(post) == 0:
        abort(404)
    return jsonify({'post': post})


@app.route('/api/v1.0/posts', methods=['POST'])
def create_post():
    if not request.json or 'message' not in request.json:
        abort(400)
    post_uid = storage.put_post(
        request.json['priority'], request.json['sec_level'],
        request.json['author'], request.json['source'],
        request.json['message'])
    post = storage.get_post_by_uid(post_uid)
    if len(post) == 0:
        abort(404)
    return jsonify({'post': post}), 201


@app.route('/api/v1.0/posts/<int:post_id>', methods=['DELETE'])
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


def __main__():
    parser = argparse.ArgumentParser(description='Live News Board')
    parser.add_argument('--generate-fixtures', action='store_const',
                        const=True, default=False,
                        help='Generate sample demo data and run server',
                        dest='fixtures')

    args = parser.parse_args()
    if args.fixtures:
        storage.generate_fixtures()
        sys.exit(0)
    app.run(debug=True)


if __name__ == '__main__':
    __main__()
