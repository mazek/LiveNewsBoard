# LiveNewsBoard

[![Join the chat at https://gitter.im/mazek/LiveNewsBoard](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/mazek/LiveNewsBoard?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Live News Board - news, data, info aggregator.

Goal is to create simple server with rest api that collects information from many sources and provides it via it's api. Default as a auto refreshig webpage. Could be used as a info, twitter, currency, changes in infrastructure configuration, releases announcments etc log.


This is a learning project. Don't get too serious ;)

Any help and suggestion appreciated.



## What You need for sure.

virtualenv flask

./flask/bin/pip install flask

./flask/bin/pip install flask-httpauth



### Testing links, assuming Your app is at: http://localhost:5000/

#### Get all posts.
curl -i http://localhost:5000/lwb/api/v1.0/posts

#### Adding a post.
curl -i -H "Content-Type: application/json" -X POST -d '{"author": "jan dlugosz", "timestamp": 1422455451, "sec_level": 0, "priority": 0, "source": "twitter", "message": "Przykladowy post mowiacy o niczym"}' http://localhost:5000/lwb/api/v1.0/posts

#### Deleting a post.
curl -i -H "Content-Type: application/json" -X DELETE  http://localhost:5000/lwb/api/v1.0/posts/8


#### Not implemented yet:
curl -i -H "Content-Type: application/json" -X PUT -d '{"done":true}' http://localhost:5000/lwb/api/v1.0/posts/2

#### Simple auth test.
curl -u username:pass -i http://localhost:5000/lwb/api/v1.0/tasks


## What could be done later on.
*  Many sources of information

*  Different priorities - with influence on forrmatin and time of exopsure on the list.

*  Different classes of security with ragard to data protection (eg. no limit, internal information).

*  Aggregator gathering data into queue.

*  Data timeouting from the queue, maybe archived somehow?

*  Data with high priority on top of the queue?


## What sources of information could we use?

*  Information about releases?

*  Jira 

*  Planned changes from ChM

*  Planned technical breaks.

*  News athered from people (maybe as a pull requests introduced into the queue)

*  Twitter and observed accounts.

*  RSS feeds.

*  Exchange rates?

*  Stock exchange

*  Jabber channels.

* Hipchat rooms.



## Resources.
* http://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask

* http://codeforgeek.com/2014/09/refresh-div-angularjs-interval/

* http://codeforgeek.com/2014/09/two-way-data-binding-angularjs/

* http://tweetdump.info/320704340320993280/

* http://www.456bereastreet.com/lab/developing_with_web_standards/csslayout/2-col/

* https://docs.angularjs.org/api



