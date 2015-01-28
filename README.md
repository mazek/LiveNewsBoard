# LiveNewsBoard
Live News Board - news, data, info aggregator.

This is a learning project. Don't get to serious ;)

Any help and suggestion appreciated.

# Resources.
1) http://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask

# What You need for sure.
virtualenv flask
./flask/bin/pip install flask
./flask/bin/pip install flask-httpauth

# Testing links, assuming Your app is at: http://localhost:5000/

# Get all posts.
curl -i http://localhost:5000/lwb/api/v1.0/posts

# Adding a post.
curl -i -H "Content-Type: application/json" -X POST -d '{"author": "jan dlugosz", "timestamp": 1422455451, "sec_level": 0, "priority": 0, "source": "twitter", "message": "Przykladowy post mowiacy o niczym"}' http://localhost:5000/lwb/api/v1.0/posts

# Not yet:
curl -i -H "Content-Type: application/json" -X PUT -d '{"done":true}' http://localhost:5000/lwb/api/v1.0/posts/2

# Simple auth test.
curl -u username:pass -i http://localhost:5000/lwb/api/v1.0/tasks

# Deleting a post.
curl -i -H "Content-Type: application/json" -X DELETE  http://localhost:5000/lwb/api/v1.0/posts/8

# What could be done later on.
Wiele źródeł informacji z modularną budową.
Różne źródła mają różne priorytety - wpływa na ich formatowanie i czas wyświetlania.
Różne źródła mają różne klasy ochrony danych (np. bez ograniczeń, wewnętrzne).

Agregator zbierający dane w formie kolejki danych.
Dane wygasają po x minutach z kolejki, archiwizowane?
Czy dane o większej pilności wpadają na początek kolejki?


Jakie informacje, źródła informacji:
informacje o wdrożeniach - czyli np jira
informacje o wprowadzanych zmianach
ciekawostki wysyłane przez ludzi wprowadzane przez pull requesty do kolejki
twitter i obserwowane konta
feedy rss
kursy walut
giełda
kanał jabberowy (np. awaria)
kanał hipchatowy (np. awaria)

Format informacji tekstowy lub graficzny.

Wysyłany tekst formatowany za pomoca tagów markdown?

