# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sqlite3
from time import time

from lwb.storage.base import Storage
import os

dbfile = 'lwb.db'
db = None


class SqliteStorage(Storage):

    def __init__(self):
        if not os.path.isfile(dbfile):
            self.create_db()
            self.db = sqlite3.connect(dbfile)
            self.put_some_data()
        else:
            self.db = sqlite3.connect(dbfile)
        post_id = self.put_post(
            1422399346, 1, 0, 'ktos', 'cos', 'jakis message')
        self.get_message_by_id(db, post_id)
        self.db.close()

    def create_db(self):
        try:
            self.db = sqlite3.connect(dbfile)

            cursor = self.db.cursor()
            cursor.execute('''
			    CREATE TABLE users(id INTEGER PRIMARY KEY,  username TEXT unique, password TEXT)
			''')

            cursor.execute('''
			    CREATE TABLE posts(id INTEGER PRIMARY KEY,
					timestamp  INTEGER,
					priority INTEGER,
					sec_level INTEGER,
					author TEXT,
					source TEXT,
					message TEXT)
			''')
        except Exception as e:
            self.db.rollback()
            #raise e

        finally:
            self.db.close()

    def put_post(self, timestamp, priority, sec_level, author, source, message):
        cursor = self.db.cursor()
        cursor.execute('''SELECT max(id) from posts''')
        post_id = cursor.fetchone()[0] + 1
        self.db.execute('''
			INSERT INTO posts(id, timestamp, priority,sec_level,author,source,message)
			VALUES (?, ?, ?, ?, ?, ?, ?)
		''', (post_id, timestamp, priority, sec_level, author, source, message))
        self.db.commit()
        return post_id

    def get_messages(self, limit=0):
        posts = []
        cursor = self.db.cursor()
        cursor.execute('''SELECT * from posts LIMIT %s ''' % limit)
        for row in cursor:
            post = {
                'id': row[0],
                'timestamp': row[1],
                'priority': row[2],
                'sec_level': row[3],
                'author': row[4],
                'source': row[5],
                'message': row[6],
            }
            posts.append(post)
        return posts

    def get_message_by_id(self, id=0):
        post = {}
        cursor = self.db.cursor()
        cursor.execute('''SELECT * from posts WHERE id = %s ''' % id)
        for row in cursor:
            post = {
                'id': row[0],
                'timestamp': row[1],
                'priority': row[2],
                'sec_level': row[3],
                'author': row[4],
                'source': row[5],
                'message': row[6],
            }
        return post

    def get_messages_timestamp_range(self, timestamp_start, timestamp_end):
        posts = []
        cursor = self.db.cursor()
        cursor.execute('''SELECT * from posts WHERE timestamp >= %s and timestamp <= %s ''' %
                       (timestamp_start, timestamp_end))
        for row in cursor:
            post = {
                'id': row[0],
                'timestamp': row[1],
                'priority': row[2],
                'sec_level': row[3],
                'author': row[4],
                'source': row[5],
                'message': row[6],
            }
            posts.append(post)
        return posts

    def delete_post(self, post_id):
        rowcount = 0
        rowcount = self.db.execute(
            "delete from posts where id = %s" % post_id).rowcount
        return rowcount

    def put_some_data(self):
        self.db.execute('''
				INSERT INTO users(id, username, password) VALUES (1,'mazek','test')
			''')
        ts = int(time())
        self.db.execute('''
				INSERT INTO posts(id, timestamp, priority,sec_level,author,source,message)
				VALUES (1 ,? ,0 ,0 , 'jan dlugosz', 'twitter', 'Przykladowy post mowiacy o niczym')
		''', (ts,))
        ts = int(time())+2
        self.db.execute('''
				INSERT INTO posts(id, timestamp, priority,sec_level,author,source,message)
				VALUES (2 ,? , 1, 0, 'ada nowak', 'ulica', 'Kolejny post mowiacy o niczym')
		''', (ts,))
        ts = int(time())+4
        self.db.execute('''
				INSERT INTO posts(id, timestamp, priority,sec_level,author,source,message)
				VALUES (3 ,? , 0, 1, 'john smith', 'kuchnia', 'Jeszcze inny post mowiacy o niczym')
		''', (ts,))
        ts = int(time())+8
        self.db.execute('''
				INSERT INTO posts(id, timestamp, priority,sec_level,author,source,message)
				VALUES (4 ,? , 1, 1, 'jan kowalski', 'fajka', 'To jest post mowiacy o niczym')
		''', (ts,))
        self.db.commit()
