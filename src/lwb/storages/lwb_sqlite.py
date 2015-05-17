#!/usr/bin.python
#!/usr/bin.python

import sqlite3
from time import time
import os

dbfile='lwb.db'
db = None

def create_db():
	try:
		db = sqlite3.connect(dbfile)

		cursor = db.cursor()
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
		db.rollback()
		#raise e

	finally:
		db.close()


def put_post(db, timestamp, priority, sec_level, author, source, message):
	cursor = db.cursor()
	cursor.execute('''SELECT max(id) from posts''')
	post_id = cursor.fetchone()[0] + 1
	db.execute('''
		INSERT INTO posts(id, timestamp, priority,sec_level,author,source,message)
		VALUES (?, ?, ?, ?, ?, ?, ?)
	''', (post_id, timestamp, priority, sec_level, author, source, message))
	db.commit()
	return post_id

def get_messages(db,limit = 0):
	posts = []
	cursor = db.cursor()
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
	print posts
	return posts

def get_message_by_id(db,id = 0):
	post = {}
	cursor = db.cursor()
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
	print post
	return post

def get_messages_timestamp_range(db,timestamp_start, timestamp_end):
	posts = []
	cursor = db.cursor()
	cursor.execute('''SELECT * from posts WHERE timestamp >= %s and timestamp <= %s ''' % (timestamp_start, timestamp_end))
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
	print posts
	return posts

def delete_post(db, post_id):
	rowcount = 0
	rowcount = db.execute("delete from posts where id = %s" % post_id).rowcount
	return rowcount

def put_some_data(db):
	db.execute('''
			INSERT INTO users(id, username, password) VALUES (1,'mazek','test')
		''')
	ts = int(time())
	db.execute('''
			INSERT INTO posts(id, timestamp, priority,sec_level,author,source,message)
			VALUES (1 ,? ,0 ,0 , 'jan dlugosz', 'twitter', 'Przykladowy post mowiacy o niczym')
	''', (ts,))
	ts = int(time())+2
	db.execute('''
			INSERT INTO posts(id, timestamp, priority,sec_level,author,source,message)
			VALUES (2 ,? , 1, 0, 'ada nowak', 'ulica', 'Kolejny post mowiacy o niczym')
	''', (ts,))
	ts = int(time())+4
	db.execute('''
			INSERT INTO posts(id, timestamp, priority,sec_level,author,source,message)
			VALUES (3 ,? , 0, 1, 'john smith', 'kuchnia', 'Jeszcze inny post mowiacy o niczym')
	''', (ts,))
	ts = int(time())+8
	db.execute('''
			INSERT INTO posts(id, timestamp, priority,sec_level,author,source,message)
			VALUES (4 ,? , 1, 1, 'jan kowalski', 'fajka', 'To jest post mowiacy o niczym')
	''', (ts,))
	db.commit()



if __name__ == "__main__":

	if not os.path.isfile(dbfile):
		create_db()
		db = sqlite3.connect(dbfile)
		put_some_data(db)
	else:
		db = sqlite3.connect(dbfile)
#	get_messages(db,100)
	post_id = put_post(db, 1422399346, 1, 0, 'ktos', 'cos', 'jakis message')
	print "\n\n"
	get_message_by_id(db,post_id)
#	get_messages_timestamp_range(db, 1422399346, 1422399350)
	db.close()

