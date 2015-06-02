# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import redis
import json

import hashlib
import time

from lnb.storage.base import Storage


class RedisStorage(Storage):

    def __init__(self):
        db = 0
        self.r = redis.StrictRedis(host='localhost', port=6379, db=db)

    def create_db(self):
        pass

    def make_pk(self, timestamp, message, source, author):
        key = ''.join([str(timestamp), message, source, author])
        return hashlib.sha1(key).hexdigest()

    def put_post(self, priority, sec_level,
                 author, source, message):
        timestamp = time.time()
        pk = self.make_pk(timestamp, message, source, author)
        self.r.rpush('posts', pk)
        self.r.hmset('post:%s' % pk, (dict(
            uid=pk,
            timestamp=timestamp,
            priority=priority,
            sec_level=sec_level,
            author=author,
            source=source,
            message=message
        )))
        return pk

    def get_posts(self, limit=100):
        for i in self.r.lrange('posts', 0, limit):
            pk = i
            yield self.r.hgetall('post:%s' % pk)

    def get_post_by_uid(self, uid=0):
        result = dict(uid=uid)
        result.update(self.r.hgetall('post:%s' % uid))
        return result

    def get_posts_timestamp_range(self, timestamp_start, timestamp_end):
        pass

    def delete_post(self, post_id):
        pass

    def generate_fixtures(self):
        for source, message in (
            ('pylabs-releases', 'Vipmaker 1.0 released!'),
            ('pylabs-releases', 'Tycho 1.0 released!'),
            ('pylabs-releases', 'Ralph 3.0-pre1 released!'),
                ):
            self.put_post(10, 0,
                   'marcin.kliks', source, message)
        for i in self.get_posts():
            print(i)
            print("ID: {id} Author: {author} Source: {source} "
                  "Message: {message}".format(
                   id=i['uid'],
                   author=i['author'], source=i['source'],
                   message=i['message']
                   )
                  )
Storage.register(RedisStorage)
